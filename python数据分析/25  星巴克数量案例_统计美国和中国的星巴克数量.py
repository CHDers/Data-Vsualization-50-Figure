# 开发作者：Yanjun Hao
# 开发时间：2021/1/4 0004 20:35
import pandas as pd
import numpy as np

file_path = 'D:/python数据处理——数据/DataAnalysis-master/day05/code/starbucks_store_worldwide.csv'

df = pd.read_csv(file_path)
# print(df.head(1))
# print(df.info())

grouped = df.groupby(by='Country')
print(grouped)

# DataFrameGroupBy
# 可以进行遍历
# for i,j in grouped:
#     print(i)
#     print('-'*100)
#     print(j)
#     print('*'*100)
# df[df['Country']='US']
# 调用聚合方法
country_count = grouped['Brand'].count()
print(country_count['US'])
print(country_count['CN'])