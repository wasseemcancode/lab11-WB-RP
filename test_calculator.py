# https://github.com/wasseemcancode/lab11-WB-RP
# Partner 1: Wasseem Barghouthi
# Partner 2: Roman Perez

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
     def test_log_invalid_argument(self):
        # log(0) is undefined
        with self.assertRaises(ValueError):
            log(0, 5)

        # negative argument
        with self.assertRaises(ValueError):
            log(-10, 2)

        # invalid base (base <= 0 or base == 1)
        with self.assertRaises(ValueError):
            log(10, 1)

     def test_hypotenuse(self):
        # right triangle classic
        self.assertEqual(hypotenuse(3, 4), 5)

        # floating point
        self.assertAlmostEqual(hypotenuse(6.0, 8.0), 10.0)

        # invalid: negative side
        with self.assertRaises(ValueError):
            hypotenuse(-5, 12)

     def test_sqrt(self):
        # invalid argument: negative number
        with self.assertRaises(ValueError):
            square_root(-16)

        # perfect square
        self.assertEqual(square_root(81), 9)

        # non-perfect square
        self.assertAlmostEqual(square_root(3), 3**0.5)
    def test_add(self):
        self.assertEqual(add(4, 5), 9)
        self.assertEqual(add(-2, 4), 2)
        self.assertEqual(add(-2, -4), -6)

    def test_divide_by_zero(self): 
        with self.assertRaises(ZeroDivisionError):
            div(0, 3)
        
    def test_logarithm(self): 
        self.assertAlmostEqual(log(100, 10), 2)
        self.assertAlmostEqual(log(27, 3), 3)
        self.assertAlmostEqual(log(49, 7), 2)
        
    def test_log_invalid_base(self): 
        with self.assertRaises(ValueError):
            log(5, 0)

  

# Do not touch this
if __name__ == "__main__":
    unittest.main()