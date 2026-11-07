"""Net expansion must not hide retirements or count renamed baseline entries."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from sf import expansion_counts


def row(sid, name, status='validated'):
    return dict(id=sid, name=name, status=status)


class ExpansionAccounting(unittest.TestCase):
    def test_retirement_offsets_new_entry(self):
        baseline = [row('A-001', 'first'), row('A-002', 'second')]
        current = [baseline[0], row('B-001', 'new')]
        counts = expansion_counts(baseline, current, lambda r: True, 5)
        self.assertEqual(counts['net_additions'], 0)
        self.assertEqual(counts['remaining'], 5)

    def test_unready_and_missing_do_not_count(self):
        baseline = [row('A-001', 'first')]
        current = baseline + [row('B-001', 'draft', 'planned'), row('B-002', 'missing')]
        counts = expansion_counts(baseline, current, lambda r: r['id'] != 'B-002', 5)
        self.assertEqual(counts['new_ready'], 0)

    def test_renamed_identity_is_not_addition(self):
        baseline = [row('A-001', 'first')]
        current = [row('A-001', 'renamed'), row('B-001', 'first')]
        counts = expansion_counts(baseline, current, lambda r: True, 5)
        self.assertEqual(counts['new_ready'], 0)
        self.assertEqual(counts['missing_or_changed'], 1)
        self.assertEqual(counts['net_additions'], -1)

    def test_normal_addition(self):
        baseline = [row('A-001', 'first')]
        counts = expansion_counts(baseline, baseline + [row('B-001', 'second')], lambda r: True, 5)
        self.assertEqual(counts['net_additions'], 1)
        self.assertEqual(counts['remaining'], 4)


if __name__ == '__main__':
    unittest.main()
