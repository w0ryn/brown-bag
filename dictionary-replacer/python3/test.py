from unittest import TestCase
from utils import Test
from solution import Solution


class MinimumRequiredTests(TestCase):
    def test_dict_replacer_empty_phrase(self):
        phrase = ''
        dictionary = {}
        result = Solution.dictionary_replacer(phrase, dictionary)
        self.assertEqual(result, '')

    def test_dict_replacer_no_replacements(self):
        phrase = 'There are no replacements to be made here.'
        dictionary = {}
        result = Solution.dictionary_replacer(phrase, dictionary)
        self.assertEqual(result, phrase)

    def test_dict_replacer_one_item_phrase(self):
        phrase = '<a>'
        dictionary = {
            'a': 'successful',
        }
        result = Solution.dictionary_replacer(phrase, dictionary)
        self.assertEqual(result, 'successful')

    def test_dict_replacer_two_items_phrase(self):
        phrase = 'I think <1> lives in <2>.'
        dictionary = {
            '1': 'Nate',
            '2': 'Idaho',
        }
        result = Solution.dictionary_replacer(phrase, dictionary)
        self.assertEqual(result, 'I think Nate lives in Idaho.')

    def test_dict_replacer_two_identical_items_phrase(self):
        phrase = 'I want to see my friend <friend_name>. <friend_name> lives in <state>.'
        dictionary = {
            'friend_name': 'Colton',
            'state': 'Utah',
        }
        result = Solution.dictionary_replacer(phrase, dictionary)
        self.assertEqual(result, 'I want to see my friend Colton. Colton lives in Utah.')


class BonusTests(TestCase):
    def test_dict_replacer_unknown_value(self):
        phrase = '<a>, <b>'
        dictionary = {
            'b': 'non-null',
        }
        result = Solution.dictionary_replacer(phrase, dictionary)
        self.assertEqual(result, '<a>, non-null')


if __name__ == '__main__':
    Test.run_suite(
        test_suite=MinimumRequiredTests,
        bonus_suite=BonusTests,
    )
