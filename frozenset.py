# Frozenset is a new class that has the characteristics of a set, but its elements cannot be changed once assigned.
# While tuples are immutable lists, frozensets are immutable sets.
# Sets being mutable are unhashable, so they can't be used as dictionary keys. On the other hand, frozensets are hashable and can be used as keys to a dictionary.
# Like normal sets, frozenset can also perform different operations like union, intersection, etc.

# initialize A and B
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
print(A.isdisjoint(B))
print(A.difference(B))
# --------------------------
# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')
fSet = frozenset(vowels)
print('The frozen set is:', fSet)
print('The empty frozen set is:', frozenset())
# --------------------------
# random dictionary
person = {"name": "John", "age": 23, "sex": "male"}
fSet = frozenset(person)
print('The frozen set is:', fSet)
# --------------------------