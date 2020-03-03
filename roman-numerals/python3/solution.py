from roman_numeral_converter import RomanNumeralConverter


class Solution():
    @staticmethod
    def convert_integer_to_roman_numeral(integer):
        rnc = RomanNumeralConverter()
        roman_numeral = rnc.convertIntegerToRomanNumeral(integer)
        return roman_numeral

    @staticmethod
    def convert_roman_numeral_to_integer(roman_numeral):
        rnc = RomanNumeralConverter()
        integer = rnc.convertRomanNumeralToInteger(roman_numeral)
        return integer
