import re


class Solution():
    @staticmethod
    def dictionary_replacer(phrase, dictionary):
        replace_me = re.compile('(<([^>]*)>)')

        for match in replace_me.findall(phrase):
            if match[1] in dictionary:
                phrase = re.compile(match[0]).sub(dictionary[match[1]], phrase)

        return phrase
