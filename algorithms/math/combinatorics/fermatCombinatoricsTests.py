from fermatCombinatorics import fermat_array, fermat_comb
import unittest

class fermat_array_test(unittest.TestCase):

    def test_dummy(self):
        self.assertEqual(1,1)

    def test_basic(self):
        r = 100000007
        facts,invs = fermat_array(100,100,r)
        n = 10
        k = 0
        self.assertEqual(fermat_comb(n,k,r,facts,invs),1)













if __name__ == "__main__":
    unittest.main()
