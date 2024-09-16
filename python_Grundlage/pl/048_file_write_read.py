# _*_ coding: utf-8 _*_
# @Time: 26.08.2024 16:06
# @Author: Qi Wang
# @File: 048_file_write_read
# @Project: python_unittest
# If file exists, it will be cleared at first, then write new info
# fp = open('test.txt', 'w')
# fp.write('hello world, I am here\n' * 5)
# fp.close()
#
#
# # appending, mode: a
# fp = open('test.txt', 'a')
# fp.write('hello world, I am here\n' * 5)
# fp.close()

# read
fp = open('test.txt', 'r')
# default, read efficiency is too low
# content = fp.read()
# print(content)

# readline is higher
# contents = fp.readline()
# print(contents)

# readlines high, but output is in form of list
contents = fp.readlines()
print(contents)