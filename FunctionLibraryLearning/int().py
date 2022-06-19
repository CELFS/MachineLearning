class int(object):
    """
    int([x]) -> integer
    int(x, base=10) -> integer

    Convert a number or string to an integer, or return 0 if no arguments
    are given.  If x is a number, return x.__int__().  For floating point
    numbers, this truncates towards zero.

    If x is not a number or if base is given, then x must be a string,
    bytes, or bytearray instance representing an integer literal in the
    given base.  The literal can be preceded by '+' or '-' and be surrounded
    by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
    Base 0 means to interpret the base from the string as an integer literal.
    >>> int('0b100', base=0)
    4
    """

    def as_integer_ratio(self):  # real signature unknown; restored from __doc__
        """
        Return integer ratio.

        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.

        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_length(self):  # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.

        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs):  # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    @classmethod  # known case
    def from_bytes(cls, *args, **kwargs):  # real signature unknown
        """
        Return the integer represented by the given array of bytes.

          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs):  # real signature unknown
        """
        Return an array of bytes representing an integer.

          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs):  # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs):  # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs):  # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs):  # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs):  # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __divmod__(self, *args, **kwargs):  # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs):  # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs):  # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs):  # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs):  # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs):  # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs):  # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs):  # real signature unknown
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

    def __index__(self, *args, **kwargs):  # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
        pass

    def __init__(self, x, base=10):  # known special case of int.__init__
        """
        int([x]) -> integer
        int(x, base=10) -> integer

        Convert a number or string to an integer, or return 0 if no arguments
        are given.  If x is a number, return x.__int__().  For floating point
        numbers, this truncates towards zero.

        If x is not a number or if base is given, then x must be a string,
        bytes, or bytearray instance representing an integer literal in the
        given base.  The literal can be preceded by '+' or '-' and be surrounded
        by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
        Base 0 means to interpret the base from the string as an integer literal.
        >>> int('0b100', base=0)
        4
        # (copied from class doc)
        """
        pass

    def __int__(self, *args, **kwargs):  # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs):  # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs):  # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs):  # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs):  # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs):  # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs):  # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs):  # real signature unknown
        """ -self """
        pass

    @staticmethod  # known case of __new__
    def __new__(*args, **kwargs):  # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs):  # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs):  # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs):  # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs):  # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs):  # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs):  # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs):  # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __repr__(self, *args, **kwargs):  # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs):  # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs):  # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs):  # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs):  # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs):  # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs):  # real signature unknown
        """
        Rounding an Integral returns itself.
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs):  # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs):  # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs):  # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs):  # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs):  # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs):  # real signature unknown
        """ Return value^self. """
        pass

    def __sizeof__(self, *args, **kwargs):  # real signature unknown
        """ Returns size in memory, in bytes. """
        pass

    def __sub__(self, *args, **kwargs):  # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs):  # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs):  # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs):  # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""