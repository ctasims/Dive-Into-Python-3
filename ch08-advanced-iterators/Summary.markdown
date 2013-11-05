# Chapter 8: Advanced Iterators

## Summary

8.1 alphametic puzzles and Hettinger's 14-line program for solving them.  
8.2 `re.findall` to find non-overlapping patterns.  
8.3 Use sets to gather the unique characters present.  
8.4 the `assert` statement, which checks for conditions that should never happen.  
8.5 **generator expressions** which are statements that return an iterator.  
8.6 `itertools.permutations` for computing permutations of given things.  
8.7 various other tools from the `itertools` module for dealing with groups and sequences of things.  
8.8 translation for mapping one byte into another.  
8.9 `eval` and its complexities, dangers and hopes.  

See file alphametics.py for in-depth comments.

## 8.2 Finding all occurrences of a pattern
`re.findall(pattern, string)` finds all **non-overlapping** instances of the pattern in the given string and returns them.


## 8.4 Making assertions
Assertions should only be used to check for conditions that should *never* happen.
Note that they are optimized away, and really just represent `if __debug__`.
However, most don't use Python's optimized mode since it doesn't really optimize.


## 8.5 Generator expressions
Like an anonymous function that yields values.
One-liner generator.
Write them just like list comprehensions, but with `()` instead of `[]`.
Faster than list comprehensions so use them when building throwaway sequences/lists.


## 8.6 Calculating permutations
`itertools.permutations` for permutations, `combinations` for the same.
They can be passed any sort of sequence or string, and return an iterator.


## 8.7 The `itertools` module
`#product` for cartesian product.
`#combinations` for combinations.
`#groupby` returns an iterator that returns a key function result and an iterator for the items that shared that result. Pass in a sequence and a key function.
Note that the given sequence must already be sorted.
`#chain` combines the results of given iterators into a single iterator.
`zip()` returns an iterator that creates pairs from same-index elements of passed-in sequences.
`#zip_longest` is similar to `zip` but includes trailing elements, pairing them with `None`.

We create a dict after zipping the ordinal representations of the digits and chars together so the puzzle string can be converted.


## 8.8 A new kind of string manipulation
Map one byte to another in a string using `string.translate()`.


## 8.9 Evaluating arbitrary strings as Python expressions
Be afraid of `eval`. Be very afraid.
To handle untrusted input we have to set the `__builtins__` module to `None` and find ways to avoid DDoS attacks.
