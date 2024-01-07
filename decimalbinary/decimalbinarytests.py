import unittest
from decimalbinary import decimaltobinary, binarytodecimal

class TestDecimalBinary(unittest.TestCase):
    def test_decimaltobinary(self):
        self.assertEqual(decimaltobinary(10), '1010')
        self.assertEqual(decimaltobinary(18), '10010')
        self.assertEqual(decimaltobinary(7), '111')

    def test_binarytodecimal(self):
        self.assertEqual(binarytodecimal('1010'), 10)
        self.assertEqual(binarytodecimal('10010'), 18)
        self.assertEqual(binarytodecimal('111'), 7)

if __name__ == '__main__':
    unittest.main()