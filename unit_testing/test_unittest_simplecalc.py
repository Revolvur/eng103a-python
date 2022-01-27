from unit_testing.simplecalc import SimpleCalc
import unittest  # core python test module

# Define a Class that inherits from TestCase

class CalcTests(unittest.TestCase):

    calc = SimpleCalc()

    def test_add(self):
        actual = self.calc.add(2, 4)
        expected = 6
        self.assertEqual(actual, expected)

    def test_subtract(self):
        actual = self.calc.subtract(4, 2)
        expected = 2
        self.assertEqual(actual, expected)

    # def test_multiply(self):
    #     actual = self.calc.multiply(4, 3)
    #     expected = 12
    #     self.assertEqual(actual, expected)

    def test_multiply(self):
        actual = self.calc.multiply(0.4, -80.9)
        expected = -32.36
        self.assertAlmostEqual(actual, expected)

    def test_divide(self):
        actual = self.calc.divide(20, 5)
        expected = 4
        self.assertEqual(actual, expected)
