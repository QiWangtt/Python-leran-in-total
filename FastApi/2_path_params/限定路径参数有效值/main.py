# _*_ coding: utf-8 _*_
# @Time: 25.09.2024 15:20
# @Author: Qi Wang
# @File: main
# @Project: Python
# @Quelle: https://blog.csdn.net/my_name_is_learn/article/details/109819127

# 有时候我们只想给某个路径参数传递某几个固定的有效值，我们就可以使用到这个方法。先看完整例子代码
import uvicorn
from enum import Enum
from fastapi import FastAPI

'''
第一步、创建一个继承str和Enum的类，并创建几个类属性，这些类属性的值将是可用的有效值

第二步、声明路径参数。路径参数hjx_man的值将传递给函数root的参数hjx_man，并且这个值的取值范围只能是Hjx_Class_name类中类属性的值。

例如你访问http://127.0.0.1:8001/hjx/20153201072，得到的会是：{“status”:“20153201072”}

例如你访问http://127.0.0.1:8001/hjx/True，得到的会是：{“status”:“True”}

这样我们就能做到给某个路径参数传递某几个固定的有效值了。
————————————————

                            版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。
                        
原文链接：https://blog.csdn.net/my_name_is_learn/article/details/109819127
'''
class Hjx_Class_name(str, Enum):
    Name = 'huangjunx'
    Year = 18
    Id = '20153201072'
    student = True


app = FastAPI()


@app.get('/hjx/{hjx_man}')
def root(hjx_man: Hjx_Class_name):
    return {'status': Hjx_Class_name.Name}


# 进一步，我们还可以在root函数里面调用这个类的类属性。通过Hjx_Class_name.Name进行调用。下面例子无论你使用哪个类属性的值访问，结果都是{"status":"huangjunx"}



if __name__=='__main__':
    uvicorn.run("main:app", reload=True)