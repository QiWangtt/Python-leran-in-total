# _*_ coding: utf-8 _*_
# @Time: 29.08.2024 12:49
# @Author: Qi Wang
# @File: 123_self
# @Project: python_unittest
# @Quelle: https://www.youtube.com/watch?v=aHRb8RoX9vI&list=PLFbd8KZNbe-_PWBT_L7V6fNYJOgER0ZlR&index=113


# 需求 小猫爱吃鱼， 小猫要喝水，定义不带属性的类
class Cat:
    # 1 在缩进中书写方法
    def eat(self): # self本质是形参，函数中的局部变量
        print(f'{id(self)}, self')
        print('小猫爱吃鱼....')

    def drink(self):
        print('小猫要喝水----')

# 2 创建对象
blue_cat = Cat() # 该变量本质是全局变量
print(f'{id(blue_cat)}, blue_cat')

# 3 通过对象调用类中的方法
blue_cat.eat() # blue_cat对象调用eat方法，解释器就会将blue_cat对象传给self
print('-' * 30)

# 创建对象
black_cat = Cat()
print(f'{id(black_cat)}, black_cat')
black_cat.eat() # black_cat对象调用eat方法，解释器就会将black_cat对象传给self


