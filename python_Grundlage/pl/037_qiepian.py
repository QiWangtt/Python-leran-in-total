# _*_ coding: utf-8 _*_
# @Time: 26.08.2024 13:46
# @Author: Qi Wang
# @File: 037_qiepian
# @Project: python_unittest

s = 'hello world'
print(s[0])
# 左闭右开区间
print(s[0:4])

print(s[1:])
print(s[:4]) # eqaul to print(s[0:4])
# from index 0 to 6, step = 2
print(s[0:6:2])