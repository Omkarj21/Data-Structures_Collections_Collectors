# Dictionary is an unordered collection(values will be shuffled.) of key-value pairs which is Mutable.
# Dict can be nested, alphabets = { 'a' : 'apple' , 'b' : 'ball' , 'c' : 'cat' ,’d’ : {1,2,3} }
# Dictionary is ordered only when it is converted from Tuple

tuple1 = ('name','omkar'),('role',1),('gender',"M"),('std',10)
d2 = {'b': 200, 'd': 400}
dict3 = dict(tuple1)
dict3["city"] = "Pune" # Add new Key-Value Pair
dict3["Country"] = "India" # Add new Key-Value Pair
dict3["name"] = "Omkar Jadhav" # Update Key-Value Pair
dict3["Property"] = "India" # Update Key-Value Pair
dict3['children'] = ['Ralph', 'Betty', 'Joey'] # Nested List
dict3['pets'] = {'dog': 'Fido', 'cat': 'Sox'} # Nested Dictionary
dict3.update(d2) # Merge 2 Dictioneries and updates the common key
print(dict3["pets"]["cat"]) #Access nested Dict element
print("Using Get = ",d2.get('d'))
print(dict3["children"]) #Access nested List element
print(dict3.pop(["children"][0])) #Delete the given key
print(len(dict3)) # Length
del dict3["gender"] # Delete Key-Value Pair
print(id(dict3)) # Shows Memory, Before clear
print(dict3)
print("Keys - ",dict3.keys()) # Show keys
print("Values - ",dict3.values()) # Show values
print("Items - ",dict3.items()) # Show Key - values
print("PopItems : ",dict3.popitem()) #Removes Last pair of dictionary.
print(dict3)
dict3.clear()   # Clear Dictionary, this clears data but not Memory
print(id(dict3)) # After clear
print(dict3)

# copy() : This method returns a shallow copy of the dictionary. It doesn't modify the original dictionary.
cpy = ('name','omkar'),('role',1),('gender',"M"),('std',10)