# 开发作者：Yanjun Hao
# 开发时间：2021/1/4 0004 20:35
import pandas as pd
import numpy as np

file_path = 'D:/python数据处理——数据/DataAnalysis-master/day05/code/starbucks_store_worldwide.csv'

df = pd.read_csv(file_path)

# 统计中国每个省店铺的数量
china_data = df[df['Country']=='CN']

grouped = china_data.groupby(by='State/Province').count()['Brand']

print(grouped)

# 数据按照多个条件进行分组，返回Series
grouped = df['Brand'].groupby(by=[df['Country'],df['State/Province']]).count()
print(grouped)
print(type(grouped))  #series类型

# 数据按照多个条件进行分组，返回DataFrame
grouped1 = df[['Brand']].groupby(by=[df['Country'],df['State/Province']]).count()
grouped2 = df.groupby(by=[df['Country'],df['State/Province']]).count()[['Brand']]
grouped3 = df.groupby(by=[df['Country'],df['State/Province']])[['Brand']].count()
print(grouped1,type(grouped1))
print('*'*100)
print(grouped2,type(grouped2))
print('*'*100)
print(grouped3,type(grouped3))

# 索引的方法和属性
print(grouped1.index)
