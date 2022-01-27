from unit_testing.squarerec import Squarerec, Square
import unittest


class Rectest(unittest.TestCase):
    rect = Squarerec(6, 4)

    def test_perimeter(self):
        actual = self.rect.peri()
        expected = 20
        self.assertEqual(actual, expected)

    def test_area(self):
        actual = self.rect.get_area()
        expected = 24
        self.assertEqual(actual, expected)



class Squtest(unittest.TestCase):
    square = Squarerec(6, 6)

    def test_area_sq(self):
        actual = self.square.get_area()
        expected = 36
        self.assertEqual(actual, expected)

    def test_peri_sq(self):
        actual = self.square.peri()
        expected = 24
        self.assertEqual(actual, expected)


    # def test_enclosing(self):
    #     actual = self.square.get_number_enclosing(Square(8))
    #     expected = 1
    #     self.assertEqual(actual, expected)

class Squaretest(unittest.TestCase):

    square2 = Square(10)

    def test_enclosing(self):
        actual = self.square2.get_number_enclosing(1)
        expected = 100
        self.assertEqual(actual, expected)
