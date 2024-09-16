# _*_ coding: utf-8 _*_
# @Time: 29.08.2024 14:39
# @Author: Qi Wang
# @File: 134_Bsp_3
# @Project: python_unittest
# @Quelle: https://www.youtube.com/watch?v=aHRb8RoX9vI&list=PLFbd8KZNbe-_PWBT_L7V6fNYJOgER0ZlR&index=113

class Student:
    def __init__(self, age, name):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age} years old'

    def eat(self):
        print(f'{self.name} 要吃饭')

    def sleep(self):
        print(f'{self.name} 要睡觉')

    def year(self):
        self.age += 1

# class definieren
Jack = Student(19, 'Jack')
Rose = Student(18, 'Rose')
print(Jack)
print(Rose)
Jack.eat()
Jack.sleep()
Jack.year()
print(Jack)

