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
    function removeDuplicateWordsNonExist() {
      const phrase = 'alpha';

      const result = Solution.removeDuplicateWords(phrase);

      assertEqual(result, 'alpha');
    },

    function removeDuplicateWordsSingleDuplicate() {
      const phrase = 'alpha beta alpha';

      const result = Solution.removeDuplicateWords(phrase);

      assertEqual(result, 'alpha beta');
    },

    function removeDuplicateWordsMultipleDuplicates() {
      const phrase = 'alpha beta alpha alpha beta delta alpha';

      const result = Solution.removeDuplicateWords(phrase);

      assertEqual(result, 'alpha beta delta');
    },
  ],
);
