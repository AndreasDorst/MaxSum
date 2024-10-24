import unittest
from unittest.mock import patch
from max_sum_digits import sum_of_digits, get_numbers

class TestMaxSumOfDigits(unittest.TestCase):

    def test_sum_of_digits_positive(self):
        self.assertEqual(sum_of_digits(1234), 10)  # 1+2+3+4 = 10

    def test_sum_of_digits_negative(self):
        self.assertEqual(sum_of_digits(-567), 18)  # 5+6+7 = 18

    def test_sum_of_digits_zero(self):
        self.assertEqual(sum_of_digits(0), 0)  # Sum of digits of 0 is 0

    def test_get_numbers_single_input(self):
        inputs = iter(['123', '0'])
        numbers_with_max_sum, max_sum = get_numbers(input_func=lambda _: next(inputs))
        self.assertEqual(numbers_with_max_sum, [123])
        self.assertEqual(max_sum, 6)  # 1+2+3 = 6

    def test_get_numbers_multiple_inputs(self):
        inputs = iter(['123', '456', '789', '0'])
        numbers_with_max_sum, max_sum = get_numbers(input_func=lambda _: next(inputs))
        self.assertEqual(numbers_with_max_sum, [789])  # 7+8+9 = 24
        self.assertEqual(max_sum, 24)

    def test_get_numbers_equal_sum(self):
        inputs = iter(['322', '233', '323', '0'])
        numbers_with_max_sum, max_sum = get_numbers(input_func=lambda _: next(inputs))
        self.assertEqual(numbers_with_max_sum, [233, 323])  # All have sum = 8
        self.assertEqual(max_sum, 8)

    @patch('max_sum_digits.animated_print')
    def test_get_numbers_invalid_input(self, mock_print):
        inputs = iter(['abc', '123', '0'])  # First input is invalid
        numbers_with_max_sum, max_sum = get_numbers(input_func=lambda _: next(inputs))
        self.assertEqual(numbers_with_max_sum, [123])
        self.assertEqual(max_sum, 6)  # 1+2+3 = 6

    @patch('max_sum_digits.animated_print')
    def test_get_numbers_max_input(self, mock_print):
        inputs = iter(['123', '456', '789', '0'])
        numbers_with_max_sum, max_sum = get_numbers(max_numbers=2, input_func=lambda _: next(inputs))
        self.assertEqual(numbers_with_max_sum, [456])  # 4+5+6 = 15 is the highest in the first 2 inputs
        self.assertEqual(max_sum, 15)

if __name__ == "__main__":
    unittest.main()
