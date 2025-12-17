import unittest
from Stack import stack
from random import randint

class stack_test(unittest.TestCase):

    def test_base(self): 
        x = stack() #create new stack
        x.push(1)
        x.push(2)
        x.push(3)
        #stack is now [1,2,3]
        self.assertEqual(x.pop(),3) #should be 3
        self.assertEqual(x.top(),2) #should be 2
        assert x.length() == 2

    def test_speed(self): 
        n = 100000
        x = stack()
        ar = list()
        for i in range(n):
            y = randint(1,100000000)
            x.push(y)
            ar.append(y)
            self.assertEqual(x.length(),i+1)
        for j in range(n):
            self.assertEqual(x.pop(),ar[-j-1])

    def test_empty(self):
        x = stack()
        x.pop()

if __name__ == "__main__":
    unittest.main()
