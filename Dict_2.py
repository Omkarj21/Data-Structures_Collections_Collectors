values1 = {1:(1,2),2:[2,5],3:{8,2}} # Values can be Dict and List and Tuple
keys1 = {(1,2):1, (1,2):2 ,(1,2):3} # Keys can not be Dict and List

print(len(values1)) #O/P = 3 # When Key is unique then record considered as a single Pair
print(values1.values())
print(values1.keys())
print(values1.items())

values2 = {1:(1,2),1:[2,5],3:{8,2}}
print(len(values2)) #O/P = 2 # When Key is not unique then duplicate record considered as a single Pair
print(values2[1]) # if Key is not unique i.e. duplicate then it will give u recent output

for x,y in values1.items():
    if y == {8,2}:
        print(x)

for x,y in values1.items():
        print("Keys & Values : ",x,y)

for x in values1.keys():
        print("Keys : ",x)

for x in values1.values():
        print("Values : ",x)