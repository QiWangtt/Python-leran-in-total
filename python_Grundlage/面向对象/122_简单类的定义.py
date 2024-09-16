# _*_ coding: utf-8 _*_
# @Time: 29.08.2024 12:36
# @Author: Qi Wang
# @File: 122_简单类的定义
# @Project: python_unittest
# Quelle: https://www.youtube.com/watch?v=aHRb8RoX9vI&list=PLFbd8KZNbe-_PWBT_L7V6fNYJOgER0ZlR&index=113


# 需求 小猫爱吃鱼， 小猫要喝水，定义不带属性的类
class Cat:
    # 1 在缩进中书写方法
    def eat(self):
        print('小猫爱吃鱼....')

    def drink(self):
        print('小猫要喝水----')

# 2 创建对象
blue_cat = Cat()


# 3 通过对象调用类中的方法
print('blue_cat')
blue_cat.eat()
blue_cat.drink()

# 创建对象
black_cat = Cat()
print('black_cat')
black_cat.eat()
black_cat.drink()


