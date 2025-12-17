import unittest
from statistics import * 
from random import randint
#all methods are already known to be functionally correct

class speed_test(unittest.TestCase):

    def test_speed(self):
        ar = list()
        n = 100000
        for i in range(n):
            ar.append(randint(0,1000000000))
        print("mean:",avg(ar))
        print("median:",median(ar))
        print("mode:",mode(ar))
        print("stddev:",std_dev(ar))

if __name__ == "__main__":
    unittest.main()
