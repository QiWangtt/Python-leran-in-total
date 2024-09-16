# _*_ coding: utf-8 _*_
# @Time: 02.09.2024 14:20
# @Author: Qi Wang
# @File: 134_Bsp_4
# @Project: python_unittest
# @Quelle: https://www.youtube.com/watch?v=aHRb8RoX9vI&list=PLFbd8KZNbe-_PWBT_L7V6fNYJOgER0ZlR&index=113

class Computer:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def play_movie(self, movie):
        print(f'{self.brand} plays {movie}')

# class definieren
mi = Computer('xiaomi', 4999)
mac = Computer('mac', 16999)
mi.play_movie('葫芦娃')
mac.play_movie('变形金刚')
mi.play_movie('西游记')


