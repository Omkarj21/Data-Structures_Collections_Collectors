# isprintable
text = 'India is Great'
print(text.isprintable())  # True
text = '\nIndia is Great'
print(text.isprintable())  # False
text = ''  # or s = ' ',
print('\nEmpty string =', text.isprintable())  # True
# -----------------------------------------------
# istitle
s = 'Python Is Good.'
print(s.istitle())  # True
s = 'Python is good'
print(s.istitle())  # False
# -----------------------------------------------
# ljust(), rjust()
print(s.ljust(20, '*'))
print(s.rjust(20, '*'))
# -----------------------------------------------
# swapcase()
string = "THIS SHOULD ALL BE LOWERCASE."
print(string.swapcase())
string = "this should all be uppercase."
print(string.swapcase())
string = "ThIs ShOuLd Be MiXeD cAsEd."
print(string.swapcase())
# -----------------------------------------------
# lstrip(), rstrip(), strip
text1 = '   India is Great   '
text2 = 'Python is Awesome'
print(text1.lstrip())  # Leading whitepsace are removed
print(text2.lstrip('Pytho'))
print(text1.rstrip())  # Trailing whitepsace are removed
print(text2.rstrip('some'))
print(text1.strip())  # All whitepsace are removed
print(text2.strip('p'))  # will not work as casesensetive
print(text2.strip('P'))  # will work
print(text2.strip('ome'))  # will work
# -----------------------------------------------
# partition()
text3 = "Python is Awesome, isn't it"
# 'is' separator is found
print(text3.partition('is '))
# 'not' separator is not found
print(text3.partition('not'))
# -----------------------------------------------
# replace()
text4 = text3.replace("isn't it", "Yes! It is")
text5 = text3.replace("is", "Omkar", 1)
print(text4)
print(text5)
# -----------------------------------------------
# rfind()
# If substring exists inside the string, it returns the highest index where substring is found.
# If substring doesn't exist inside the string, it returns -1.
quote = 'Let it be, let it be, let it be'
result = quote.rfind('small')
print("Substring 'small ':", result) # Substring 'small ': -1
result = quote.rfind('be,')
if result != -1:
    print("Highest index where 'be,' occurs:", result) # Highest index where 'be,' occurs: 18
else:
    print("Doesn't contain substring")
# -----------------------------------------------
quote = 'Do small things with great love'
# Substring is searched in 'hings with great love'
print(quote.rfind('things', 10)) #  output is -1, beacuse not found, here 10 is start position
# Substring is searched in ' small things with great love'
print(quote.rfind('t', 2)) # output is 25th position, here 2 is start position
# Substring is searched in 'hings with great lov'
print(quote.rfind('o small ', 10, -1)) # here, -1 means remove last character and start position is 10, even output is -1
# Substring is searched in 'll things with'
print(quote.rfind('th', 6, 20)) # output is 18, here 6 is start position, 20 is last position
# -----------------------------------------------
# rindex()
# rfind() & rindex() = The only difference is that rfind() returns -1 if the substring is not found, whereas rindex() throws an exception.
quote = "Python is Awesome, isn't it"
result = quote.rindex('is')
print("Substring 'is':", result) # Substring 'is': 19
result = quote.rindex('omkar')
print("Substring 'omkar ':", result) # ValueError: substring not found
# -----------------------------------------------