# Chapter 15: Porting Chardet to Python 3

## Summary

15.2 Intro to character-encoding auto-detection.
15.3 The `chardet` module implements auto-detection for Python 2.
15.4 using the `2to3` script to begin conversion.
15.5 Multi-file modules and relative imports.
15.6 Debugging and byte streams.
15.7 Always use tests!


## 15.2
Browsers have built-in character-encoding auto-detection to handle poorly-made websites.


## 15.3
Outline of `chardet` architecture and flow.


## 15.5
If Python encounters a `__init__` file in a directory it assumes the files therein comprise a multi-file module.
Python 3 assumes absolute import paths. Use `from . import __` to do relative imports.
