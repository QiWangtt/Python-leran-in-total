# _*_ coding: utf-8 _*_
# @Time: 29.08.2024 09:31
# @Author: Qi Wang
# @File: 113_sum
# @Project: python_unittest
# Quelle: https://www.youtube.com/watch?v=aHRb8RoX9vI&list=PLFbd8KZNbe-_PWBT_L7V6fNYJOgER0ZlR&index=113

def my_sum(*args, **kwargs):
    num = 0
    for i in args:
        num += i

    for j in kwargs.values():
        num += j

    print(num)

# 需求 my_list = [1,2,3,4], my_dict) = {'a':1, 'b':2, 'c':3, 'd':4}
my_list = [1,2,3,4]
my_dict = {'a':1, 'b':2, 'c':3, 'd':4}
# 将字典和列表中的数据使用my_sum函数进行求和， 该如何传参
# my_sum(1,2,3,4)
my_sum(a=1, b=2, c=3, d=4)
# 想要将列表(and Tuple)中的数据分别作为位置参数进行传参，需要对列表进行拆包操作， 需要在list前面加*
my_sum(*my_list)
# 想要将字典中的数据作为关键字传参，需要使用**对字典进行拆包
my_sum(**my_dict) # my_sum(a=1, b=2, c=3, d=4)

