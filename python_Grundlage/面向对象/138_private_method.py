# _*_ coding: utf-8 _*_
# @Time: 05.09.2024 11:08
# @Author: Qi Wang
# @File: 138_private_method
# @Project: python_unittest
# @Quelle: https://www.youtube.com/watch?v=aHRb8RoX9vI&list=PLFbd8KZNbe-_PWBT_L7V6fNYJOgER0ZlR&index=113

# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f'{self.name} is {self.age} years old'
#
# Jack = Person('Jack', 25)
# print(Jack)
#
# # 在class的外部直接访问age属性
# print(Jack.age)
# # 外部直接修改age属性
# Jack.age = 18
# print(Jack)

class Person():
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 将其定义为私有属性，属性名前加上两个"_"
        # 私有的本质，是python解释器执行代码，发现属性名或者方法名前面有两个_， 会将这个名字重命名
        # 会在这个名字的前面加上 _类明前缀， 即self.__age ===> self._Person__age
    def __str__(self): # 在class内部是可以访问私有属性的
        return f'{self.name} is {self.__age} years old'

Jack = Person('Jack', 25)
print(Jack)

# 在class的外部直接访问age属性会报错，不能直接使用私有属性
# print(Jack.__age)

print(Jack.__dict__)
# 外部直接修改age属性不报错
Jack.__age = 18  # 这个其实是添加了一个公有属性
# 但是下面print不会显示修改后的age
print(Jack)
print(Jack._Person__age) # 能用，但是不要用
Jack._Person__age = 19
print(Jack)

# 补充
# 对象.__dict__  魔法属性，可以将对象具有的属性组成字典返回
print(Jack.__dict__)

