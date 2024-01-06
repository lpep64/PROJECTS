import unittest
from palindrome import is_palindrome

class PalindromeTests(unittest.TestCase):
    def test_palindrome_true(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("Racecar"))
        self.assertTrue(is_palindrome("@#3#3#@"))
        
    def test_palindrome_false(self):
        self.assertFalse(is_palindrome("Luke Pepin"))
        self.assertFalse(is_palindrome("Test123"))
        self.assertFalse(is_palindrome("&@D&#*#D&*@DN"))
        
if __name__ == "__main__":
    unittest.main()
