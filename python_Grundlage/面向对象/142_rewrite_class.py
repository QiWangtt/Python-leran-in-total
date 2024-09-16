# _*_ coding: utf-8 _*_
# @Time: 05.09.2024 12:46
# @Author: Qi Wang
# @File: 142_rewrite_class
# @Project: python_unittest
# @Quelle: https://www.youtube.com/watch?v=aHRb8RoX9vI&list=PLFbd8KZNbe-_PWBT_L7V6fNYJOgER0ZlR&index=113

'''class Dog:
    def bark(self):
        print('汪汪汪')


class XTQ(Dog):
    # XTQ类bark方法不再是汪汪汪叫，改为嗷嗷嗷叫
    def bark(self):
        print('嗷嗷嗷')  # 覆盖式重写

xtq = XTQ()
xtq.bark()
'''


# 扩展式改写
class Dog:
    def bark(self):
        print('汪汪汪')
        print('汪汪汪')
        print('汪汪汪')
        print('汪汪汪')


class XTQ(Dog):
    # XTQ类bark方法不再是汪汪汪叫，改为
    # 1. 先嗷嗷嗷叫（新功能） 2. 汪汪汪叫（父类中功能） 3. 嗷嗷嗷叫（新功能）
    def bark(self):
        print('嗷嗷嗷')
        # 在中间调用父类中的代码
        super().bark()
        print('嗷嗷嗷')

xtq = XTQ()
xtq.bark()




