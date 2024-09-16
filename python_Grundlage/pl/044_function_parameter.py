# _*_ coding: utf-8 _*_
# @Time: 26.08.2024 15:21
# @Author: Qi Wang
# @File: 044_function_parameter
# @Project: python_unittest

# def sum():
#     a = 1
#     b = 2
#     c = a + b
#     print(c)
#
# sum()

# 定义函数时小括号中的参数为形参，用来接收参数
# 调用函数时小括号中的参数为实参，用来传递给函数
def sum(a, b):
    c = a + b
    print(f'{a} + {b} = {c}')

# position parameter
sum(2,16)
sum(156,264)

# keyword parameter
sum(b = 23, a = 56)