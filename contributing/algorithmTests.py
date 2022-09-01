import unittest
from algorithm import * #change to filename


class algorithm_test(unittest.TestCase):

    def test_a(self): #insert test here
        print("test a")
        self.assertEqual(1,1)

    def test_b(self): #insert test here
        print("test b")
        self.assertEqual(1,1)


if __name__ == "__main__":
    unittest.main()
