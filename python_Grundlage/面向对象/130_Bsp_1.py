# _*_ coding: utf-8 _*_
# @Time: 29.08.2024 14:39
# @Author: Qi Wang
# @File: 130_Bsp_1
# @Project: python_unittest
# @Quelle: https://www.youtube.com/watch?v=aHRb8RoX9vI&list=PLFbd8KZNbe-_PWBT_L7V6fNYJOgER0ZlR&index=113

class Person:
    def __init__(self, name, weight): # 创建对象后给对象添加属性
        self.name = name
        self.weight = weight

    def __str__(self):
        return f'name: {self.name}, weight: {self.weight} kg'

    def run(self):
        print(f'{self.name} has run 5 km, he has lost weight')
        # 减肥， 即修改属性
        self.weight -= 0.5

    def eat(self):
        print(f'{self.name} eats a lot, he has gained weight')
        self.weight += 1

Jack = Person('Jack', 75)
print(Jack)
Jack.run()
print(Jack)
Jack.eat()
print(Jack)
# print(dir(Jack)) # 显示该对象的所有方法