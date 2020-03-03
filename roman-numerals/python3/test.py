from unittest import TestCase
from local_utils import Test
from solution import Solution


class MinimumRequiredTests(TestCase):
    def test_convert_integer_to_roman_numeral_one(self):
        roman_numeral = Solution.convert_integer_to_roman_numeral(1)
        self.assertEqual('I', roman_numeral)

    def test_convert_integer_to_roman_numeral_three(self):
        roman_numeral = Solution.convert_integer_to_roman_numeral(3)
        self.assertEqual('III', roman_numeral)

    def test_convert_integer_to_roman_numeral_four(self):
        roman_numeral = Solution.convert_integer_to_roman_numeral(4)
        self.assertEqual('IV', roman_numeral)

    def test_convert_integer_to_roman_numeral_five(self):
        roman_numeral = Solution.convert_integer_to_roman_numeral(5)
        self.assertEqual('V', roman_numeral)

    def test_convert_integer_to_roman_numeral_six(self):
        roman_numeral = Solution.convert_integer_to_roman_numeral(6)
        self.assertEqual('VI', roman_numeral)

    def test_convert_integer_to_roman_numeral_nine(self):
        roman_numeral = Solution.convert_integer_to_roman_numeral(9)
        self.assertEqual('IX', roman_numeral)

    def test_convert_integer_to_roman_numeral_ten(self):
        roman_numeral = Solution.convert_integer_to_roman_numeral(10)
        self.assertEqual('X', roman_numeral)


class BonusTests(TestCase):
    def test_convert_roman_numeral_one(self):
        roman_numeral = Solution.convert_roman_numeral_to_integer('I')
        self.assertEqual(1, roman_numeral)

    def test_convert_roman_numeral_three(self):
        roman_numeral = Solution.convert_roman_numeral_to_integer('III')
        self.assertEqual(3, roman_numeral)

    def test_convert_roman_numeral_four(self):
        roman_numeral = Solution.convert_roman_numeral_to_integer('IV')
        self.assertEqual(4, roman_numeral)

    def test_convert_roman_numeral_five(self):
        roman_numeral = Solution.convert_roman_numeral_to_integer('V')
        self.assertEqual(5, roman_numeral)

    def test_convert_roman_numeral_six(self):
        roman_numeral = Solution.convert_roman_numeral_to_integer('VI')
        self.assertEqual(6, roman_numeral)

    def test_convert_roman_numeral_nine(self):
        roman_numeral = Solution.convert_roman_numeral_to_integer('IX')
        self.assertEqual(9, roman_numeral)

    def test_convert_roman_numeral_ten(self):
        roman_numeral = Solution.convert_roman_numeral_to_integer('X')
        self.assertEqual(10, roman_numeral)


if __name__ == '__main__':
    Test.run_suite(
        test_suite=MinimumRequiredTests,
        bonus_suite=BonusTests,
    )
