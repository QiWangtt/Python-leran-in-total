# _*_ coding: utf-8 _*_
# @Time: 28.08.2024 15:44
# @Author: Qi Wang
# @File: 014_不定长参数_args
# @Project: python_unittest

def func(*args, **kwargs):
    print(type(args), args)
    print(type(kwargs), kwargs)
    print('-' * 30)

func()
# 位置传参，数据都给args
func(1, 2, 3)
# 关键字传参，数据都给kwargs
func(a=1, b=2, c=3)
func(1, 2, 3, a=1, b=2, c=3)