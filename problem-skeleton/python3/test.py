from unittest import TestCase
from local_utils import Test
from solution import Solution


class MinimumRequiredTests(TestCase):
    pass


class BonusTests(TestCase):
    pass


if __name__ == '__main__':
    Test.run_suite(
        test_suite=MinimumRequiredTests,
        bonus_suite=BonusTests,
    )
