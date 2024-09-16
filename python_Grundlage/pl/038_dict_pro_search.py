# _*_ coding: utf-8 _*_
# @Time: 26.08.2024 13:55
# @Author: Qi Wang
# @File: 038_dict_pro_search
# @Project: python_unittest

person = {'name': 'Jack', 'age': 25}
print(person['name'])
print(person['age'])

'''# keyerror, because 'gender doesn't exist'
print(person['gender'])

# also doesn't work
print(person.name)'''

print(person.get('name'))
print(person.get('age'))

# a 'None' will be returned
print(person.get('gender'))