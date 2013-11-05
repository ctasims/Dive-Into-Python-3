# Chapter 13: Serializing Python Objects

## Summary

13.1 The problem: how do you save, reuse, and/or send data structures?  
13.2 The pickle protocol dumps data structure in binary format into file.  
13.3 Can load the pickled data structure back into Python.  
13.4 Can also serialize to a `bytes` object in memory.  
13.5 Be aware of the four different pickle protocols.  
13.6 Use `pickletools` to find version number and view binary data.  
13.7 Use `JSON` for cross-language compatible serialization.  
13.8 Serializing data as `JSON` and making it pretty.  
13.9 `JSON` has no data type for tuples and bytes!  
13.10 Can create custom serialization formats to handle encoding and decoding of unsupported data, like bytes.  
13.10 Loading `JSON` back into Python.  


## 13.2 Saving data to a pickle file

    >>> shell = 1
    >>> entry = {}
    >>> entry['title'] = 'Dive into history, 2009 edition'
    >>> entry['article_link'] = 'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition'
    >>> entry['comments_link'] = None
    >>> entry['internal_id'] = b'\xDE\xD5\xB4\xF8'
    >>> entry['tags'] = ('diveintopython', 'docbook', 'html')
    >>> entry['published'] = True
    >>> import time
    >>> entry['published_date'] = time.strptime('Fri Mar 27 22:20:42 2009')
    >>> entry['published_date']
    time.struct_time(tm_year=2009, tm_mon=3, tm_mday=27, tm_hour=22, tm_min=20, tm_sec=42, tm_wday=4, tm_yday=86, tm_isdst=-
    1)
    >>> import pickle
    >>> with open('entry.pickle', 'wb') as f:
    ...   pickle.dump(entry, f)
    ...
    >>>

We create a dict with a bunch of data types, then dump it to binary format into file.  
Don't assume compatibility between different Pickle protocols.


## 13.3 Loading data from a pickle file

    >>> shell = 2
    >>> entry
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'entry' is not defined
    >>> import pickle
    >>> with open('entry.pickle', 'rb') as f:
    ...   entry = pickle.load(f)
    ...
    >>> entry
    {'tags': ('diveintopython', 'docbook', 'html'), 'published': True, 'comments_link': None, 'published_date': time.struct_
    time(tm_year=2009, tm_mon=3, tm_mday=27, tm_hour=22, tm_min=20, tm_sec=42, tm_wday=4, tm_yday=86, tm_isdst=-1), 'interna
    l_id': b'\xde\xd5\xb4\xf8', 'title': 'Dive into history, 2009 edition', 'article_link': 'http://diveintomark.org/archive
    s/2009/03/27/dive-into-history-2009-edition'}
    >>> entry['tags']
    ('diveintopython', 'docbook', 'html')

Using pickle we can de-serialize our data back into Python data.

    >>> import pickle
    >>> with open('entry.pickle', 'wb') as f:
    ...   pickle.dump(entry, f)
    ...
    >>> with open('entry.pickle', 'rb') as f:
    ...   entry2 = pickle.load(f)
    ...
    >>> entry == entry2
    True
    >>> entry2 is entry
    False
    >>> entry2['tags']
    ('diveintopython', 'docbook', 'html')
    >>> entry2['internal_id']
    b'\xde\xd5\xb4\xf8'

It's a perfect copy of our original data!


## 13.4 Pickling without a file

    >>> shell
    1
    >>> b = pickle.dumps(entry)
    >>> b
    b'\x80\x03}q\x00(X\x0e\x00\x00\x00published_dateq\x01ctime\nstruct_time\nq\x02(M\xd9\x07K\x03K\x1bK\x16K\x14K*K\x04KVJ\x
    ff\xff\xff\xfftq\x03}q\x04\x86q\x05Rq\x06X\x0c\x00\x00\x00article_linkq\x07XJ\x00\x00\x00http://diveintomark.org/archive
    s/2009/03/27/dive-into-history-2009-editionq\x08X\t\x00\x00\x00publishedq\t\x88X\x05\x00\x00\x00titleq\nX\x1f\x00\x00\x0
    0Dive into history, 2009 editionq\x0bX\x0b\x00\x00\x00internal_idq\x0cC\x04\xde\xd5\xb4\xf8q\rX\r\x00\x00\x00comments_li
    nkq\x0eNX\x04\x00\x00\x00tagsq\x0fX\x0e\x00\x00\x00diveintopythonq\x10X\x07\x00\x00\x00docbookq\x11X\x04\x00\x00\x00html
    q\x12\x87q\x13u.'
    >>> type(b)
    <class 'bytes'>
    >>> entry3 = pickle.loads(b)
    >>> entry3
    {'article_link': 'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition', 'published_date': time.st
    ruct_time(tm_year=2009, tm_mon=3, tm_mday=27, tm_hour=22, tm_min=20, tm_sec=42, tm_wday=4, tm_yday=86, tm_isdst=-1), 'ti
    tle': 'Dive into history, 2009 edition', 'internal_id': b'\xde\xd5\xb4\xf8', 'comments_link': None, 'published': True, '
    tags': ('diveintopython', 'docbook', 'html')}
    >>> entry3 == entry
    True

`pickle.dump` takes a stream object and writes the data to it.
`pickle.dumps` returns the pickled data as a `bytes` object.  
Same applies with `pickle.load` and `pickle.loads`.


## 13.6 Debugging pickle files

    >>> import pickletools
    >>> with open('entry.pickle', 'rb') as f:
    ...   pickletools.dis(f)
    ...
        0: \x80 PROTO      3
        2: }    EMPTY_DICT
        3: q    BINPUT     0
        5: (    MARK
        6: X        BINUNICODE 'published_date'
        ... snip...
      354: q        BINPUT     19
      356: u        SETITEMS   (MARK at 5)
      357: .    STOP
    highest protocol among opcodes = 3
    >>>

Use `pickletools` to determine pickle protocol version number (3 in this case).  
See `pickleversion.py`.

    >>> import pickleversion
    >>> with open('entry.pickle', 'rb') as f:
    ...   v = pickleversion.protocol_version(f)
    ...
    >>> v
    3

## 13.7 Serializing Python objects to be read by other languages
Use `JSON` for language cross-compatibility.  
JSON encodes data as text using a Unicode encoding (UTF-32, UTF-16 or UTF-8).


## 13.8 Saving data to a JSON file

    >>> basic_entry = {}
    >>> basic_entry['id'] = 256
    >>> basic_entry['title'] = 'Dive into history, 2009 edition'
    >>> basic_entry['tags'] = ('diveintopython', 'docbook', 'html')
    >>> basic_entry['published'] = True
    >>> basic_entry['commens_link'] = None
    >>> import json
    >>> with open('basic.json', mode='w', encoding='utf-8') as f:
    ...   json.dump(basic_entry, f)

You can never go wrong with UTF-8.  
Use `indent` to prettify the output:

    >>> with open('basic-pretty.json', mode='w', encoding='utf-8') as f:
    ...   json.dump(basic_entry, f, indent=2)

Results:

    {
      "commens_link": null, 
      "id": 256, 
      "tags": [
        "diveintopython", 
        "docbook", 
        "html"
      ], 
      "title": "Dive into history, 2009 edition", 
      "published": true
    }


## 13.9 Mapping of Python datatypes to JSON
JSON does not have built-in data types for handling tuples and bytes.  
Also note that `False` and `True` become `false` and `true`.


## 13.10 Serializing datatypes unsupported by JSON

    >>> entry
    {'published_date': time.struct_time(tm_year=2009, tm_mon=3, tm_mday=27, tm_hour=22, tm_min=20, tm_sec=42, tm_wday=4, tm_
    yday=86, tm_isdst=-1), 'article_link': 'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition', 'pu
    blished': True, 'title': 'Dive into history, 2009 edition', 'internal_id': b'\xde\xd5\xb4\xf8', 'comments_link': None, '
    tags': ('diveintopython', 'docbook', 'html')}
    >>> json
    <module 'json' from 'C:\\Python33\\lib\\json\\__init__.py'>
    >>> with open('entry.json', 'w', encoding='utf-8') as f:
    ...   json.dump(entry, f)
    ...
    Traceback (most recent call last):
      File "<stdin>", line 2, in <module>
      File "C:\Python33\lib\json\__init__.py", line 183, in dump
        for chunk in iterable:
      File "C:\Python33\lib\json\encoder.py", line 414, in _iterencode
        for chunk in _iterencode_dict(o, _current_indent_level):
      File "C:\Python33\lib\json\encoder.py", line 388, in _iterencode_dict
        for chunk in chunks:
      File "C:\Python33\lib\json\encoder.py", line 422, in _iterencode
        o = _default(o)
      File "C:\Python33\lib\json\encoder.py", line 173, in default
        raise TypeError(repr(o) + " is not JSON serializable")
    TypeError: b'\xde\xd5\xb4\xf8' is not JSON serializable

See `customserializer.py`:

    >>> import customserializer as cus
    >>> with open('entry.json', 'w', encoding='utf-8') as f:
    ...   json.dump(entry, f, default=cus.to_json)

Results:

    {"published_date": [2009, 3, 27, 22, 20, 42, 4, 86, -1], "article_link": "http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition", "published": true, "title": "Dive into history, 2009 edition", "internal_id": {"__class__": "bytes", "__value__": [222, 213, 180, 248]}, "comments_link": null, "tags": ["diveintopython", "docbook", "html"]}


## 13.11 Loading data from a JSON file

    >>> del entry
    >>> entry
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'entry' is not defined
    >>> import json
    >>> with open('entry.json', 'r', encoding='utf-8') as f:
    ...   entry = json.load(f)
    ...
    >>> entry
    {'tags': ['diveintopython', 'docbook', 'html'], 'published': True, 'comments_link': None, 'published_date': [2009, 3, 27
    , 22, 20, 42, 4, 86, -1], 'internal_id': {'__value__': [222, 213, 180, 248], '__class__': 'bytes'}, 'title': 'Dive into
    history, 2009 edition', 'article_link': 'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition'}

Notice the time_struct and bytes objects are not restored.
They were converted into dictionaries when we serialized them, so now we get dicts back.
We'll add a `from_json` method to handle this.

    >>> import customserializer as cus
    >>> with open('entry.json', 'r', encoding='utf-8') as f:
    ...   entry = json.load(f, object_hook=cus.from_json)
    ...
    >>> entry
    {'tags': ['diveintopython', 'docbook', 'html'], 'published': True, 'comments_link': None, 'published_date': [2009, 3, 27
    , 22, 20, 42, 4, 86, -1], 'internal_id': b'\xde\xd5\xb4\xf8', 'title': 'Dive into history, 2009 edition', 'article_link'
    : 'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition'}

Note that this won't give us back our tuple, which was converted into a list.

    >>> with open('entry.json', 'r', encoding='utf-8') as f:
    ...   entry2 = json.load(f, object_hook=cus.from_json)
    ...
    >>> entry2 == entry
    False
    >>> entry['tags']
    ('diveintopython', 'docbook', 'html')
    >>> entry2['tags']
    ['diveintopython', 'docbook', 'html']

