# _*_ coding: utf-8 _*_
# @Time: 25.09.2024 14:58
# @Author: Qi Wang
# @File: async def
# @Project: Python
# @Quelle: https://blog.csdn.net/weixin_43915090/article/details/136659735

import asyncio

# 使用def定义的同步函数
def regular_function():
    return "Hello from a regular function!"

# 使用async def定义的异步函数
async def async_function():
    await asyncio.sleep(1)  # 这是一个异步操作
    print("1")
    await asyncio.sleep(1)  # 这是一个异步操作
    print("2")
    await asyncio.sleep(1)  # 这是一个异步操作
    print("3")
    await asyncio.sleep(1)  # 这是一个异步操作
    print("4")
    await asyncio.sleep(1)  # 这是一个异步操作
    print("5")
    await asyncio.sleep(1)  # 这是一个异步操作
    print("6")
    await asyncio.sleep(1)  # 这是一个异步操作
    return "Hello from an async function after 6 second!"

# 调用同步函数
print(regular_function())

# 调用异步函数
# 这是错误的：print(async_function())  # 这会返回一个协程对象，而不是我们期望的字符串
# 正确的调用方式如下：
print(asyncio.run(async_function()))

