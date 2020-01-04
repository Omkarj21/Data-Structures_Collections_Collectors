# The isdisjoint() method returns True if two sets are disjoint sets. If not, it returns False.
A = {'a', 'b', 'c', 'd'}
B = ['b', 'e', 'f']
C = '5de4'
D = {1 : 'a', 2 : 'b'} # This will check "value"
E = {'a' : 1, 'b' : 2} # This will check "value"
print('Are A and B disjoint?', A.isdisjoint(B)) # Are A and B disjoint? False
print('Are A and C disjoint?', A.isdisjoint(C)) # Are A and C disjoint? False
print('Are A and D disjoint?', A.isdisjoint(D)) # Are A and D disjoint? True
print('Are A and E disjoint?', A.isdisjoint(E)) # Are A and E disjoint? False
# ----------------------------------------------------------------------------
# issubset() = method returns True if all elements of set are present in another set (passed as an argument). If not, it returns False.
# issuperset() = method returns True if a set has every elements of another set (passed as an argument). If not, it returns False.
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
# Returns True
print(A.issubset(B))
# Returns False
print(B.issubset(A))
# Returns True
print(A.issuperset(B))
# Returns False
print(B.issuperset(A))
# ----------------------------------------------------------------------------