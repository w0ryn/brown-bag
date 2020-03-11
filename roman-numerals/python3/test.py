from unittest import TestCase
from utils import Test
from solution import Solution


class MinimumRequiredTests(TestCase):
    def test_convert_integer_to_roman_numeral_one(self):
        roman_numeral = Solution.convert_integer_to_roman_numeral(1)
        self.assertEqual(roman_numeral, 'I')

    def test_convert_integer_to_roman_numeral_three(self):
        roman_numeral = Solution.convert_integer_to_roman_numeral(3)
        self.assertEqual(roman_numeral, 'III')

    def test_convert_integer_to_roman_numeral_four(self):
        roman_numeral = Solution.convert_integer_to_roman_numeral(4)
        self.assertEqual(roman_numeral, 'IV')

    def test_convert_integer_to_roman_numeral_five(self):
        roman_numeral = Solution.convert_integer_to_roman_numeral(5)
        self.assertEqual(roman_numeral, 'V')

    def test_convert_integer_to_roman_numeral_six(self):
        roman_numeral = Solution.convert_integer_to_roman_numeral(6)
        self.assertEqual(roman_numeral, 'VI')

    def test_convert_integer_to_roman_numeral_nine(self):
        roman_numeral = Solution.convert_integer_to_roman_numeral(9)
        self.assertEqual(roman_numeral, 'IX')

    def test_convert_integer_to_roman_numeral_ten(self):
        roman_numeral = Solution.convert_integer_to_roman_numeral(10)
        self.assertEqual(roman_numeral, 'X')


class BonusTests(TestCase):
    def test_convert_roman_numeral_one(self):
        converted_integer = Solution.convert_roman_numeral_to_integer('I')
        self.assertEqual(converted_integer, 1)

    def test_convert_roman_numeral_three(self):
        converted_integer = Solution.convert_roman_numeral_to_integer('III')
        self.assertEqual(converted_integer, 3)

    def test_convert_roman_numeral_four(self):
        converted_integer = Solution.convert_roman_numeral_to_integer('IV')
        self.assertEqual(converted_integer, 4)

    def test_convert_roman_numeral_five(self):
        converted_integer = Solution.convert_roman_numeral_to_integer('V')
        self.assertEqual(converted_integer, 5)

    def test_convert_roman_numeral_six(self):
        converted_integer = Solution.convert_roman_numeral_to_integer('VI')
        self.assertEqual(converted_integer, 6)

    def test_convert_roman_numeral_nine(self):
        converted_integer = Solution.convert_roman_numeral_to_integer('IX')
        self.assertEqual(converted_integer, 9)

    def test_convert_roman_numeral_ten(self):
        converted_integer = Solution.convert_roman_numeral_to_integer('X')
        self.assertEqual(converted_integer, 10)


if __name__ == '__main__':
    Test.run_suite(
        test_suite=MinimumRequiredTests,
        bonus_suite=BonusTests,
    )
