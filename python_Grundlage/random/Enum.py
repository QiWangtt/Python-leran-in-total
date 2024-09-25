# _*_ coding: utf-8 _*_
# @Time: 25.09.2024 15:28
# @Author: Qi Wang
# @File: Enum
# @Project: Python
# @Quelle: https://blog.csdn.net/weixin_45949073/article/details/116764198?ops_request_misc=%257B%2522request%255Fid%2522%253A%252242E72A79-B836-4156-A23D-802AF6C69DE7%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=42E72A79-B836-4156-A23D-802AF6C69DE7&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-2-116764198-null-null.142^v100^pc_search_result_base5&utm_term=python%20Enum&spm=1018.2226.3001.4187

# 导入枚举类
from enum import Enum


# 继承枚举类
class color(Enum):
    YELLOW = 1
    BEOWN = 1
    # 注意BROWN的值和YELLOW的值相同，这是允许的，此时的BROWN相当于YELLOW的别名
    RED = 2
    GREEN = 3
    PINK = 4


class color2(Enum):
    YELLOW = 1
    RED = 2
    GREEN = 3
    PINK = 4


print(color.YELLOW)  # color.YELLOW
print(type(color.YELLOW))  # <enum 'color'>

print(color.YELLOW.value)  # 1
print(type(color.YELLOW.value))  # <class 'int'>

print(color.YELLOW == 1)  # False
print(color.YELLOW.value == 1)  # True
print(color.YELLOW == color.YELLOW)  # True
print(color.YELLOW == color2.YELLOW)  # False
print(color.YELLOW is color2.YELLOW)  # False
print(color.YELLOW is color.YELLOW)  # True

print(color(1))  # color.YELLOW
print(type(color(1)))  # <enum 'color'>


class Hjx_Class_name(str, Enum):
    Name = 'huangjunx'
    Year = 18
    Id = '20153201072'
    student = True

print(Hjx_Class_name.Id.value)

print(color.YELLOW.value == color2.YELLOW.value)  # True