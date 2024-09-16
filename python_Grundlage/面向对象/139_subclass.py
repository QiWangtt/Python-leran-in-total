# _*_ coding: utf-8 _*_
# @Time: 05.09.2024 12:23
# @Author: Qi Wang
# @File: 139_subclass
# @Project: python_unittest
# @Quelle: https://www.youtube.com/watch?v=aHRb8RoX9vI&list=PLFbd8KZNbe-_PWBT_L7V6fNYJOgER0ZlR&index=113

class Animal:
    def eat(self):
        print('eat')


class Dog(Animal):
    def bark(self):
        print('bark')


class XTQ(Dog):
    pass

dog = Dog()  # 实例对象，实例化， 平时说的对象都是实例对象
dog.eat()  # 调用父类的方法
dog.bark()

xtq = XTQ()
xtq.bark()  # 调用父类方法
xtq.eat()  # 调用父类的父类公有方法， 就是继承。 但是私有方法不可调用
