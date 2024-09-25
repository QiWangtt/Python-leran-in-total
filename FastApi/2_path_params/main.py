# _*_ coding: utf-8 _*_
# @Time: 09.09.2024 09:39
# @Author: Qi Wang
# @File: main
# @Project: FastApi learn
# @Quelle: https://www.youtube.com/watch?v=n6Xa6cokCKc&list=PLvQDgAXJ4ADP4G8Iuc02B11bvFokZMChK&index=2
from winreg import EnumKey

import uvicorn
from fastapi import FastAPI
from enum import Enum

app = FastAPI()


class Gender(str, Enum): # Enum是枚举
    male = "male"
    female = "female"
    diverse = "diverse"

# 对于@app.get，小范围在前，大范围在后， current是固定字符串，属于小范围
@app.get('/users/current')
async def get_current_user():
    return {'user': f'This is current user'}


@app.get('/users/{user_id}')
async def get_user(user_id: int):
    return {'user': f'This is the user for {user_id}'}


@app.get('/students/{gender}')
async def get_user(gender: Gender): # Gender 是上面定义的性别枚举类
    return {'student': f'This is a {gender.value} student'}


# 将参数item_id的类型定义为int类型
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


# 将参数item_name的类型定义为str类型
@app.get("/items/{item_name}")
def read_item(item_name: str):
    return {"item_id": item_name}
'''
当我们声明了路径参数的类型，如果我们在访问链接的时候提供的参数类型不对，
FastAPI还会自动为我们做数据校验的功能，在开发和调试与您的API交互的代码时，这非常有用。注意两点：

 :所有的数据验证都是由 Pydantic实现的.
 :你可以用同样的类型声明比如 str, float, bool 或者其他更复杂的类型.
————————————————

                            版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。
                        
原文链接：https://blog.csdn.net/my_name_is_learn/article/details/109819127
'''

if __name__=='__main__':
    uvicorn.run("main:app", reload=True)

