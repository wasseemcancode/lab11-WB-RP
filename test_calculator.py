import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
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