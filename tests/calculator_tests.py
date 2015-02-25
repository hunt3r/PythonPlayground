
import unittest
from calculator import Calculator

class CalculatorTests(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        #Ensure we start at
        self.assertEqual(self.calculator.value(), 0.0)

        #Assert we can add a positive integer value
        self.calculator.add(3)
        self.calculator.add(3)
        self.assertEqual(self.calculator.value(), 6.0)
        self.assertIsInstance(self.calculator.value(), float)

    def test_add_negative(self):
        #Assert we can add a negative
        self.calculator.clear()
        self.calculator.add(-4)
        self.assertEqual(self.calculator.value(), -4.0)
        self.assertIsInstance(self.calculator.value(), float)

    def test_clear(self):
        #Assert we can clear the value
        self.assertEqual(self.calculator.value(), 0.0)
        self.calculator.add(3)
        self.assertEqual(self.calculator.value(), 3)
        self.calculator.clear()
        self.assertEqual(self.calculator.value(), 0.0)
        self.assertIsInstance(self.calculator.value(), float)

    def test_subtract_positive(self):
        self.calculator.add(3)
        self.calculator.subtract(1)
        self.assertEqual(self.calculator.value(), 2.0)
        self.assertIsInstance(self.calculator.value(), float)
        self.calculator.clear()

        self.calculator.add(-3)
        self.calculator.subtract(1)
        self.assertEqual(self.calculator.value(), -4.0)
        self.assertIsInstance(self.calculator.value(), float)


    def test_subtract_negative(self):
        self.calculator.add(3)
        self.calculator.subtract(-1)
        self.assertEqual(self.calculator.value(), 4.0)
        self.assertIsInstance(self.calculator.value(), float)
        self.calculator.clear()

        self.calculator.add(-3)
        self.calculator.subtract(-1)
        self.assertEqual(self.calculator.value(), -2.0)
        self.assertIsInstance(self.calculator.value(), float)


    def test_multiply_positive(self):
        pass

    def test_multiply_negative(self):
        pass

    def test_divide_positive(self):
        pass

    def test_divide_negative(self):
        pass



