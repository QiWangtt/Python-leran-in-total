# _*_ coding: utf-8 _*_
# @Time: 25.09.2024 10:28
# @Author: Qi Wang
# @File: main
# @Project: Python
# @Quelle: https://www.runoob.com/fastapi/fastapi-pydantic.html

import uvicorn
from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.get("/items/")
def read_item(item: Item, q: str = Query(..., max_length=10)):
    return {"item": item, "q": q}


# https://blog.csdn.net/my_name_is_learn/article/details/109819127?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522F6627062-56B7-43D7-BB45-59EBAD26E2BC%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=F6627062-56B7-43D7-BB45-59EBAD26E2BC&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-109819127-null-null.142^v100^pc_search_result_base5&utm_term=fastapi&spm=1018.2226.3001.4187
# 当你需要使用Python类型来声明query参数的时候(例如用int)，他们就会被转换为相应的类型并且依据这个类型来验证传入参数
@app.get("/files/")
def add(num1: int=3, num2: int=8):
    return {"num1 + num2 = ": num1 + num2}



if __name__=='__main__':
    uvicorn.run("main:app", reload=True)