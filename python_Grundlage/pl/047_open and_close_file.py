# _*_ coding: utf-8 _*_
# @Time: 26.08.2024 15:47
# @Author: Qi Wang
# @File: 047_open and_close_file
# @Project: python_unittest

'''# open(filepath, mode)
# mode: w: writable
#       r: readable
open('text.txt', 'w')'''

# open file
# fp = open('text.txt', 'w')
# fp.write('hello world')

# folder can't be created automatically if it doesn't exist, it must be done manually
fp = open('demo/text.txt', 'w')
fp.write('hello world')

# close file
fp = open('demo/a.txt','w')
fp.write('hello world')
fp.close()