# _*_ coding: utf-8 _*_
# @Time: 13.09.2024 10:09
# @Author: Qi Wang
# @File: first_sqlalchemy
# @Project: python_SQLAlchemy learn
# @Quelle: https://www.youtube.com/watch?v=n6Xa6cokCKc&list=PLvQDgAXJ4ADP4G8Iuc02B11bvFokZMChK&index=2


import sqlalchemy
from dns.e164 import query

engine = sqlalchemy.create_engine('mysql://root:4UeUshk2U2QozoXLDLnL@localhost1234/sql_tutorial') # 这里告诉python使用何种方式连接什么样的数据库
conn = engine.connect() # 然后使用引擎帮助建立连接

query = sqlalchemy.text('SELECT * FROM students') # 这里是创建一个基本的SQL的原始查询语句
# 然后使用conn连接执行查询操作, 查询完成后会得到一个结果数据集result_set
result_set = conn.execute(query)


# 得到查询结果后，想要拿到每一行并直接打印输出
for row in result_set:
    print(row)

# 使用完之后，比较稳妥的做法是将连接关闭并且销毁引擎，善始善终
conn.close()
engine.dispose()
