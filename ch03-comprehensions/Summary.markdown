# Chapter 3: Comprehensions

## Summary
Exploring comprehensions of Python - a very powerful tool.

3.2 Details moving around the filesystem using the python shell. It also covers handling files and file paths using the modules `os`, `glob`, `os.path`.

3.3 Introduces the **List Comprehension** in order to map a function to list elements and apply a filter using `if`.

3.4 Introduces the **Dictionary Comprehension** which acts just like the list comprehension but returns a dict.

3.5 Introduces the **Set Comprehension**, just like the previous two.

## Takeaway
Can use comprehensions over container classes to apply functions and filters on their elements.


## 3.2 Working With Files and Directories
Playing with the `os` module.
    import os
    os.getcwd()
    os.chdir(x)
    os.path.join(x,y,z...)
    os.path.split(pathname)
    os.path.splitext(filename)

To get absolute path info:
    os.path.realpath(filename)

Playing with the `glob` module.
    import glob
    glob.glob('examples/*.xml')
    glob.glob('*test*.py)

File metadata with `os.stat`


## 3.3 List Comprehensions
An easy way to apply a function to a list, or sublist, of elements.
`[func(x) for x in list if bool_expression]`


## 3.4 Dict Comprehensions
`{expression:expression for x in list if bool_expression}`

Flip keys and values:

    >>> dc = {'a': 1, 'b': 2, 'c':3}
    >>> dc
    {'c': 3, 'b': 2, 'a': 1}
    >>> dc.items()
    dict_items([('c', 3), ('b', 2), ('a', 1)])
    >>> {val: key for key, val in dc.items()}
    {1: 'a', 2: 'b', 3: 'c'}
    >>>

## 3.5 Set Comprehensions
`{expression for x in list if bool_expression}`

