import unittest

from mymodule import square, double

class TestSquare(unittest.TestCase):
    def test1(self):
        self.assertEqual(square(2), 4) # check square 2 = 4 - true
        self.assertEqual(square(3), 9) # check square 3 = 9 - true
        self.assertEqual(square(4), 16)
        self.assertNotEqual(square(2), 5) # check square 2,  2*2 = 4, so 4 != 5 - not Equal returns true


class TestDouble(unittest.TestCase):
    def test1(self):
        self.assertEqual(double(2), 4) #checking if 2*2 = 4, which is true
        self.assertEqual(double(3), 6)
        self.assertEqual(double(5), 10)
        self.assertNotEqual(double(10), 12) # checking if result(12) is not equal , in this case returns true because 10*2 = 20 and is != 12

unittest.main() #calling the unit test
