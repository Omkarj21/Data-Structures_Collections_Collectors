# SET is an unordered collection of unique items and mutable. Set is defined by values separated by comma inside braces { }.
# Items in a set are not ordered.
# discard() = if the item does not exist in the set, it remains unchanged.
# remove() =  if the item does not exist in the set, will raise an error in such condition.
# Sets can be used to carry out mathematical set operations like union, intersection, difference and symmetric difference

tp1 = {2, 1, 2, 4, 6, 2, 5, 9, 1, 2, 8, 3, 7, 2}
print(tp1)
tp1.add(12)
print("SET Value changed : ", tp1)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 12}
print(len(tp1))  # 10, length

tp1.update([44, 55], {11, 66, 88})
print("Update SET :", tp1)

tp1.remove(3)
print("Removed iteam 3 : ", tp1)  # 11, This retunrs position where 3 is located

tp1.discard(7)
print("Discarded iteam 7 : ", tp1)  # 11, This retunrs position where 3 is located

tp1.pop()
print("Pop function : ", tp1)

tp1.clear()
print("Clear SET : ", tp1)

x = {3 * x for x in range(10) if x > 5}
print("SET Comprehension : ", x)

# ----------------------------------
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use | operator = Union
# Output: {1, 2, 3, 4, 5, 6, 7, 8}
print("Union : ", A | B)
# ----------------------------------
# use & operator = intersection
# Output: {4, 5}
print("intersection : ", A & B)
# ----------------------------------
# use - operator on A = Difference
# Output: {1, 2, 3}
print("Difference : ", A - B)
# ----------------------------------
# use ^ operator = symmetric_difference
# Output: {1, 2, 3, 6, 7, 8}
print(A ^ B)
# ----------------------------------
# symmetric_difference_update =>
A = {'a', 'c', 'd'}
B = {'c', 'd', 'e' }
result = A.symmetric_difference_update(B)
print('A = ', A) # A = {'a', 'e'}
print('B = ', B) # B = {'d', 'c', 'e'}
print('result = ', result) # result =  None
# ----------------------------------
# difference_update =>
A = {'a', 'c', 'g', 'd'}
B = {'c', 'f', 'g'}
result = A.difference_update(B)
print('A = ', A) # A will be equal to A-B
print('B = ', B) # B will be unchanged
print('result = ', result) # None
# ----------------------------------
# intersection_update =>
A = {1, 2, 3, 4}
B = {2, 3, 4, 5, 6}
C = {4, 5, 6, 9, 10}
result = C.intersection_update(B, A)
print('result =', result) # result will be None
print('C =', C) # C will be equal to the intersection of A, B and C
print('B =', B) # B remains unchanged
print('A =', A) # A remains unchanged
# ----------------------------------