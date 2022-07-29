from fermatCombinatorics import *
import unittest

class fermat_array_test(unittest.TestCase):

    def test_basic(self):
        r = 100000007
        facts,invs = fermat_array(100,100,r)
        n = 10
        k = 0
        self.assertEqual(fermat_comb(n,k,r,facts,invs),1)
        self.assertEqual(fermat_comb(5,2,r,facts,invs),10)


    def test_speed(self):
        r = 1000000007
        facts,invs = fermat_array(200000,200000,r)
        self.assertEqual(fermat_comb(5,2,r,facts,invs),10)


class fermat_calc_test(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(fermat_calc(8,6,100000007),28)








if __name__ == "__main__":
    unittest.main()
