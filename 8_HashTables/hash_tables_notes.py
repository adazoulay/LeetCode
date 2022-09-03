
# If implemented properly:
# O(1 + n/m) lookup, insertion, deletion where n is the number of objets and m is the length of the array
# If the load grows too big ie, n >> m: rehashing can be applied to the table, takes O(n + m) but is done infrequently
# Inserting and deleting more efficient that a BST

# Avoid mutating keys otherwise lookup for key will now fail despite still being in hash table
# Instead, remove key, update it, add it back
import collections
import functools

# List of hash table based data structures:
# Set is different because it only stored keys while others tore key-value pairs
# None of them allow for duplicate keys
set()
dict()
collections.defaultdict()
collections.Counter()
# All return a KeyError if accessing value associated with a key is not present
# Except for collections.defaultdict(default) which returns the default value
d = collections.defaultdict(list)
d['k']  # returns []

# collections.Counter() is used for counting the number of occurrences of keys
c = collections.Counter(a=3, b=1)
d = collections.Counter(a=1, b=2)
c + d  # add to counters together: c[x] + d[x], collections.Counter({'a':4, 'b':3})
c - d  # subtract (keeping only positive counter): c[x] - d[x], collections.Counter({'a':2})
c & d  # intersection: min(c[x], d[x]), collections.counter({'a':1, 'b':1})
c | d  # union: max(c[x], d[x]), collections.counter({'a':3, 'b':2})
# To get most common
collections.Counter(a=3, b=1).most_common(1)[0][0]  # similar to nsmallest, returns (x) last elements in an array

x = 3
#  Most important operations for sets:
s = set()
t = set()
s.add(42)  # Adds 42 to the set
s.remove(42)  # Removes 42 from the set !! Raises error if item not in set
s.discard(123)  # Removes 42 from set !! Does NOT raise error if item not in set
x in s  # Returns weather x in s
s <= t  # Returns if s is a subset of t
s - t  # Returns elements in s that are not in t


# Dictionaries:
# Values in dictionary can be any data type
thisdict = {  # (key : value) = item
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#  --- ACCESS ITEMS ---
thisdict["brand"]  # returns value from key !! Raises error if item not in set
thisdict.get("bogus", list)  #  # returns value from key !! Does NOT raise error if item not in set, instead returns default
len(thisdict)  # Returns number of items
thisdict.keys()  # Returns a list of all the keys in dictionary !! returns a view of the dictionary: changes done to the dictionary will be reflected in the keys list.
thisdict.values()  # Returns a list of all the keys in dictionary !! returns a view of the dictionary: changes done to the dictionary will be reflected in the value list.
thisdict.items()  #  # Returns a list of all the key value pairs as a TUPLE !! returns a view of the dictionary: changes done to the dictionary will be reflected in the value list.
"model" in thisdict  # Use in to check if item in dict before trying to access
#  --- CHANGE ITEMS ---
thisdict["year"] = 2018  # Updates value from key  ! Way faster than update
thisdict.update({"year": 2020})  # Can be used with iterable objects, update stuff from one dict to the other
#  --- ADD ITEMS ---
thisdict["year"] = 2018  # Adds value from key if key not present  ! Way faster than update
thisdict.update({"year": 2020})  #  Adds value from key if key not present, Can be used with iterable objects. Ex: update stuff from one dict to the other
#  --- REMOVE ITEMS ---
thisdict.pop("model")  # Removes item with specified key name
thisdict.popitem()  #  Removes the last inserted item
del thisdict["model"]  # Removes item with specified key name
thisdict.clear()  # Empties the dictionary
#  --- DICTIONARY ITERATION ---
for x in thisdict: print(x)  # Prints all key names in dict
for x in thisdict: print(thisdict[x])  # Prints all values in dict
for x, y in thisdict.items(): print(x, y)  # Prints both keys and values
key_val = {key: val for val, key in enumerate(len(10))}  # Returns dict with key and val

def string_hash(s, modulus):
    MULT = 997
    return functools.reduce(lambda v, c: (v * MULT + ord(c)) % modulus, s, 0)


def find_anagrams(dictionary):
    sorted_string_to_anagrams = collections.defaultdict(list)
    for s in dictionary:
        sorted_string_to_anagrams[''.join((sorted(s)))].append(s)

    return [group for group in sorted_string_to_anagrams.values() if len(group) >= 2]