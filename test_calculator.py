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

# Do not touch this
if __name__ == "__main__":
    unittest.main()