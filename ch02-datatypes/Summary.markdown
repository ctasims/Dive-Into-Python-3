## 2.2 Booleans
True or False.
Can be treated as numbers: True = 1, False = 0.

`Boolean context` is location where boolean expression is expected.


## 2.3 Numbers
Ints and floats. Python tells them apart by the presence of a decimal point.
int now acts like old long.
ints no longer limited by sys.maxInt.

fractions with module fractions.

`/` means float division, always.
`//` rounds up.
All numbers except 0 are True in boolean contexts.


## 2.4 Lists
A list is an ordered set.
`slice()` to get a complete copy of the list.
Slicing includes the start index but excludes the end index.
Can use negative indexing.

### 2.4.3 Four ways to add to a list:
* `+` to concatenate lists and return a new one.
* `append(element)` adds to the end.
* `extend([])` appends given elements to end of list.
* `insert(index, element)` inserts element into list at given index.

### 2.4.4 Searching
`list.count(element)` to count # of occurrences in list.
`element in list` -> whether or not element is present in list.
`list.index(element)` gives its index. If not found, throws `ValueError`. Can give start and end range to search through.

### 2.4.5 Removing elements
Lists never have gaps. To remove an element:
* `del list[n]`
* `list.remove('my_item')` to remove the *first instance*. Will throw ValueError if not found.
* list.pop(n) will remove and return the popped item. If n not given, pops the last item.

An empty list is False in boolean context. True if it has any items.

### Memory
A list is represented as an array. The largest costs are due to everything having to move:
* growing beyond the current allocation size.
* inserting/deleting near beginning

If modifying both ends of list, use a `collections.deque`, which is slow if operating on middle.


## 2.5 Tuples
A tuple is simply an immutable list.
Tuple elements have a defined order and can be accessed with 0-based indexing.
Can `slice` a tuple. The result is a tuple.

Why use tuples?
* tuples are faster than lists. Use them if you have set of constant values.
* Immutability can be useful. Duh.
* Can be used as dict keys, if values are immutable.

Tuples and lists can be converted to each other.
Don't forget the extra comma when making a tuple with one value.

We can quickly assign tuples of values to different variables using tuples.
`>>> x,y,z = range(3)`


## 2.6 Sets
Sets are bags of values. Elements in sets must be **unordered**, **unique** and **immutable**.
`>>> my_set = {1, 2, 'a'}`

Use `set.add(elem)` to add to a set.
Adding a duplicate element to a set is a no-op.

`set.update(a, b, list...)` adds the args to the set.
It can be passed a list.

Remove elements from a set with `set.discard(x)` or `set.remove(x)`.
If x does not exist in the set, `discard` will do nothing, but `remove` will throw a KeyError exception.

`set.pop()` removes an arbitrary value from the set.
`set.clear()` removes all elements and returns an empty set.

### 2.6.4 Set Operations
`x in set` tells whether x is in set.
`set.union(set2)` returns elements in *either* set.
`set.intersection(set2)` returns elements in *both* sets.
`set.difference(set2)` returns elements in set that are not in set2.
`set.symmetric\_difference(set2)` returns elements in *exactly one* set.

    >>> set1 = {2, 4, 5, 9, 12, 21, 30, 51, 76, 127, 195}
    >>> set2 = {1, 2, 3, 5, 6, 8, 9, 12, 15, 17, 18, 21}
    >>> 2 in set1
    True
    >>> 2 in set2
    True
    >>> 1 in set1
      False
    >>> set1.intersect(set2)
      Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
      AttributeError: 'set' object has no attribute 'intersect'
        >>> set1.intersection(set2)
    {9, 2, 12, 5, 21}
    >>> set1.union(set2)
    {1, 2, 195, 4, 5, 6, 8, 12, 76, 15, 17, 18, 3, 21, 30, 51, 9, 127}
    >>> set1.difference(set2)
    {195, 4, 76, 51, 30, 127}
    >>> set1.symmetric_difference(set2)
    {1, 3, 4, 6, 8, 76, 15, 17, 18, 195, 127, 30, 51}

    >>> set1 = {1,3,5,9}
    >>> set2 = {1,2,4,6,8,9}
    >>> set1.issubset(set2)
    False
    >>> set2.issubset(set1)
    False
    >>> set1 = {1,2,4}
    >>> set1.issubset(set2)
    True
    >>> set1.issuperset(set2)
    False
    >>> set2.issuperset(set1)
    True

Sets that contain the same values are equal. Remember: *order doesn't matter*.
An empty set evaluates to False in a boolean context.
A set with anything in it evaluates to True.


## 2.7 Dictionaries
Unordered, unique key-value pairs. Dicts can be of any length.
Keys are usually strings, ints, and a few others.
`x in dict` to see if x is a key in dict.
An empty dict evaluates to False. A non-empty dict evaluates to True.
Dicts are optimized for retrieving values given a known key.

### Memory
Note that dicts have a fast-path that only deals with Str keys which speeds up the constant factors and "how quickly a typical program finishes."

* copy and iteration are both O(n) in average and worst-case.
* get, set, delete are O(1) average, O(n) worst.
