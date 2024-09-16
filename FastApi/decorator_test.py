# _*_ coding: utf-8 _*_
# @Time: 16.09.2024 11:27
# @Author: Qi Wang
# @File: decorator_test
# @Project: FastApi learn
# @Quelle: https://www.youtube.com/watch?v=70heS34o94c&list=PLvQDgAXJ4ADNKXsFtiQU_CcbxUQg5r-pR&index=2

import time
from turtledemo.penrose import start


'''def timeit(f):

    # def wrapper(*args, **kwargs):
    def wrapper(x, y):
        start = time.time()
        # ret = f(*args, **kwargs)
        ret = f(x, y)
        print(time.time()-start)
        return ret

    return wrapper


@timeit
def add(x, y):
    return x ** y

print(add(2, 3))'''


def timeit(iteration):

    def inner(f):

        def wrapper(*args, **kwargs):
            start = time.time()
            for _ in range(iteration):
                ret = f(*args, **kwargs)
            print(time.time()-start)
            return ret
        return wrapper

    return inner


@timeit(10000000)
def add(x, y):
    return x ** y

print(add(2, 3))


