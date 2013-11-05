# Chapter 11: Files

## Summary

11.2 Opening, reading from and closing files. Intro to runtime contexts.  
11.3 Writing to files.  
11.4 Binary files and reading/writing bytes. No encoding necessary!  
11.5 Using `Stream` objects from non-files like strings, compressed files.  
11.6 `Standard output` and `error` and writing a `Context Manager`.  


## 11.2 Reading from text files
the `open` command accepts a file path, a `mode` and an `encoding` and returns a **stream** object.  
Stream objects handle streams of characters.  
The path input is a system-agnostic string.  
Always specify an encoding!  

Use `with` to open a file in a **runtime context**.
It will be automatically closed once the context ends.
The runtime context tells the stream object when it is entering and exiting the context.
The stream object knows to close itself upon leaving.

Use a `for` loop or `readline()` to read single lines.
`for` loop works because the stream object is an iterator!


## 11.3 Writing to text files
Modes `w` for writing and `a` for appending.
Again, use `with` for a convenient runtime context.


## 11.4 Binary files
When opening a binary or image file we do not pass an encoding.
Encodings are just for converting from strings to bytes.
We read bytes from binary files, not characters.


## 11.5 Stream objects from non-file sources
Generalize when possible.
Instead of accepting a file, accept a stream object.
`io.StringIO()` to treat a string as a file (stream object).
`io.ByteIO()` to treat a bytearray as a binary file.

Python comes with `gzip` and `bzip2` for handling compressed files.
With these modules we can read and write with compressed files without decompressing them!
Can also use a runtime context with them to automatically close them.  
Note: always open compressed files in binary mode.


## 11.6 Standard Input, Output and Error
`sys.stdout` and `sys.stderr` are write-only stream objects.
`print` just appends `\\n` to your string before sending it to `sys.stdout`.

Define a context manager class by including `__enter__` and `__exit__` methods.
The `with` statement takes a *comma-separated list of contexts**.
