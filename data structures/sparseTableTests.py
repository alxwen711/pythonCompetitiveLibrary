import sys
import unittest
from sparseTable import * #change to filename
from random import randint

class sparse_test(unittest.TestCase):

    def test_normal(self):
        x = [7,8,7,0,9,8,6,4,3,1,9,2,0,0,89,2]
        a = create_sparse(x)
        #print(a), contains sparse table
        for i in range(len(x)):
            for j in range(i,len(x)):
                #print(i,j,query(i,j,a)) for validation
                assert query(i,j,a) == min(x[i:j+1])
    
    def test_speed(self):
        #table creation time is O(n log n), should take just under 1 second
        n = 100000
        ar = [0]*n
        for i in range(n):
            ar[i] = i
        t = create_sparse(ar) #table
        for j in range(n):
            a,b = randint(0,n-1),randint(0,n-1)
            assert query(min(a,b),max(a,b),t) == min(a,b)

    def test_single(self):
        n = 1000
        ar = [0]*n
        for i in range(n):
            ar[i] = randint(0,1000000000)
        t = create_sparse(ar) #table
        for j in range(n):
            assert query(j,j,t) == ar[j]

if __name__ == "__main__":
    unittest.main()
