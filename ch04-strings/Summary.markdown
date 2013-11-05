# Chapter 4: Strings

## Summary

4.2 Brief history and intro to Unicode and character encodings.  
4.3 Python and (Unicode) strings.  
4.4 String formatting: using compound field names to access data and format specifiers to render it as desired.  
4.5 Various String methods like converting between case and slicing, which acts just like list slicing!  
4.6 Python 3 implements a separation of text and data through strings and bytes. Use `encode()` and `decode` methods to convert between them, based on a character encoding.  
4.7 How to change the character encoding of a `.py` file. Default is UTF-8.  


## Takeaway


## 4.2 Unicode
Python 3 stores strings as Unicode. These Unicode strings can be encoded into bytes using character encodings like UTF-8 and ASCII.
"The Unicode standard describes how characters are represented by code points."
Code points are base 16, integer values that represent characters.

Unicode -> code point -> byte encoding

Therefore, **Unicode strings are a sequence of code points**, with values ranging from 0 through 0x10FFFF (1,114,111 decimal).

**Encodings are just rules for translating a Unicode string into a sequence of bytes.**


### UTF-8
Unicode Transformation Format-8
* if code point less than 128, it's represented by the corresponding byte value.
* if code point >= 128, turned into sequence of 2, 3 or 4 bytes where each byte of this sequence is between 128 and 255.

What's special about UTF-8:
* It can handle ANY Unicode code point.
* Encoded strings contain no zero bytes so byte ordering issues and C functions are no problem.
* It's compact - most characters only require 1 or 2 bytes.
* ASCII is valid UTF-8.
* Can find teh start of the next UTF-8-encoded code point and resynchronize, when bytes are corrupted or lost. Random 8-bit data will likely not look like valid UTF-8.

From [Python 3 Docs](http://docs.python.org/3/howto/unicode.html)


## 4.3 Diving In
String characters can be accessed through 0-based indexing.
Use `+` to concatenate strings.


## 4.4 Formatting Strings
`'Inserting {0} into {1}'.format('values', 'strings')`

Can use compound field names with psuedo-Python syntax for more complex formatting.

    >>> import humansize
    >>> si_suff = humansize.SUFFIXES[1000]
    >>> si_suff
    ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
    >>> '1000{0[0]} = 1{0[1]}'.format(si_suff)
    '1000KB = 1MB'

Use format specifiers for presenting text in a desired fashion:

    >>> '{0:.2f}'.format(1500.25)
    '1500.25'
    >>> '{0:.2e}'.format(1500.25)
    '1.50e+03'

`:` marks the start of the specifier.


## 4.5 Other Common String Methods
`s.splitlines()` to get a list of sub-strings separated based on carriage return.
`s.upper()` to convert all characters to upper-case.
`s.lower()` to convert all characters to lower-case.
Can use `s.count(c)` to count # of occurrences of a character in a string.

`s.split('d', n)` to split string into list of sub-strings based on separator d and # of splits n:

    >>> query = 'user=pilgrim&db=master&pw=papaya'
    >>> query
    'user=pilgrim&db=master&pw=papaya'
    >>> params = query.split('&')
    >>> params
    ['user=pilgrim', 'db=master', 'pw=papaya']
    >>> sub_params = [p.split('=', 1) for p in params]
    >>> sub_params
    [['user', 'pilgrim'], ['db', 'master'], ['pw', 'papaya']]
    >>> dct = dict(sub_params)
    >>> dct
    {'db': 'master', 'user': 'pilgrim', 'pw': 'papaya'}

`slice()` strings just like lists.


## 4.6 Strings vs. Bytes
**string**: an immutable sequence of characters.
**byte**: an immutable sequence of numbers between 0 and 255.
**bytearray**: a mutable object containing bytes. Allows assignment by index notation.

    >>> by = b'abcd\x65'
    >>> by
    b'abcde'
    >>> type(by)
    <class 'bytes'>
    >>> isinstance(by, bytes)
    True
    >>> len(by)
    5
    >>> by += b'\xff'
    >>> by
    b'abcde\xff'
    >>> by[5]
    255
    >>> by2 = b'\xff'
    >>> by2
    b'\xff'
    >>> print(by2)
    b'\xff'
    >>> by3 = b'\xfe'
    >>> by3
    b'\xfe'
    >>> len(by)
    6
    >>> by[0]
    97
    >>> by[1]
    98
    >>> by[0] = 102
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'bytes' object does not support item assignment

Playing with bytearrays:

    >>> by
    b'abcde\xff'
    >>> barr = bytearray(by)
    >>> barr
    bytearray(b'abcde\xff')
    >>> len(barr)
    6
    >>> barr[0]=102
    >>> barr
    bytearray(b'fbcde\xff')
    >>> type(barr)
    <class 'bytearray'>
    >>> isinstance(barr, bytearray)
    True

Convert between Unicode and character encoding like UTF-8 using `string.encode(enc)` and `bytes.decode(enc)`.


## 4.7 Character Encoding of Python Source Code
`# -*- coding: windows-1252 -*-` to change from the default encoding of UTF-8.

