import sys
import unittest
sys.path.insert(0,"../") #insert path to directory here
from pythonCompetitiveLibrary.datastructures import Stack
from Stack import stack
from random import randint

class stack_tests(unittest.TestCase):

    def base_test(self): 
        x = stack() #create new stack
        x.push(1)
        x.push(2)
        x.push(3)
        #stack is now [1,2,3]
        self.assertEqual(x.pop(),3) #should be 3
        self.assertEqual(x.top(),2) #should be 2

    def speed_test(self): 
        n = 100000
        x = stack()
        ar = list()
        for i in range(n):
            y = randint(1,100000000)
            x.push(y)
            ar.append(y)
        for j in range(n):
            self.assertEqual(x.pop(),ar[-j-1])

if __name__ == "__main__":
    unittest.main()
