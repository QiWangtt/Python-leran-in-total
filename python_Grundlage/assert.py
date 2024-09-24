# _*_ coding: utf-8 _*_
# @Time: 24.09.2024 09:59
# @Author: Qi Wang
# @File: assert
# @Project: Python
# @Quelle: https://blog.csdn.net/TeFuirnever/article/details/88883859
from typing import TypeVar, List,Generic
from pydantic.generics import GenericModel

assert 1 == 1, 'Something is going wrong'

T = TypeVar('   tztfrgthb', str, bytes)
print(T)

Data = TypeVar("Data")
print(Data)
data = List[Data]
print(data)

my_list_1: List[int] = [1, 'f', 3, 4]
print(my_list_1)
my_list_2= [1, 2, 3, 'a']
print(my_list_2)
my_list_1.append(8)
print(my_list_1)



T = TypeVar('T')


def first_element(items: List[T]) -> T:
    return items[0]


int_list = [1, 2, 3, 4, 5]
print(first_element(int_list))  # 输出: 1

str_list = [9, "Hello", "World", "Python"]
print(first_element(str_list))  # 输出: Hello


#
def add(x, y) -> int:
  return x+y

def add2(x: int, y: int) -> int:
  return x+y

print(add(4, 2))
print(add2(5, 4))





#
class ListModelPaginated(GenericModel, Generic[Data]):
    data: List[Data]
    total: int = 101
    offset: int = 0
    limit: int = 10
    # def get_value(self, key: str):
    #     if key in
    #     return

model = ListModelPaginated
model.limit = 15


