# _*_ coding: utf-8 _*_
# @Time: 13.09.2024 14:30
# @Author: Qi Wang
# @File: create_db
# @Project: python_SQLAlchemy learn
# @Quelle: https://www.youtube.com/watch?v=gvRXjsrpCHw

import mysql.connector

connection = mysql.connector.connect(host = 'localhost1234',
                                     port='3306',
                                     user='root',
                                     password='4UeUshk2U2QozoXLDLnL')

cursor = connection.cursor()

# 创建资料库
cursor.execute("CREATE DATABASE `qq`;")

# 取得所有资料库名称

cursor.close()
connection.close()