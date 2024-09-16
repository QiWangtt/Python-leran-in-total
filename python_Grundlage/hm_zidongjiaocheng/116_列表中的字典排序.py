# _*_ coding: utf-8 _*_
# @Time: 29.08.2024 10:15
# @Author: Qi Wang
# @File: 116_列表中的字典排序
# @Project: python_unittest
# Quelle: https://www.youtube.com/watch?v=aHRb8RoX9vI&list=PLFbd8KZNbe-_PWBT_L7V6fNYJOgER0ZlR&index=113

user_list = [
    {'name': 'Jack', 'age': 18},
    {'name': 'Rose', 'age': 23},
    {'name': 'Bob', 'age': 28},
]

user_list.sort(key=lambda x: x['name']) # sort by name
print('Sort by name: ', user_list)

user_list.sort(key=lambda x: x['age']) # sort by age
print('Sort by age ascent: ', user_list)

user_list.sort(key=lambda x: x['age'], reverse=True)
print('Sort by age descent: ', user_list)
