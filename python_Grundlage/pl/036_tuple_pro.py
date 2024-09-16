# _*_ coding: utf-8 _*_
# @Time: 26.08.2024 13:36
# @Author: Qi Wang
# @File: 036_tuple_pro
# @Project: python_unittest

'''a_tuple = (1, 2, 3, 4, 5)
print(a_tuple[0])
print(a_tuple[1])'''

# The elements in a Tuple can't be changed
# a_tuple[3] = 5
# print(a_tuple)

'''a_list = [1, 2, 3, 4, 5]
print(a_list[0])
# The elements in a list can be changed
a_list[3] = 5
print(a_list)'''

# If there is only one element in tuple, the element will be int
a_tuple= (5)
print(type(a_tuple))
# There must be a comma after the only element, if you want it be a tuple
a_tuple= (5,)
print(type(a_tuple))


