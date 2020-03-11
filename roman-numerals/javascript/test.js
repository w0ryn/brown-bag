const Utils = require('./utils.js').utils;
const Solution = require('./solution.js').solution;

// assertion facility
const assertEqual  = Utils.test.assertEqual;
const assertTrue   = Utils.test.assertTrue;
const assertFalse  = Utils.test.assertFalse;
const assertTruthy = Utils.test.assertTruthy;
const assertFalsey = Utils.test.assertFalsey;


Utils.test.runSuite(
  'Roman Numeral Converter Minimum Required Tests', [
    function testConvertIntegerToRomanNumeralOne() {
      const romanNumeral = Solution.convertIntegerToRomanNumeral(1)
      assertEqual(romanNumeral, 'I')
    },

    function testConvertIntegerToRomanNumeralThree() {
      const romanNumeral = Solution.convertIntegerToRomanNumeral(3)
      assertEqual(romanNumeral, 'III')
    },

    function testConvertIntegerToRomanNumeralFour() {
      const romanNumeral = Solution.convertIntegerToRomanNumeral(4)
      assertEqual(romanNumeral, 'IV')
    },

    function testConvertIntegerToRomanNumeralFive() {
      const romanNumeral = Solution.convertIntegerToRomanNumeral(5)
      assertEqual(romanNumeral, 'V')
    },

    function testConvertIntegerToRomanNumeralSix() {
      const romanNumeral = Solution.convertIntegerToRomanNumeral(6)
      assertEqual(romanNumeral, 'VI')
    },

    function testConvertIntegerToRomanNumeralNine() {
      const romanNumeral = Solution.convertIntegerToRomanNumeral(9)
      assertEqual(romanNumeral, 'IX')
    },

    function testConvertIntegerToRomanNumeralTen() {
      const romanNumeral = Solution.convertIntegerToRomanNumeral(10)
      assertEqual(romanNumeral, 'X')
    },
  ],

  'Roman Numeral Converter Bonus Tests', [
    function testConvertRomanNumeralOne() {
      const convertedInteger = Solution.convertRomanNumeralToInteger('I')
      assertEqual(1, convertedInteger)
    },

    function testConvertRomanNumeralThree() {
      const convertedInteger = Solution.convertRomanNumeralToInteger('III')
      assertEqual(3, convertedInteger)
    },

    function testConvertRomanNumeralFour() {
      const convertedInteger = Solution.convertRomanNumeralToInteger('IV')
      assertEqual(4, convertedInteger)
    },

    function testConvertRomanNumeralFive() {
      const convertedInteger = Solution.convertRomanNumeralToInteger('V')
      assertEqual(5, convertedInteger)
    },

    function testConvertRomanNumeralSix() {
      const convertedInteger = Solution.convertRomanNumeralToInteger('VI')
      assertEqual(6, convertedInteger)
    },

    function testConvertRomanNumeralNine() {
      const convertedInteger = Solution.convertRomanNumeralToInteger('IX')
      assertEqual(9, convertedInteger)
    },

    function testConvertRomanNumeralTen() {
      const convertedInteger = Solution.convertRomanNumeralToInteger('X')
      assertEqual(10, convertedInteger)
    },
  ],
);
