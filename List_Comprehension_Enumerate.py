# Normal For loop
h_letters = []
for letter in 'human':
    h_letters.append(letter)
print("Normal :" ,h_letters)

# List Comprehension
h_letters = [ letter for letter in 'human' ]
print("List Comprehension :", h_letters)
# -------------------------------------------------------------------------------------
##### In Memory Management and execution time frame, List Comprension is better

# Lambda
letters = list(map(lambda x: x, 'human'))
print("Lambda :",letters)

# Conditions in List Comprehension
number_list = [ x for x in range(20+1) if x % 2 == 0]
print("Conditions in List Comprehension :",number_list)

num_list = [y for y in range(100) if y % 2 == 0  if y % 5 == 0]
print("Nested IF in List Comprehension :",num_list)

obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
print("If Else in List Comprehension :",obj)

# Use of enumerate to fetch element with its index
x = [7,2,4,9,1]
for index,item in enumerate(x):
    print("Enumerate for Element with Index : ",index,item)
# -------------------------------------------------------------------------------------