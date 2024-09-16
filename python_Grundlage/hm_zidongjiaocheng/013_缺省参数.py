# _*_ coding: utf-8 _*_
# @Time: 28.08.2024 15:34
# @Author: Qi Wang
# @File: 013_缺省参数
# @Project: python_unittest

def show_info(name, gender='secret'):
    print(name, gender)

#  if no input, default value would be used
show_info('Jack')
# if input, the input would be used
show_info('Jack', 'male')