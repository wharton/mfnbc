import unittest
from mfnbc import MFNBC

PROBS = {
    'women': {'Plant': '0.05', 'Animal': '0.12', 'Word': 'women', 'Human': '0.45'},
    'man': {'Plant': '0.05', 'Animal': '0.12', 'Word': 'man', 'Human': '0.45'},
    'dog': {'Plant': '0.05', 'Animal': '0.33', 'Word': 'dog', 'Human': '0.02'},
    'cat': {'Plant': '0.05', 'Animal': '0.33', 'Word': 'cat', 'Human': '0.03'},
    'tree': {'Plant': '0.4', 'Animal': '0.05', 'Word': 'tree', 'Human': '0.02'},
    'leaves': {'Plant': '0.4', 'Animal': '0.05', 'Word': 'leaves', 'Human': '0.03'}}


class TestMFNBC(unittest.TestCase):

    def test_print_probs(self):
        m = MFNBC('sample_files/likeli_sample.csv', 'sample_files/input_sample.csv', False)
        self.assertNotEqual(m.print_probs(), '')

    def test_read_likelihoods(self):
        d = MFNBC('sample_files/likeli_sample.csv', 'sample_files/input_sample.csv', False)
        d._read_likelihoods()
        self.assertEqual(PROBS, PROBS)

    def test_calc_denuminator(self):
        m = MFNBC('sample_files/likeli_sample.csv', 'sample_files/input_sample.csv', False)
        m._read_likelihoods()
        den = m._calc_denuminator(m.posteriors, m.probs['cat'], m.features)
        self.assertEqual(den, 0.13666666666666666)


if __name__ == '__main__':
    unittest.main()
