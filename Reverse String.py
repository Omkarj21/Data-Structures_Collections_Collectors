# Sequence Order Data Structures = String, List, Tuple
# Non Sequence Data Structures = Set, Dictionary

st = "Hello World"
print("Given String : ",st)
print("Length of the String : ",len(st))
print("String Reverse in Single Line :" ,st[::-1])


for i in range(len(st) - 1,-1,-1):
    print("String Reverse in Line by Line :" ,st[i])
