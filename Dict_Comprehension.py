keys = ['a', 'b', 'c', 'd', 'e']
values = [1, 2, 3, 4, 5]

# 1st Way :
abc = {p:q**2 for p,q in zip(keys,values)}
print(abc)

# 2nd Way :
abc = {p:p**2 for p in values}
print(abc)

# 3rd Way :
abc = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(abc)