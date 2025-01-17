import unittest
from Calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_sum(self):
        self.assertEqual(self.calc.sum(2, 2), 4)
        self.assertEqual(self.calc.sum(-2, 1), -1)
        self.assertEqual(self.calc.sum(-1, -1), -2)


    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 2), 0)
        self.assertEqual(self.calc.subtract(-2, 1), -3)
        self.assertEqual(self.calc.subtract(-1, -1), 0)


    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)
        self.assertEqual(self.calc.multiply(-2, 1), -2)
        self.assertEqual(self.calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(self.calc.divide(2, 2), 1)
        self.assertEqual(self.calc.divide(-2, 1), -2)
        self.assertEqual(self.calc.divide(-1, -1), 1)
        with self.assertRaises(ValueError): self.calc.divide(2, 0)

if __name__ == '__main__':
   unittest.main()


   #to test both test classes, run the following command in the terminal:
   #pytest TestRomanNumerals.py TestCalculator.py
   #but remember to install pytest first by running the following command:
   #pip install pytest