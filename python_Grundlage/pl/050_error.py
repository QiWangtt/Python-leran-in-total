# _*_ coding: utf-8 _*_
# @Time: 27.08.2024 09:29
# @Author: Qi Wang
# @File: 050_error
# @Project: python_unittest

# fp = open('text.txt', 'r')
# fp.read()
# fp.close()

try:
    fp = open('text.txt', 'r')
    fp.read()
except FileNotFoundError:
    print('Maintainance')
