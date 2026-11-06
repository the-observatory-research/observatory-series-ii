"""New repository regression tests derived from documented formatting requirements.
These are NOT asserted to be the original historical unit-test file.
"""
import unittest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from arm_b_normalizer import normalize

class NormalizationRegressionTests(unittest.TestCase):
    def test_line_endings(self):
        self.assertEqual(normalize('A\r\nB\rC'), 'A\nB\nC')

    def test_nfc(self):
        self.assertEqual(normalize('Cafe\u0301'), 'Caf\u00e9')

    def test_trailing_whitespace(self):
        self.assertEqual(normalize('A  \nB\t'), 'A\nB')

    def test_blank_lines(self):
        self.assertEqual(normalize('A\n\n\n\nB'), 'A\n\n\nB')

    def test_two_blank_lines_unchanged(self):
        self.assertEqual(normalize('A\n\n\nB'), 'A\n\n\nB')

    def test_preserve_indentation(self):
        self.assertEqual(normalize('  A\n\t B'), '  A\n\t B')

    def test_relational_tokens_unchanged(self):
        s='A \u2192 B; B cannot transition directly to E; a valid route cannot repeat any node.'
        self.assertEqual(normalize(s), s)

    def test_idempotence(self):
        s='\nA  \r\n\r\n\r\n\r\nB\t\n'
        self.assertEqual(normalize(normalize(s)), normalize(s))

if __name__=='__main__': unittest.main()
