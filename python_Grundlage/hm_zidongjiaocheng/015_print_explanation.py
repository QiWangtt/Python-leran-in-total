# _*_ coding: utf-8 _*_
# @Time: 28.08.2024 15:55
# @Author: Qi Wang
# @File: 015_print_explanation
# @Project: python_unittest

# end='\n', 每一个print结束都会打印的内容，结束符，换行
# 如果不想换行, 在打印的内容后面加end=''
print(1, end='')
print(2, end='')
print(3)
print(4)
print(5)

# sep='', 多个位置参数之间的间隔
print(1, 2, 3, 4, 5, 6)  # print默认间隔为空格
# 如果想修改间隔符号， 使用sep
print(1, 2, 3, 4, 5, 6, sep='_')
print(1, 2, 3, 4, 5, 6, sep=' 狗屁 ')
