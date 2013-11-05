# Chapter 12: XML

## Summary

12.1 XML is all about data.  
12.2 XML describes hierarchical structured data.  
12.3 Covers the structure of an Atom XML feed.  
12.4 Using the `ElementTree` module to parse XML.  
12.5 Searching an XML tree.  
12.6 ElementTree with the `libxml` parser.  
12.7 Creating XML data.  
12.8 Custom parsers to handle broken XML.


## 12.2 A 5-minute crash couse in XML
`xmlns` attribute to define a namespace.
Namespaces affect all child nodes.
Or use a prefix to explicitly declare namespace.  
Put encoding information on first line: `<?xml version='1.0' encoding='utf-8'?>`  
`xml:lang` to define language of all child elements.


## 12.4 Parsing XML

    >>> import xml.etree.ElementTree as etree
    >>> tree = etree.parse('feed.xml')
    >>> tree
    <xml.etree.ElementTree.ElementTree object at 0x0000000002C8DE80>
    >>> root = tree.getroot()
    >>> root
    <Element '{http://www.w3.org/2005/Atom}feed' at 0x0000000002EB7408>
    >>> root.tag
    '{http://www.w3.org/2005/Atom}feed'
    >>> len(root)
    8
    >>> root[0]
    <Element '{http://www.w3.org/2005/Atom}title' at 0x0000000002EB7318>
    >>> root[0].tag
    '{http://www.w3.org/2005/Atom}title'
    >>> for child in root:
    ...   print(child)
    ...
    <Element '{http://www.w3.org/2005/Atom}title' at 0x0000000002EB7318>
    <Element '{http://www.w3.org/2005/Atom}subtitle' at 0x0000000002EB73B8>
    <Element '{http://www.w3.org/2005/Atom}id' at 0x0000000002EB74F8>
    <Element '{http://www.w3.org/2005/Atom}updated' at 0x0000000002EB7548>
    <Element '{http://www.w3.org/2005/Atom}link' at 0x0000000002EB75E8>
    <Element '{http://www.w3.org/2005/Atom}entry' at 0x0000000002EB7638>
    <Element '{http://www.w3.org/2005/Atom}entry' at 0x0000000002EB7AE8>
    <Element '{http://www.w3.org/2005/Atom}entry' at 0x0000000002EB7EA8>
    >>> root.attrib
    {'{http://www.w3.org/XML/1998/namespace}lang': 'en'}
    >>> root[4]
    <Element '{http://www.w3.org/2005/Atom}link' at 0x0000000002EB75E8>
    >>> root[4].attrib
    {'type': 'text/html', 'href': 'http://diveintomark.org/', 'rel': 'alternate'}
    >>> root[3]
    <Element '{http://www.w3.org/2005/Atom}updated' at 0x0000000002EB7548>
    >>> root[3].attrib
    {}

Elements act like lists which contain their direct children.
They also have attribute dictionaries.


## 12.5 Searching

    >>> root.findall('{http://www.w3.org/2005/Atom}entry')
    [<Element '{http://www.w3.org/2005/Atom}entry' at 0x0000000002EB7638>, <Element '{http://www.w3.org/2005/Atom}entry' at
    0x0000000002EB7AE8>, <Element '{http://www.w3.org/2005/Atom}entry' at 0x0000000002EB7EA8>]
    >>> root.tag
    '{http://www.w3.org/2005/Atom}feed'
    >>> root.findall(root.tag)
    []
    >>> root.findall('{http://www.w3.org/2005/Atom}author')
    []

`#findall` only looks at immediate children of the `root` element.
`#find` to find the first match.

    >>> tree.findall('{http://www.w3.org/2005/Atom}entry')
    [<Element '{http://www.w3.org/2005/Atom}entry' at 0x0000000002EB7638>, <Element '{http://www.w3.org/2005/Atom}entry' at
    0x0000000002EB7AE8>, <Element '{http://www.w3.org/2005/Atom}entry' at 0x0000000002EB7EA8>]
    >>> tree.findall('{http://www.w3.org/2005/Atom}author')
    []
    >>> entries - tree.findall('{http://www.w3.org/2005/Atom}entry')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'entries' is not defined
    >>> entries = tree.findall('{http://www.w3.org/2005/Atom}entry')
    >>> len(entries)
    3
    >>> title_element = entries[0].find('{http://www.w3.org/2005/Atom}title')
    >>> title_element
    <Element '{http://www.w3.org/2005/Atom}title' at 0x0000000002EB77C8>
    >>> title_element.text
    'Dive into history, 2009 edition'
    >>> foo_element = entries[0].find('{http://www.w3.org/2005/Atom}foo')
    >>> foo_element
    >>> type(foo_element)
    <class 'NoneType'>

To use `find` in boolean context, do `if element.find(...) is not None`.
If you just do `if element.find(..)` you're actually testing whether or not that element has any children.
This is because it acts like a list and `[]` evaluates to `False`.
Add `//` to search descendant elements as well.


## 12.6 Going further with LXML
LXML has full XPath support, a faster parser, and support for more complicated expressions.


## 12.7 Generating XML

    >>> new_feed = etree.Element('{http://www.w3.org/2005/Atom}feed', attrib={'{http://www.w3.org/XML/1998/namespace}lang':
    'en'})
    >>> new_feed
    <Element '{http://www.w3.org/2005/Atom}feed' at 0x0000000002EB8458>
    >>> print(etree.tostring(new_feed))
    b'<ns0:feed xmlns:ns0="http://www.w3.org/2005/Atom" xml:lang="en" />'

Pass an element name (namespace and local name) to the `Element` class to create a new element.
Use LXML to set a default namespace. Just use LXML!


## 12.8 Parsing broken XML
XML has draconian error handling, as opposed to HTML.
Create a custom parser and pass the `recover` argument to overcome wellformedness errors.

