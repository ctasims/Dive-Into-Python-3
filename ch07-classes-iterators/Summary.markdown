# Chapter 7: Classes & Iterators

## Summary

7.2 The structure and conventions for creating a class with an `__init__` method.
7.3 Simple example of isntantiating an instance of a class.
7.4 Instance variables, `self.max`, are specific to the instance and accessible in each method.
7.5 Creating an example iterator for the Fibonacci sequence. It only needs an `__iter__` method (and a `__next__` method?) to be an iterator.
7.6 Convert our pluralizer into an efficient module that uses an iterator to pluralize words.


## 7.2 Defining classes
The `__init__` function is run after the instance object is created, so don't think of it as the constructor.


## 7.5 A Fibonacci Iterator
The `__iter__` method must return an object with a `__next__` method.
The `StopIteration` exception is not treated like an error and is handled gracefully, e.g. by `for` loops.


## 7.6 A Plural Rule Iterator
See plural6.py for code comments.
Our iterator reduces redundancy of reading regex and generating functions.
Still has optimizations left, like keeping file open, but overall presents a much cleaner interface for iterating through regex options.
It has a quick startup, good performance, and maintains SoC between code and data.
