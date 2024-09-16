# _*_ coding: utf-8 _*_
# @Time: 02.09.2024 14:52
# @Author: Qi Wang
# @File: 135_Bsp_HouseItem
# @Project: python_unittest
# @Quelle: https://www.youtube.com/watch?v=aHRb8RoX9vI&list=PLFbd8KZNbe-_PWBT_L7V6fNYJOgER0ZlR&index=113

# class für HouseItem definieren
class HouseItem:
    """家具类"""
    def __init__(self, name, area):
        """添加属性的方法"""
        self.name = name
        self.area = area

    def __str__(self):
        return f'ItemName: {self.name}, Area: {self.area} square meters'


class House:
    def __init__(self, name, area):
        self.name = name  # 户型
        self.total_area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return (f'Name: {self.name}, total area: {self.total_area} m2, free area: {self.free_area} m2, '
                f'ItemList: {self.item_list}')

    def add_item(self, item): # item表示家具的对象
        # 判断房子剩余面积和家具占地面积之间的关系
        # self表示的房子对象， 缺少一个家具对象使用传参解决
        if self.free_area > item.area:
            # 添加家具---->向列表中添加数据
            self.item_list.append(item.name)
            # 修改剩余面积
            self.free_area -= item.area
            print(f'{item.name}添加成功')
        else:
            print('剩余面积不足， 换个大房子')



# 创建家具对象
bed = HouseItem('席梦思', 4)
chest = HouseItem('衣柜', 2)
table = HouseItem('餐桌', 1.5)
print(bed)
print(chest)
print(table)

# 创建房子对象
house = House('big house', 169)
print(house)

# 添加床
house.add_item(bed)
print(house)
house.add_item(chest)
print(house)
house.add_item(table)
print(house)