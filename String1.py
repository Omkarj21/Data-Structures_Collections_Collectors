# capitalize() => function returns a string with first letter capitalized and all other characters lowercased.
# It doesn't modify the original string.
text = "india is GREAT"
print('Old String: ', text) # india is GREAT
print('Capitalized String:', text.capitalize()) # India is GREAT
# --------------------------------------------------
print("Endswith_1",text.endswith('GREAT'))
print("Endswith_2",text.endswith('is',5,20)) # TRUE if 'is' should be at 20th position else FALSE
print("Endswith_3",text.endswith(('Omkar', 'Jadhav', 'GREAT'))) # if GREAT wasnt present then FALSE
# --------------------------------------------------
print("Startswith_1",text.startswith('India'))
print("Startswith_2",text.startswith('is',6,20)) # TRUE if 'is' should be at 6th position else FALSE
print("Startswith_3",text.startswith(('india', 'Jadhav', 'GREAT'))) # if GREAT wasnt present then FALSE
# --------------------------------------------------
# center(width, fillchar) =>
# width - length of the string with padded characters
# fillchar (optional) - padding character, If it's not provided, space is taken as default argument.
print("Center without fillchar :",text.center(50)) # No fillchar provided,
print("Center with fillchar :",text.center(50,'$')) # fillchar provided,
# output of above = $$$$$$$$$$$$$$$$$India is great.$$$$$$$$$$$$$$$$$$ , whose length is 50
# --------------------------------------------------
# The casefold() method removes all case distinctions present in a string. It is used for caseless matching, i.e. ignores cases when comparing.
print("Lowercase using casefold():", text.casefold())
# German lowercase letter ß is equivalent to ss. However, since ß is already lowercase, lower() method does nothing to it. But, casefold() converts it to ss.
firstString = "der Fluß"
secondString = "der Fluss"
# ß is equivalent to ss
if firstString.casefold() == secondString.casefold():
    print('The strings are equal.')
else:
    print('The strings are not equal.')
# --------------------------------------------------
quote = 'Do small things with great love'
# Substring is searched in 'hings with great love'
print(quote.find('small things', 10))
# Substring is searched in ' small things with great love'
print(quote.find('small things', 2))
# Substring is searched in 'hings with great lov'
print(quote.find('o small ', 10, -1))
# Substring is searched in 'll things with'
print(quote.find('things ', 6, 20))
# --------------------------------------------------
# isalnum (), isalpha(), isdecimal(), isdigit(), isidentifier(), islower(), isnumeric()
name = "omkar"
print("isalnum",name.isalnum()) # True
print("isalpha",name.isalpha()) # True
print("isdecimal",name.isdecimal()) # False
print("isdigit",name.isdigit()) # False
print("isidentifier",name.isidentifier()) # True
print("islower",name.islower()) # True
print("isnumeric",name.isnumeric()) # True
print("isupper",name.isupper()) # False
name = "Omkar Jadhav "
print("isalnum",name.isalnum()) # False
print("isalpha",name.isalpha()) # False
print("isdecimal",name.isdecimal()) # False
print("isdigit",name.isdigit()) # False
print("isidentifier",name.isidentifier()) # False
print("islower",name.islower()) # False
print("isnumeric",name.isnumeric()) # False
print("isupper",name.isupper()) # False
name = "omkar007jadhav"
print("isalnum",name.isalnum()) # True
print("isalpha",name.isalpha()) # False
print("isdecimal",name.isdecimal()) # False
print("isdigit",name.isdigit()) # False
print("isidentifier",name.isidentifier()) # True
print("islower",name.islower()) # True
print("isnumeric",name.isnumeric()) # True
print("isupper",name.isupper()) # False
name = "007"
print("isalnum",name.isalnum()) # True
print("isalpha",name.isalpha()) # False
print("isdecimal",name.isdecimal()) # True
print("isdigit",name.isdigit()) # True
print("isidentifier",name.isidentifier()) # False
print("islower",name.islower()) # False
print("isnumeric",name.isnumeric()) # False
print("isupper",name.isupper()) # False
text1 = ' '
print("isidentifier with space",text1.isidentifier()) # False
text2 = "OMKAR"
print("isupper",text2.isupper()) # True