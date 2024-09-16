# _*_ coding: utf-8 _*_
# @Time: 29.08.2024 13:26
# @Author: Qi Wang
# @File: 126___init___
# @Project: python_unittest
# @Quelle: https://www.youtube.com/watch?v=aHRb8RoX9vI&list=PLFbd8KZNbe-_PWBT_L7V6fNYJOgER0ZlR&index=113

class Cat:
    # 定义添加属性的方法
    def __init__(self, name, age):  # 如果init方法中，存在出现了self之外的参数，在创建对象时必须传参
        self.name = name
        self.age = age

    # 输出属性信息
    def show_info(self):
        print('The cat\'s name is {}, age is {}'.format(self.name, self.age))

# 创建对象不要在class的缩进中创建
# Cat()  # 创建对象，会输出
blue_cat = Cat('blue_cat', 2)  # 创建对象，会输出

blue = blue_cat  # 不是创建对象，不会输出
blue.show_info()

# 创建黑猫
black_cat = Cat('black_cat', 3)
black_cat.show_info()