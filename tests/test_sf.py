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


if __name__ == '__main__':
    unittest.main()
