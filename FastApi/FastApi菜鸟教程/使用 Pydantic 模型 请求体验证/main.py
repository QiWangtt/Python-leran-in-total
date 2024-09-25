# _*_ coding: utf-8 _*_
# @Time: 25.09.2024 10:15
# @Author: Qi Wang
# @File: FastAPI Pydantic 模型
# @Project: Python
# @Quelle: https://www.runoob.com/fastapi/fastapi-pydantic.html

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str = "Jack"
    description: str = "stri    ng"
    price: float
    tax: float = None

@app.post("/items/")
def create_item(item: Item):
    return item


if __name__=='__main__':
    uvicorn.run("main:app", reload=True)