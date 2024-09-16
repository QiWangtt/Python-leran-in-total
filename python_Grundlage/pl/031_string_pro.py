# _*_ coding: utf-8 _*_
# @Time: 26.08.2024 12:40
# @Author: Qi Wang
# @File: 031_string_pro
# @Project: python_unittest
# len: length
s = 'Deutschland'
print(len(s))
print(f'Wo ist c? {s.find('c')}')
print(s.startswith('D'))
print(s.endswith('d'))
s1 = 'aaaabbbbbb'
print(s1.count('a'))
print(s1.count('b'))
print(s1.replace('b','a'))

s2 = '1#2#3#4#5#6#7#8'
print(s2.split('#'))

s3 = 'Deutschland'
print(s3.upper())
print(s3.lower())

s4 = '  a  fff  '
print(len(s4))
print(s4.strip())
print(len(s4.strip()))

s5 = 'a'
print(s5.join('Hello'))