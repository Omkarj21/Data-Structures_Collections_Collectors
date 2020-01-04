# fromkeys()
keys = {'a', 'e', 'i', 'o', 'u' }
value = 'vowel'
vowels = dict.fromkeys(keys, value)
print(vowels)
# ----------------------------------------------------
# setdefault() = when key is in the dictionary
person = {'name': 'Omkar', 'age': 27}
age = person.setdefault('age')
print('person = ',person)
print('Age = ',age)
# ----------------------------------------------------
# setdefault() = when key is not in the dictionary and default_value is provided
person = {'name': 'Omkar'}
emp_id = person.setdefault('emp_id')
print('person = ',person)
print('emp_id = ',emp_id)
age = person.setdefault('age', 27)
print('person = ',person)
print('age = ',age)
# ----------------------------------------------------