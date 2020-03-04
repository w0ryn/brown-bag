from unittest import TestCase
from local_utils import Test
from solution import Solution


class MinimumRequiredTests(TestCase):
    def test_remove_duplicate_words_none_exist(self):
        phrase = 'alpha'
        result = Solution.remove_duplicate_words(phrase)
        self.assertEqual('alpha', result)

    def test_remove_duplicate_words_one_duplicate(self):
        phrase = 'alpha beta alpha'
        result = Solution.remove_duplicate_words(phrase)
        self.assertEqual('alpha beta', result)

    def test_remove_duplicate_words_multiple_duplicates(self):
        phrase = 'alpha beta alpha alpha beta delta alpha'
        result = Solution.remove_duplicate_words(phrase)
        self.assertEqual('alpha beta delta', result)

if __name__ == '__main__':
    Test.run_suite(
        test_suite=MinimumRequiredTests,
    )
