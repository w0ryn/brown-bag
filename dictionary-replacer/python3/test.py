from unittest import TestCase
from local_utils import Test
from solution import Solution


class MinimumRequiredTests(TestCase):
    def test_dict_replacer_no_phrase(self):
        phrase = ''
        dictionary = {}
        result = Solution.dictionary_replacer(phrase, dictionary)
        self.assertEqual('', result)

    def test_dict_replacer_one_item_phrase(self):
        phrase = '<a>'
        dictionary = {
            'a': 'successful',
        }
        result = Solution.dictionary_replacer(phrase, dictionary)
        self.assertEqual('successful', result)

    def test_dict_replacer_two_items_phrase(self):
        phrase = 'I think <1> lives in <2>.'
        dictionary = {
            '1': 'Nate',
            '2': 'Idaho',
        }
        result = Solution.dictionary_replacer(phrase, dictionary)
        self.assertEqual('I think Nate lives in Idaho.', result)


class BonusTests(TestCase):
    def test_dict_replacer_unknown_value(self):
        phrase = '<a>, <b>'
        dictionary = {
            'b': 'non-null',
        }
        result = Solution.dictionary_replacer(phrase, dictionary)
        self.assertEqual('<a>, non-null', result)


if __name__ == '__main__':
    Test.run_suite(
        test_suite=MinimumRequiredTests,
        bonus_suite=BonusTests,
    )
