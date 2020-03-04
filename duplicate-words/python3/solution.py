from duplicate_remover import DuplicateRemover


class Solution():

    @staticmethod
    def remove_duplicate_words(phrase):

        # return ' '.join(set(phrase.split())
        
        # unfortunately, a standard set does not maintain the order of keys entered.
        # python's `collections` library, however has an OrderedDict, which can be used
        # to implement an 'OrderedSet'
        
        return str(DuplicateRemover(phrase.split())) # a standard set does not maintain order
