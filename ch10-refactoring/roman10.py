import re

class OutOfRangeError(ValueError): pass
class NotIntegerError(ValueError): pass
class InvalidRomanNumeralError(ValueError): pass


roman_numeral_map = (
        ('M',  1000),
        ('CM', 900),
        ('D',  500),
        ('CD', 400),
        ('C',  100),
        ('XC', 90),
        ('L',  50),
        ('XL', 40),
        ('X',  10),
        ('IX', 9),
        ('V',  5),
        ('IV', 4),
        ('I',  1))

to_roman_table = [ None ]
from_roman_table = {}


def to_roman(n):
    ''' Convert integer to Roman numeral.'''
    if not (0 < n < 5000):
        raise OutOfRangeError("number out of range (must be 1..4999)")
    if not isinstance(n, int):
        raise NotIntegerError("non-integers cannot be converted.")
    return to_roman_table[n]


def from_roman(s):
    """ Convert Roman numeral to integer. """
    if not isinstance(s, str):
        raise InvalidRomanNumeralError("Input must be a string")
    if not s:
        raise InvalidRomanNumeralError('Input cannot be blank')
    if s not in from_roman_table:
        raise InvalidRomanNumeralError('Invalid Roman numeral: {}'.format(s))
    return from_roman_table[s]


def build_lookup_tables():
    def to_roman(n):
        result = ''
        for numeral, integer in roman_numeral_map:
            if n >= integer:
                result = numeral
                # decrement current number so we can use it as lookup index.
                n -= integer
                break
        if n > 0:
            # append previous roman numeral - build it up.
            result += to_roman_table[n]
        return result

    for integer in range(1, 5000):
        roman_numeral = to_roman(integer)
        # add numeral and number to tables
        to_roman_table.append(roman_numeral)
        from_roman_table[roman_numeral] = integer

build_lookup_tables()

