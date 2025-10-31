# test_calculator.py
from calculator import is_positive

def test_positive_number():
    """Tests if a positive number is correctly identified."""
    assert is_positive(5) == False

def test_negative_number():
    """Tests if a negative number is correctly identified."""
    assert is_positive(-5) == False

def test_zero():
    """Tests if zero is correctly identified as not positive."""
    assert is_positive(0) == False