# _*_ coding: utf-8 _*_
# @Time: 29.08.2024 14:26
# @Author: Qi Wang
# @File: 128___del__
# @Project: python_unittest
# @Quelle: https://www.youtube.com/watch?v=aHRb8RoX9vI&list=PLFbd8KZNbe-_PWBT_L7V6fNYJOgER0ZlR&index=113

class Demo:
    def __init__(self, name):
        print('我是__init__，我被调用了')
        self.name = name
    def __del__(self):
        print(f'{self.name}没了，给他处理后事') # 所有程序执行完再最终执行这条命令

a = Demo('a')

b = Demo('b')
del a # 删除，销毁对象
print('Process is over')

