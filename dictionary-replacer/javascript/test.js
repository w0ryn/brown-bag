const Utils = require('./local_utils.js').utils;
const Solution = require('./solution.js').solution;

// assertion facility
const assertEqual  = Utils.test.assertEqual;
const assertTrue   = Utils.test.assertTrue;
const assertFalse  = Utils.test.assertFalse;
const assertTruthy = Utils.test.assertTruthy;
const assertFalsey = Utils.test.assertFalsey;


Utils.test.runSuite(
  'MinimumRequiredTests', [
    function dictReplacerEmptyPhrase() {
      const phrase = '';
      const dictionary = {};

      result = Solution.dictionaryReplacer(phrase, dictionary);

      assertEqual(result, '');
    },

    function dictReplacerNoReplacements() {
      const phrase = 'There are no replacements to be made here';
      const dictionary = {};

      result = Solution.dictionaryReplacer(phrase, dictionary);

      assertEqual(result, phrase);
    },

    function dictReplacerSingleItemPhrase() {
      const phrase = '<a>';
      const dictionary = {
        a: 'successful',
      };

      result = Solution.dictionaryReplacer(phrase, dictionary);

      assertEqual(result, 'successful');
    },

    function test_dictReplacerTwoItemsPhrase() {
      const phrase = 'I think <1> lives in <2>.';
      const dictionary = {
        '1': 'Nate',
        '2': 'Idaho',
      };

      result = Solution.dictionaryReplacer(phrase, dictionary);

      assertEqual(result, 'I think Nate lives in Idaho.');
    },

    function test_dictReplacerTwoIdenticalItems() {
      const phrase = 'I want to see my friend <friendName>. <friendName> lives in <state>.'
      const dictionary = {
        friendName: 'Colton',
        state: 'Utah',
      }

      result = Solution.dictionaryReplacer(phrase, dictionary);

      assertEqual(result, 'I want to see my friend Colton. Colton lives in Utah.');
    }
  ],

  'BonusTests', [
    function dictReplacerUnknownValue() {
      const phrase = '<a>, <b>'
      const dictionary = {
        'b': 'non-null',
      }

      result = Solution.dictionaryReplacer(phrase, dictionary);

      assertEqual(result, '<a>, non-null')
    },
  ],
);
