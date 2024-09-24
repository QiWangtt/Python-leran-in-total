# _*_ coding: utf-8 _*_
# @Time: 24.09.2024 13:46
# @Author: Qi Wang
# @File: Generic
# @Project: Python
# @Quelle: https://blog.csdn.net/book_dw5189/article/details/137212745?ops_request_misc=%257B%2522request%255Fid%2522%253A%25221AC52024-8DE6-4427-9E16-8B95254B74EC%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=1AC52024-8DE6-4427-9E16-8B95254B74EC&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-137212745-null-null.142^v100^pc_search_result_base5&utm_term=typing%20Generic&spm=1018.2226.3001.4187

from typing import TypeVar, Generic

# 定义一个泛型类型T
T = TypeVar('T')


class Storage(Generic[T]):
    def __init__(self, initial_value: T):
        self._value = initial_value

    def get_value(self) -> T:
        """获取存储的值"""
        return self._value

    def set_value(self, new_value: T) -> None:
        """设置新的值"""
        self._value = new_value


# 使用泛型类
int_storage = Storage(10)
print(int_storage.get_value())  # 输出: 10
int_storage.set_value(20)
print(int_storage.get_value())  # 输出: 20

str_storage = Storage("Hello")
print(str_storage.get_value())  # 输出: Hello
str_storage.set_value("World")
print(str_storage.get_value())  # 输出: World

str_storage = Storage(True)
print(str_storage.get_value())  # 输出: True
str_storage.set_value(False)
print(str_storage.get_value())  # 输出: False
