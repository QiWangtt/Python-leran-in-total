# _*_ coding: utf-8 _*_
# @Time: 26.08.2024 12:57
# @Author: Qi Wang
# @File: 032_list_pro
# @Project: python_unittest

# append: neu Element am Ende hinzufügen
food_list = ['Gurke','Tomaten']
print(food_list)

food_list.append('Kartoffel')
print(food_list)

# insert
char_list = ['a','c','d']
print(char_list)
char_list.insert(1,'b')
print(char_list)

# extend
num_list = [1,2,3]
num1_list = [4,5,6]

num_list.extend(num1_list)
print(num_list)