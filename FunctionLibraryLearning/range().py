class range(object):
    """
    range(stop) -> range object
    range(start, stop[, step]) -> range object

    Return an object that produces a sequence of integers from start (inclusive)
    to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
    start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
    These are exactly the valid indices for a list of 4 elements.
    When step is given, it specifies the increment (or decrement).
    """

    def count(self, value):  # real signature unknown; restored from __doc__
        """ rangeobject.count(value) -> integer -- return number of occurrences of value """
        return 0

    def index(self, value):  # real signature unknown; restored from __doc__
        """
        rangeobject.index(value) -> integer -- return index of value.
        Raise ValueError if the value is not present.
        """
        return 0

    def __bool__(self, *args, **kwargs):  # real signature unknown
        """ self != 0 """
        pass

    def __contains__(self, *args, **kwargs):  # real signature unknown
        """ Return key in self. """
        pass

    def __eq__(self, *args, **kwargs):  # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs):  # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, *args, **kwargs):  # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs):  # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs):  # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs):  # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, stop):  # real signature unknown; restored from __doc__
        pass

    def __iter__(self, *args, **kwargs):  # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs):  # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs):  # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs):  # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod  # known case of __new__
    def __new__(*args, **kwargs):  # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs):  # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self, *args, **kwargs):  # real signature unknown
        pass

    def __repr__(self, *args, **kwargs):  # real signature unknown
        """ Return repr(self). """
        pass

    def __reversed__(self, *args, **kwargs):  # real signature unknown
        """ Return a reverse iterator. """
        pass

    start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    step = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default