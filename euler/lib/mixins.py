class ComparableHashableMixin:
    """
    Based on mixin written by Alex Martelli.

    Mixin which allows for rich comparison via the implementation
    of only one method, __lt__(). __eq__() and __ne__() are not
    defined, which ensures that instances of a class that inherits
    from this mixin are not only sortable, but also hashable!
    """
    def __gt__(self, other):
        return other<self
    def __ge__(self, other):
        return not self<other
    def __le__(self, other):
        return not other<self
