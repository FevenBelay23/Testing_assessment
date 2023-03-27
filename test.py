import unittest
from string_functions import *

class TestToUpper(unittest.TestCase):
    # write your code her
     
    def test_toupper(self):
        self.assertEqual(to_upper("hello"), 'HELLO')
    pass

class TestToLower(unittest.TestCase):
   # Write you code here
    def test_tolower(self):
        self.assertEqual(to_lower('HELLO'), 'hello')


class TestCapitalize(unittest.TestCase):
    # Write your code here
    def test_capitalize(self):
        self.assertEqual(capitalize('hello'), 'Hello')

if __name__ == '__main__':
    unittest.main()
