from Queue import queue
from random import randint
import unittest


class queue_test(unittest.TestCase):

    def test_basic(self):
        x = queue() #create new queue
        x.add(1)
        x.add(2)
        x.add(3)
        #queue is now [1,2,3]
        self.assertEqual(x.dequeue(),1) #should be 1
        self.assertEqual(x.top(),2) #should be 2
        x.add(5)
        x.add(4)
        #queue is now [2,3,5,4]
        self.assertEqual(x.dequeue(),2) #should be 2
        self.assertEqual(x.dequeue(),3) #should be 3

    def test_speed(self): #efficiency test, should be done in 1 second tops
        x = queue()
        num = 500000
        for i in range(num):
            x.add(randint(1,1000000000))
        for _ in range(num):
            x.dequeue()
        self.assertEqual(x.dequeue(),None) 
        
        
if __name__ == "__main__":
    unittest.main()
