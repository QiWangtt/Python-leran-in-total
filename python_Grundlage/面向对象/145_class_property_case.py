# _*_ coding: utf-8 _*_
# @Time: 05.09.2024 13:35
# @Author: Qi Wang
# @File: 145_class_property_case
# @Project: python_unittest
# @Quelle: https://www.youtube.com/watch?v=aHRb8RoX9vI&list=PLFbd8KZNbe-_PWBT_L7V6fNYJOgER0ZlR&index=113

class Dog:
    # 定义类属性
    count = 0
    # 定义实例属性，在init方法中
    def __init__(self, name):
        self.name = name  # 实例属性
        # 因为每创建一个对象就会调用init方法，就将个数加1的操作，写在init方法中
        Dog.count += 1

# 在类外部
# 打印输出目前创建了几个对象
print(Dog.count)
# 创建一个对象
dog1 = Dog('Bob')
# 打印输出目前创建了几个对象
print(Dog.count)

dog2 = Dog  # 不是创建对象，个数不会变
dog3 = dog1  # 不是创建对象，个数不会变
print(Dog.count)

dog4 = Dog('Jack')
print(Dog.count)
dog5 = Dog('Lambda')
print(Dog.count)

print(dog1.count)
print(dog4.count)
print(dog5.count)