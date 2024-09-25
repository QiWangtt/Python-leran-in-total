# _*_ coding: utf-8 _*_
# @Time: 25.09.2024 10:37
# @Author: Qi Wang
# @File: main
# @Project: Python
# @Quelle: https://www.youtube.com/watch?v=70heS34o94c&list=PLvQDgAXJ4ADNKXsFtiQU_CcbxUQg5r-pR&index=2

import uvicorn
from fastapi import FastAPI, Form
from pydantic import BaseModel, Field


app = FastAPI()


@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username": password}


class Item(BaseModel):
    name: str = Field(..., title="Item Name", max_length=100)
    description: str = Field(None, title="Item Description", max_length=255)
    price: float = Field(..., title="Item Price", gt=0)


@app.post("/items/")
def create_item(item: Item):
    return item


if __name__=='__main__':
    uvicorn.run("main:app", reload=True)