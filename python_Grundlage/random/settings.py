# _*_ coding: utf-8 _*_
# @Time: 20.09.2024 13:43
# @Author: Qi Wang
# @File: settings
# @Project: Python
# @Quelle: https://www.youtube.com/watch?v=70heS34o94c&list=PLvQDgAXJ4ADNKXsFtiQU_CcbxUQg5r-pR&index=2


# importing os module for environment variables
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values

# loading variables from .env file
load_dotenv()

# accessing and printing value
print(os.getenv("MY_KEY"))
