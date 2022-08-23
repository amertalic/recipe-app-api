"""
Sample tests.
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """
    Test the cval module.
    """

    def test_add_numbers(self):
        """
        Test adding numbers together.
        :return: int
        """
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """
        Test subtracts numbers.
        :return: int
        """
        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)
