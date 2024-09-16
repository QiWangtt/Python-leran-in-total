# _*_ coding: utf-8 _*_
# @Time: 26.08.2024 14:11
# @Author: Qi Wang
# @File: 041_dict_pro_delete
# @Project: python_unittest

'''# del
person = {'name': 'Jack', 'age': 28}
print('before delete age: ', end='')
print(person)

del person['age']
print('after delete age: ', end='')
print(person)

person = {'name': 'Jack', 'age': 28}
print('before delete person: ', end='')
del person
print(person)'''

# clear: delete elements, but dict(ionary) remains staying
person = {'name': 'Jack', 'age': 28}
print('before clear person: ', end='')
print(person)

person.clear()
print('after clear person: ', end='')
print(person)