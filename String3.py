# The split() breaks the string at the separator and returns a list of strings.
text1 = 'Python is Great'
print(text1.split()) # ['Python', 'is', 'Great']
text2 = 'Python, is, Great'
print(text2.split()) # ['Python,', 'is,', 'Great']
print(text2.split(',')) # ['Python', ' is', ' Great']
print(text2.split(':')) # ['Python, is, Great']
print(len(text2.split(':'))) # ['Python, is, Great']
# -------------
# split with maxsplit
print("maxsplit 2(Splits = 0,1,2) -",text2.split(', ', 2)) # ['Python', 'is', 'Great']
print("maxsplit 1(Splits = 0,1) -",text2.split(', ', 1)) # ['Python', 'is, Great']
print("maxsplit 5(Splits = 0,1,2,3,4) -",text2.split(', ', 5)) # ['Python', 'is', 'Great']
print("maxsplit 0(Splits = 0) -",text2.split(', ', 0)) # ['Python, is, Great']
# ----------------------------------------------------
# rsplit() - Split from Right Side
# rsplit(), When maxsplit is not specified, the rsplit() behaves like split().
print(text2.rsplit()) # ['Python,', 'is,', 'Great']
print(text2.rsplit(',')) # ['Python', ' is', ' Great']
print(text2.rsplit(':')) # ['Python, is, Great'] # Single Element
# rsplit with maxsplit
print("maxsplit 2(rSplits = 0,1,2) -",text2.rsplit(', ', 2)) # ['Python', 'is', 'Great']
print("maxsplit 1(rSplits = 0,1) -",text2.rsplit(', ', 1)) # ['Python, is', 'Great']
print("maxsplit 5(rSplits = 0,1,2,3,4) -",text2.rsplit(', ', 5)) # ['Python', 'is', 'Great']
print("maxsplit 0(rSplits = 0) -",text2.rsplit(', ', 0)) # ['Python, is, Great']
# ----------------------------------------------------
# splitlines()
grocery = 'Milk\nChicken\r\nBread\rButter\vMilk\fChicken\x1cBread\x1dButter'
print(grocery.splitlines())
print(grocery.splitlines(True))
grocery = 'Milk Chicken Bread Butter'
print(grocery.splitlines())
# ----------------------------------------------------
# startswith(), This is casesensative
print(text1.startswith('is great'))# returns False
print(text1.startswith('Python is '))# returns True, default is 0 start position and last position is end.
print(text1.startswith('Python is', 0)) # returns True
print(text1.startswith('Python is', 0, 9)) # True with 9 or more, False with less than 9

# startswith() With Tuple
print(text1.startswith(('java', 'python', 'programming'))) # False as python..not Python
print(text1.startswith(('is', 'was'), 7, 19)) # True because is at 7 position
# ----------------------------------------------------
# title() - 1st character will be capitilzed
text = 'My favorite number is 25.'
print(text.title())
text = '234 5kw3l2ab *43 fun'
print(text.title())
text = "He's an engineer, isn't he?"
print(text.title())
# ----------------------------------------------------
# format_map()
point = {'x':4,'y':-5, 'z': 0}
print('{x} {y} {z}'.format_map(point))

class Coordinate(dict):
    def __missing__(self, key):
      return key
print('({x}, {y})'.format_map(Coordinate(x='6')))
print('({x}, {y})'.format_map(Coordinate(y='5')))
print('({x}, {y})'.format_map(Coordinate(x='6', y='5')))
# ----------------------------------------------------