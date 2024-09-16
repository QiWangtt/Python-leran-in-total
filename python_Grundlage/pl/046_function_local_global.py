# _*_ coding: utf-8 _*_
# @Time: 26.08.2024 15:39
# @Author: Qi Wang
# @File: 046_function_local_global
# @Project: python_unittest

# def f1():
#     # local, in function
#     a = 1
#     print(a)
#
# f1()
# # print(a) # error

a = 1
print(a)


def f1():
    print(a)


f1()

# local is preferred if possible
