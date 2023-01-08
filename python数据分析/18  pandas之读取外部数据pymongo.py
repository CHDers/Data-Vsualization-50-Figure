# 开发作者：Yanjun Hao
# 开发时间：2021/1/1 0001 12:09
import pandas as pd
from pymongo import MongoClient

client = MongoClient()
collection = client['douban']['tv1']
data = list(collection.find())

# t1 = data[0]
# t1 = pd.Series(t1)
# print(t1)

df = pd.DataFrame(data)
print(df)