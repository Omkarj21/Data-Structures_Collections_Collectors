# Sequence Order = String, List, Tuple
# Non Sequence = Set, Dictionary
# Integers, floats, strings and tuples are objects that cannot be changed i.e. these are immutable,
# which means you cannot change an existing.
# We cannot delete or remove characters from a string. But deleting the string entirely is possible using the keyword del.

str1 = "Computer, Domain"
print("computer" in str1.lower())
str2 = "World"
print("StringUpper : ",str1.upper())
print("StringLower : ",str1.lower())
print("String : ",str1) # Computer
print("Length : ",len(str1)) # 8
print("Search 2nd positional string : ",str1[2]) # m
print("String Split with - sign right side : ",str1[:-2]) # Comput
print("String Split with - sign left side : ",str1[-2:]) # er
print("String position using Index : ",str1.index("u")) # 2
print("Combine 2 string : ",str1+str2)
print("multiple string : ",str1*3)
print("Count of string : ",str1.count("C")) # This is Case Sensetive, if you type "c" small c, it wont work.
list_enumerate = list(enumerate(str1))
print('list(enumerate(str1) = ', list_enumerate)

# IN & NOT IN Operator
print("IN Operator : ", "e" in str1)
print("NOT IN Operator : ", "o" not in str2)

# default(implicit) order
default_order = "{}, {} and {}".format('John','Bill','Sean')
print('\n--- Default Order ---')
print(default_order)

# order using positional argument
positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
print('\n--- Positional Order ---')
print(positional_order)

# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
print('\n--- Keyword Order ---')
print(keyword_order)

a="ACROTE"
print ("String Slice_1",a[-2:-5:2])
print ("String Slice_2",a[-5:-2:2])
print ("String Slice_3",a[-5:2:2])
print ("String Slice_4",a[-5:1:2])
print ("String Slice_5",a[-5:0:2])
print ("String Slice_6",a[-2:2:2])

def cnt():
    str3 = "Hello Dog and where is dog"
    c = 0
    for dog in str3.lower().split():
        if "dog" in dog:
            c +=1
    return c
print(cnt())
    # print("Count of Dog :",c)
# --------------------------------------
str3 = "Delete Entire possible"
print(str3)
del str3
# print("After Delete : ",str3)
# --------------------------------------
# Raw String to ignore escape sequence
# output : This is \x61 \ngood example
print(r"This is \x61 \ngood example")
# --------------------------------------
# default(implicit) order
default_order = "{}, {} and {}".format('Omkar','Karan','OmKaran')
print('\n--- Default Order ---')
print(default_order)
# --------------------------------------
# order using positional argument
positional_order = "{1}, {0} and {2}".format('Omkar','Karan','OmKaran')
print('\n--- Positional Order ---')
print(positional_order)
# --------------------------------------
# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='Omkar',b='Karan',s='OmKaran')
print('\n--- Keyword Order ---')
print(keyword_order)
# --------------------------------------
