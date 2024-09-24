# _*_ coding: utf-8 _*_
# @Time: 24.09.2024 14:43
# @Author: Qi Wang
# @File: ValidationError
# @Project: Python
# @Quelle: https://blog.csdn.net/qq_33801641/article/details/120320775?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522DDD2FF1E-9E13-4C16-A1D4-B8B0AE1DB166%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=DDD2FF1E-9E13-4C16-A1D4-B8B0AE1DB166&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-120320775-null-null.142^v100^pc_search_result_base5&utm_term=python%20ValidationError&spm=1018.2226.3001.4187

# 一定要导入 ValidationError
from pydantic import BaseModel, ValidationError


class Person(BaseModel):
    id: int
    name: str


try:
    # id是个int类型，如果不是int或者不能转换int会报错
    p = Person(id="ss", name="hallen")
except ValidationError as e:
    # 打印异常消息
    print(e.errors())


