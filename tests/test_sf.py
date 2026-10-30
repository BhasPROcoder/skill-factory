"""Regression tests for failure reporting and safe registry ingestion."""
import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import sf


class RegistrySafety(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.saved = {k: getattr(sf, k) for k in ['REG', 'DOM', 'MAC', 'SK']}
        for key, path in [('REG','skills.jsonl'),('DOM','domains.jsonl'),('MAC','macros.json'),('SK','skills')]:
            setattr(sf,key,str(self.root/path))
        Path(sf.REG).write_text('', encoding='utf-8')
        Path(sf.DOM).write_text('', encoding='utf-8')
        Path(sf.MAC).write_text('["Writing & Editing"]', encoding='utf-8')

    def tearDown(self):
        for key,value in self.saved.items():
            setattr(sf,key,value)
        self.temp.cleanup()

    def invoke(self, function, args):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            try:
                function(args)
            except SystemExit as error:
                return error.code, output.getvalue()
        return 0, output.getvalue()

    def test_unknown_id_is_failure(self):
        code, output = self.invoke(sf.cmd_validate,['ZZZ-001'])
        self.assertEqual(code,1)
        self.assertIn('not in registry',output)

    def test_invalid_file_returns_failure(self):
        path=self.root/'invalid.md'
        path.write_text('not a skill',encoding='utf-8')
        code, _ = self.invoke(sf.cmd_validate,['--file',str(path)])
        self.assertEqual(code,1)

    def test_missing_file_returns_failure(self):
        code, output = self.invoke(sf.cmd_validate,['--file',str(self.root/'absent.md')])
        self.assertEqual(code,1)
        self.assertIn('file missing',output)

    def test_migration_rejects_unmapped_source(self):
        source = self.root / 'source'
        (source / 'unmapped').mkdir(parents=True)
        (source / 'unmapped' / 'SKILL.md').write_text('source', encoding='utf-8')
        mapping = self.root / 'mapping.json'
        mapping.write_text('[]', encoding='utf-8')
        code, _ = self.invoke(sf.cmd_migration_check, [str(source), str(mapping)])
        self.assertIn('unmapped sources', str(code))

    def test_removal_receipt_rejects_changed_target(self):
        source = self.root / 'removed-source'
        row = dict(id='ZZ-001', name='fixture-review', domain_code='ZZ', status='validated')
        Path(sf.REG).write_text(json.dumps(row) + '\n', encoding='utf-8')
        target = Path(sf.spath(row))
        target.parent.mkdir(parents=True)
        target.write_text('changed', encoding='utf-8')
        receipt = self.root / 'receipt.json'
        receipt.write_text(json.dumps(dict(source_folder=str(source.resolve()), sources={'old':'hash'}, targets={'ZZ-001':'wrong-digest'})), encoding='utf-8')
        code, _ = self.invoke(sf.cmd_migration_check, ['--removed', str(source), str(receipt)])
        self.assertIn('target changed', str(code))

    def make_batch(self, duplicate=False):
        domain=dict(code='ZZ',name='Test',macro='Writing & Editing',scope='Test only.',subdomains=['Review'])
        row=dict(id='ZZ-001',name='fixture-review',domain_code='ZZ',subdomain='Review',description='Review fixture.',risk_level='low',requires=[],status='planned')
        rows=[row]
        if duplicate:
            rows.append(dict(row,id='ZZ-002'))
        path=self.root/'batch.json'
        path.write_text(json.dumps(dict(domains=[domain],skills=rows)),encoding='utf-8')
        return path

    def test_invalid_batch_leaves_registry_unchanged(self):
        path=self.make_batch(duplicate=True)
        code,_=self.invoke(sf.cmd_ingest,[str(path)])
        self.assertNotEqual(code,0)
        self.assertEqual(Path(sf.DOM).read_text(),'')
        self.assertEqual(Path(sf.REG).read_text(),'')

    def test_ingest_is_idempotent(self):
        path=self.make_batch()
        self.assertEqual(self.invoke(sf.cmd_ingest,[str(path)])[0],0)
        before=Path(sf.REG).read_bytes()
        code,output=self.invoke(sf.cmd_ingest,[str(path)])
        self.assertEqual(code,0)
        self.assertEqual(before,Path(sf.REG).read_bytes())
        self.assertIn('domains=0 skills=0',output)

    def test_missing_prerequisite_rejects_whole_batch(self):
        path=self.make_batch()
        batch=json.loads(path.read_text(encoding='utf-8'))
        batch['skills'][0]['requires']=['ZZ-099']
        path.write_text(json.dumps(batch),encoding='utf-8')
        code,_=self.invoke(sf.cmd_ingest,[str(path)])
        self.assertNotEqual(code,0)
        self.assertEqual(Path(sf.DOM).read_text(),'')
        self.assertEqual(Path(sf.REG).read_text(),'')


if __name__ == '__main__':
    unittest.main()
