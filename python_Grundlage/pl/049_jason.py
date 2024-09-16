# _*_ coding: utf-8 _*_
# @Time: 27.08.2024 09:06
# @Author: Qi Wang
# @File: 049_jason
# @Project: python_unittest


# fp = open('test.txt', 'w')
# fp.write('hello world')
# fp.close()

# fp = open('test.txt', 'w')
# name_list = ['rsg','er']
# fp.write(name_list)
# fp.write(''.join(name_list))


# 序列化的两种方式
# dumps()
fp = open('test.txt', 'w')
# def a list
name_list = ['rsg','er']
import json

# 序列化
# 将python对象变成json字符串
# used for scrapy frame
names = json.dumps(name_list)

print(names)
print(type(names))
print(type(name_list))

# 将names写入文件中
fp.write(names)
fp.close()







