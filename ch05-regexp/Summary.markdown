# Chapter 5. Regular Expressiosn

## Summary

5.1 Regular expressions are a pattern-matching tool for strings.

5.2 Seemingly-simple text parsing tasks can become complicated quickly. RegExps can maintain the simplicity.

5.3 Covers basic regexp patterns for matching hundreds and thousands places of Roman Numerals using `^`, `$`, `?`, `|`, `()`.

5.4 `{n,m}` syntax for more concise expressions.

5.5 Verbose regular expressions can be used to inline documentation into the pattern.

5.6 Getting data from regexps using groups and more complicated expressions.


## 5.2 Case Study: Street Addresses
String methods like `replace()` are sufficient for simple replacements. But they're case-sensitive and hard-code single phrases.
RegExp method `re.sub()` allows for substitutions using regexps.

    >>> s
    '100 NORTH BROAD ROAD'
    >>> s.replace('ROAD', 'RD.')
    '100 NORTH BRD. RD.'
    >>> s[:-4] + s[-4:].replace('ROAD', 'RD.')
    '100 NORTH BROAD RD.'
    >>> import re
    >>> re.sub(r'ROAD$', 'RD.', s)
    '100 NORTH BROAD RD.'
    >>> s = '100 BROAD'
    >>> re.sub('ROAD$', 'RD.', s)
    '100 BRD.'
    >>> re.sub('\\bROAD$', 'RD.', s)
    '100 BROAD'
    >>> re.sub('\bROAD$', 'RD.', s)
    '100 BROAD'
    >>> re.sub('\bROAD$', 'RD.', '100 ROAD')
    '100 ROAD'
    >>> re.sub(r'\bROAD$', 'RD.', s)
    '100 BROAD'
    >>> re.sub(r'\bROAD$', 'RD.', '100 ROAD')
    '100 RD.'
    >>> s = '100 BROAD ROAD APT. 3'
    >>> s
    '100 BROAD ROAD APT. 3'
    >>> re.sub(r'\bROAD$', 'RD.', s)
    '100 BROAD ROAD APT. 3'
    >>> re.sub(r'\bROAD\b', 'RD.', s)
    '100 BROAD RD. APT. 3'


## 5.3-4 Roman Numerals and `{n,m}` Syntax

    >>> pattern = r'^M?M?M?$'
    >>> pattern
    '^M?M?M?$'
    >>> re.search(pattern, 'M')
    <_sre.SRE_Match object at 0x0000000002BFE100>
    >>> re.search(pattern, 'MM')
    <_sre.SRE_Match object at 0x0000000002BFE168>
    >>> re.search(pattern, 'M M')
    >>> re.search(pattern, 'MMM')
    <_sre.SRE_Match object at 0x0000000002BFE100>
    >>> re.search(pattern, 'MMMM')

`?` means match zero or one instance of the preceding character.
`^` matches the start of the string.
`$` matches the end of the string.
`()` to create a group of expressions to match.
`|` denotes OR syntax. `x|y` matches x or y, with x checked first.
`{n,m}` matches n to m instances of the preceding character.


## 5.5 Verbose Regular Expressions
Write regexp using docstring format in order to include comments.
* Whitespace is ignored. Use a backslash to recognize white-space.
* comments are ignored.

When using verbose regexps, remember to pass `re.search` a third parameter of `re.VERBOSE`.

    >>> pattern = '''
    ...
    ... ^                   # beginning
    ... M{0,3}              # thousands
    ... (CM|CD|D?C{0,3})    # hundreds
    ... (XC|XL|L?X{0,3})    # tens
    ... (IX|IV|V?I{0,3})    # ones
    ... $                   # end string
    ... '''
    >>> pattern
    '\n\n^ \t\t\t# beginning\nM{0,3} \t\t# thousands\n(CM|CD|D?C{0,3}) \t# hundreds\n(XC|XL|L?X{0,3}) \t# tens\n(IX|IV|V?I{0
    ,3}) \t# ones\n$ \t\t\t# end string\n'
    >>> re.search(pattern, 'M', re.VERBOSE)
    <_sre.SRE_Match object at 0x00000000023DB750>
    >>> re.search(pattern, 'MCMLXXXIX', re.VERBOSE)
    <_sre.SRE_Match object at 0x00000000023DB6B8>
    >>> re.search(pattern, 'MMMDCCCLXXXVIII', re.VERBOSE)
    <_sre.SRE_Match object at 0x00000000023DB750>
    >>> re.search(pattern, 'M', re.VERBOSE)
    <_sre.SRE_Match object at 0x00000000023DB6B8>


## 5.6 Parsing Phone Numbers
I read through this section yesterday. I'll now attempt to develop the correct regexp without looking at the author's steps.
Based on his criteria, the regexp should handle:
* 3-digit area code
* 3-digit trunk
* 4-digit remainder
* 4-digit extension
* arbitrary separations between groups
* no separation between groups
* area code in parens
* area code preceded by 1 or arbitrary text

I remember some of his strategy...

    >>> pattern = re.compile(r'(\d{3})\D(\d{3})\D(\d{4})\D(\d{4})')
    >>> pattern
    <_sre.SRE_Pattern object at 0x00000000023E2BA0>
    >>> pattern.search('800-555-1212').groups()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'NoneType' object has no attribute 'groups'
    >>> pattern.search('800-555-1212x1212').groups()
    ('800', '555', '1212', '1212')
    >>> pattern.search('1-(800)-555-1212x1212').groups()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'NoneType' object has no attribute 'groups'
    >>> pattern.search('1-800-555-1212x1212').groups()
    ('800', '555', '1212', '1212')

My first attempt doesn't handle simple cases without an extension.
It also breaks on parens around area code.
Next attempt:

    >>> pattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d{0,4})')
    >>> pattern.search('1-(800)-555-1212x1212').groups()
    ('800', '555', '1212', '1212')
    >>> pattern.search('1-800-555-1212x1212').groups()
    ('800', '555', '1212', '1212')
    >>> pattern.search('800-555-1212x1212').groups()
    ('800', '555', '1212', '1212')
    >>> pattern.search('800-555-1212').groups()
    ('800', '555', '1212', '')
    >>> pattern.search('8005551212').groups()
    ('800', '555', '1212', '')
    >>> pattern.search('18005551212').groups()
    ('180', '055', '5121', '2')
    >>> pattern.search('work 1-(800)-555-1212 #1234').groups()
    ('800', '555', '1212', '1234')

I think this is his answer. Note that it doesn't handle a preceding 1 if no separators are used.
But it handles the other requirements!
Mine:

    >>> pattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d{0,4})')

His answer:

    >>> pattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$') 

I forgot to match for the end of the line with `$`.
His also matches arbitrary digits for the extension.

`x+` matches one or more.
`x*` matches zero or more.
`\d` matches any numeric digit.
`\D` matches any non-numeric digit.
`\b` matches a word boundary.
`(x)` is a remembered group whose value can be retrieved using `groups()`, which returns a tuple.

What's a word boundary? Three positions qualify:
* Before the first char in a string, if it's is a word char.
* After the last char in a string, if it's a word char.
* Between two chars in a string, if one is a word char and the other is not.
(From regular-expressions.info)


