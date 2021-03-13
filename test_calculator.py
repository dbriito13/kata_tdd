"""
Unit tests for the calculator library
"""
import unittest
import calculator


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

if __name__ == '__main__':
    unittest.main()