# _*_ coding: utf-8 _*_
# @Time: 28.08.2024 15:28
# @Author: Qi Wang
# @File: 011_return_multivalues
# @Project: python_unittest

def calc(a, b):
    num = a + b
    num1 = a - b
    return num, num1

result = calc(10, 5)
print(result, result[0], result[1])
print()

# 直接拆包
x, y = calc(10, 5)
print(x, y)