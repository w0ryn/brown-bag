from collections import OrderedDict, MutableSet


class OrderedSet(OrderedDict, MutableSet):
    # @TODO : implement all the set functions __le__, __lt__, add, discard, etc.
    def __init__(self, *args):
        for arg in args:
            for element in arg:
                self[element] = None


class DuplicateRemover(OrderedSet):
    def __str__(self):
        return ' '.join(self.keys())
