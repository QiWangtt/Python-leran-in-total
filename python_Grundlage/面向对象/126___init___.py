# _*_ coding: utf-8 _*_
# @Time: 29.08.2024 13:26
# @Author: Qi Wang
# @File: 126___init___
# @Project: python_unittest
# @Quelle: https://www.youtube.com/watch?v=aHRb8RoX9vI&list=PLFbd8KZNbe-_PWBT_L7V6fNYJOgER0ZlR&index=113

class Cat:
    # 定义添加属性的方法，所有魔法方法都是以__开头和结尾
    def __init__(self):  # 这个方法是创建对象之后才调用
        self.name = 'blue_cat'
        self.age = 2
        # 下方代码只是为了验证该方法被调用了，实际代码不要书写
        print('我是__init__，我被调用了')
    # 输出属性信息
    def show_info(self):
        print('The name is {}, age is {}'.format(self.name, self.age))

# 创建对象不要在class的缩进中创建
Cat()  # 创建对象，会输出
blue_cat = Cat()  # 创建对象，会输出
blue = blue_cat  # 不是创建对象，不会输出
blue.show_info()

# 创建黑猫
black_cat = Cat()
black_cat.show_info()