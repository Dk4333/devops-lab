import unittest
from calculator import is_positive

class TestCalculator(unittest.TestCase):

    def test_positive_number(self):
        """Tests if a positive number is correctly identified."""
        self.assertTrue(is_positive(5))

    def test_negative_number(self):
        """Tests if a negative number is correctly identified."""
        self.assertFalse(is_positive(-5))

    def test_zero(self):
        """Tests if zero is correctly identified as not positive."""
        self.assertFalse(is_positive(0))

    def test_positive_float(self):
        """Tests if a small positive float is correctly identified."""
        self.assertTrue(is_positive(0.1))

    def test_negative_float(self):
        """Tests if a small negative float is correctly identified."""
        self.assertFalse(is_positive(-0.0001))

if __name__ == "__main__":
    unittest.main()
