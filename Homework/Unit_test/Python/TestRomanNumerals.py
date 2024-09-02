import unittest
from RomanNumerals import RomanNumerals

class TestRomanNumerals(unittest.TestCase):

    def setUp(self):
        self.roman = RomanNumerals()

    def test_roman_to_decimal(self):
        self.assertEqual(self.roman.roman_to_decimal('I'), 1)
        self.assertEqual(self.roman.roman_to_decimal('V'), 5)
        self.assertEqual(self.roman.roman_to_decimal('X'), 10)
        self.assertEqual(self.roman.roman_to_decimal('L'), 50)
        self.assertEqual(self.roman.roman_to_decimal('C'), 100)
        self.assertEqual(self.roman.roman_to_decimal('D'), 500)
        self.assertEqual(self.roman.roman_to_decimal('M'), 1000)
        self.assertEqual(self.roman.roman_to_decimal('II'), 2)
        self.assertEqual(self.roman.roman_to_decimal('III'), 3)
        self.assertEqual(self.roman.roman_to_decimal('IV'), 4)
        self.assertEqual(self.roman.roman_to_decimal('VI'), 6)
    if __name__ == '__main__':
        unittest.main()