# _*_ coding: utf-8 _*_
# @Time: 27.08.2024 13:03
# @Author: Qi Wang
# @File: 015_函数的嵌套调用
# @Project: python_unittest

def func1():
    print(1)
    print('func1')
    print(2)

def func2():
    print('3')
    func1()
    print('4')

print(5)
func2()
print(6)
