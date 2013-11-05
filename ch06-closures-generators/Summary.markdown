# Chapter 6: Closures and Generators

## Summary

6.2 Introduces more tools to our regexp toolbox: matching characters, negations and group references.  
6.3 Functions are objects are can be stored and referred to as such.  
6.4 Using the closure concept to generate dynamic functions for regexp matching.  
6.5 Separate data from code by storing regexp pattern, search and replace strings in a text file.  
6.6 Generators are "resumable" functions and lazily operate through their logic.  


## 6.2 Using Regular Expressions
File plural1.py for pluralizing English nouns.
`[xyz]` matches exactly one of the chars contained in the brackets.
`[^xyz]` matches exactly one of the chars **not contained** in the brackets.
`re.sub` replaces **all** matches found, not just the first.
So `re.sub('[abc]', 'o', 'caps')` returns `oops`.
Can also use `re.sub` to search and replace, with `\1` to remember groups.


## 6.3 A list of functions
File `plural2.py` wherein the rules are separated into match and apply functions.
Remember that **everything** in Python is an object - even functions.


## 6.4 A list of patterns
Can use closures to apply parameters from outer functions.


## 6.5 A file of patterns
Store patterns in separate file for easy maintenance and separation of concerns.
Code is code. Data is data.


## 6.6 Generators
Create resumable function, or **generator function**, using the `yield` keyword.
Generator functions return an iterator known as a generator, which controls the execution of the generator function.
Use `next()` to acquire the next value from the iterator.
Can operate over returned values using a `for` loop.


