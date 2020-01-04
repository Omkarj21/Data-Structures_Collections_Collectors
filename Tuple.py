# Tuple is an ordered sequence of items same as list. The only difference is that tuples are immutable.
# Tuples once created cannot be modified. Tuples are used to write-protect data and are usually
# faster than the list as it cannot change dynamically.
# Deleting a tuple entirely is possible using the keyword del.
# tuple used for heterogeneous (different) datatypes
# Since tuples are immutable, iterating through tuple is faster than with list. So there is a slight performance boost.
# Tuples that contain immutable elements can be used as a key for a dictionary.

tp1 = ((1,2,4,6),[2,5,9,3],{8:5,2:7}) # Tuple can have Dict and List and Tuple
tp2 = (2,1,2,4,6,2,5,9,1,2,8,3,7,2)

print(tp1)
print(tp2)

om = "omkar",
print(type("omkar"))
print(type(om))

print(tp2.count(2)) # 5 , here 2 is item, 2 present in list 5 times
print(len(tp1)) # 3, length
print(tp2.index(3)) # 11, This retunrs position where 3 is located

#Slicing Tuple
print(tp2[0:2]) # Access element of Tuple
print(tp2[0:-2:1]) # Access element of Tuple
print(tp2[0:-2:2]) # Access element of Tuple
print(tp2[0:-2:3]) # Access element of Tuple
print(tp2[:-2]) # Access element of Tuple
print(tp2[-2:]) # Access element of Tuple

tp1[1][1]=10 # Though Tuple is Immutable but members can be mutable
print("Exceptional Mutable Tuple : ",tp1)

# tuple unpacking is also possible
a, b, c = tp1
print(a)
print(b)
print(c)

# Concatenation
# Output: (11, 22, 33, 44, 55, 66)
print((11, 22, 33) + (44, 55, 66))
# Repeat
# Output: ('Om', 'Om', 'Om')
print(("Om",) * 3)

del tp1
print((tp1))