# Below are important LIST Functions =>
# Len, Count, Index, Append, Extend, Pop, Remove, Insert, Sort, Sort(Revers=True), Delete, Clear, Reverse, Max, Min.
# List is Ordered Type Data Structure
# Sequence Order Data Structures = String, List, Tuple
# Non Sequence Data Structures = Set, Dictionary
# list for homogeneous (similar) datatypes.
#---------------------------------------------------------------------------------------
list1 = [(1,2,4,6),[2,5,9,3],{8:5,2:7}] # List can have Dict and List and Tuple
list2 = [2,1,2,4,6,2,5,9,3,2,8,7,2,0]
list3 = ["a","b","c"]

print( list2[-1:-5:-1]) # Will get some output
print( list2[-1:-5:1]) # Will get Empty output

print("Remove Duplicate elements from List : ",set(list2))

# unpacking list
a,b,c=list1
print("Unpacked List 1 : ",a)
print("Unpacked List 1 : ",b)
print("Unpacked List 1 : ",c)

print(len( list1 )) # length of List
print(list2.count(2)) # 5 , here 2 is item, 2 present in List 5 times so answer is 5
print(list1[0][2]) # 4
print(list1[1][3]) # 3
print(list1[2][2]) # 7

print("Index - ",list2.index(4)) # 8, This retunrs position where 4 is located in given list
list1.append([2,3,4,5]) # Adds element at Last

list1.extend(list2) # combines 2 Lists , here List 1 will have List 2 values as well, whereas NO change in List 2 values
add_list = list2+list3
print("Combine 2 list and save in new field : ",add_list)
print("multiply list : ",add_list*2)

print("Before Pop - ", list1)
list1.pop(0) # Pop(index), it deletes given index element, if index not exist then removes last element
print("After Pop - ", list1)
list1.remove(1) # remove(item/element), it deletes/removes given item/element and ITEM is mandatory
print("After remove - ", list1)
list1.insert(0,111) # Syntax = insert(index,item), if index is out of range then it will add at last
list2.insert(-1,222) # Syntax = insert(index,item), -1 index means add number at 2nd last position

list2.sort() # Default is sort in ascending order
print("Ascending = ",list2)
list2.sort(reverse=True) # This sorts in Descending order, If reverse=False then it will show in ascending order.
print("Descending = ",list2)

del list1[1] # Delete 2nd Element of List, 1 is index
print(list1)
list1.clear() # Clear All Elements of List
print(list1)

print(list2)
list2.reverse()
print("After List Reverse : ",list2) # Reverse List elements

print("Maximum number of list: ",max(list2))
#2nd Largest number
list2.sort(reverse=True)
print("2nd Largest number in List 2 : ",list2[1])

print("Minimum number of list: ",min(list2))
#2nd Smallest number
list2.sort()
print("2nd Smallest number in List 2 : ",list2[1])

# IN & NOT IN Operator
print("IN Operator : ", 10 in list2)
print("NOT IN Operator : ", 1001 not in list2)

lst1 = [2,4,6,8]
print("Sum of Total elemets : ",sum(lst1))
print("Sum of Partial elemets : ",sum(lst1[0:2]))
print("Sum of Partial elemets : ",sum(lst1[2:]))
print("Sum of Partial elemets : ",sum(lst1[-2:]))
print("Sum of Partial elemets : ",sum(lst1[:-4]))

list4 = ['o','m','k','a','r']
# Output: r
print(list4[-1])
# Output: o
print(list4[-5])
# Output: [] : 0th to 1st
print(list4[:-5])

# print(list1[0][5]) # Error = Tuple index out of range
# print(list1[1][5]) # Error = List index out of range
# print(list1[2][5]) # Error = Key Does not find