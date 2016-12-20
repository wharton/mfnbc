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

    L_HOOD_FILE = 'sample_files/likeli_sample.csv'
    UNLABELED_FILE = 'sample_files/likeli_sample.csv'

    def test_print_probs(self):
        m = MFNBC(self.L_HOOD_FILE, self.UNLABELED_FILE, False)
        self.assertNotEqual(m.print_probs(), '')

    def test_read_likelihoods(self):
        d = MFNBC(self.L_HOOD_FILE, self.UNLABELED_FILE, False)
        d._read_likelihoods()
        self.assertEqual(PROBS, PROBS)

    def test_calc_denuminator(self):
        m = MFNBC(self.L_HOOD_FILE, self.UNLABELED_FILE, False)
        m._read_likelihoods()
        den = m._calc_denuminator(m.posteriors, m.probs['cat'], m.features)
        self.assertEqual(den, 0.13666666666666666)


if __name__ == '__main__':
    unittest.main()
