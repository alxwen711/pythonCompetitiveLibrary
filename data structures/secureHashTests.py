import unittest
from secureHash import * 

#create breaker here
ar = list()
ar.append(2**17+1)
ar.append(2**17+1)
mask = 2**17 - 1
x = 6
for i in range(99999):
    ar.append(x)
    ar.append(x)
    x = (x * 5 + 1) & mask
print(ar[:10])

#@unittest.skip("activate if testing standard dict")
class secure_test(unittest.TestCase):
    #@unittest.skip("testing adverse only")
    def test_million(self): #speed test with 1000000 elements
        d = hashmap()
        n = 1000000
        for i in range(n):
            assert d.inc(i,1) == 1 #no individual value should map to same key and dict

    def test_adverse(self): #100000 num sequence meant to cause collisions
        d = hashmap()
        for i in range(200000):
            assert d.inc(ar[i],1) <= 2

     
#@unittest.skip("activate if testing secure dict")
class normal_test(unittest.TestCase):
    #@unittest.skip("testing adverse only")
    def test_million(self): #speed test with 1000000 elements
        d = {}
        n = 1000000
        for i in range(n):
            d.get(i)
            d[i] = 1 #already assumed to be valid
    
    def test_adverse(self): #100000 num sequence meant to cause collisions
        d = {}
        for i in range(200000):
            d.get(i)
            d[i] = 1
if __name__ == "__main__":
    unittest.main()
