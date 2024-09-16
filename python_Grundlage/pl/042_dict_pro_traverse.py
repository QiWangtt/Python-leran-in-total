# _*_ coding: utf-8 _*_
# @Time: 26.08.2024 14:39
# @Author: Qi Wang
# @File: 042_dict_pro_traverse
# @Project: python_unittest

person = {'name': 'Jack', 'age': 28, 'city': 'New York'}
print(person.keys())
print(person.values())

# traverse keys of the dict
print('Keys: ')
for key in person.keys():
    print(key)
print()

# traverse values of the dict
print('values: ')
for value in person.values():
    print(value)
print()

# traverse keys and values of the dict
for key, value in person.items():
    print(key, value)
print()

# traverse items of the dict
for item in person.items():
    print(item)
