# _*_ coding: utf-8 _*_
# @Time: 27.08.2024 15:33
# @Author: Qi Wang
# @File: 06_quote
# @Project: python_unittest

a = 1 # 1 has benn saved in a
print('a: ', id(a))

b = a
print('b: ', id(b))  # the same as id(a)

a = 10
print('a: ', id(a))
print('b: ', id(b))