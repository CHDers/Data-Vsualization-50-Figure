# 开发作者：Yanjun Hao
# 开发时间：2021/1/6 0006 10:56
# coding=utf-8
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

file_path='D:/python数据处理——数据/DataAnalysis-master/911data/911.csv'
df = pd.read_csv(file_path)

df['timeStamp'] = pd.to_datetime(df['timeStamp'])

df.set_index('timeStamp',inplace=True)

# print(df.head(10))

# 统计出911数据中不同月份电话次数
count_by_month = df.resample('M').count()['title']
print(count_by_month)

# 画图
_x = count_by_month.index
_y = count_by_month.values

# for i in _x:
#     print(dir(i))
#     break
_x = [i.strftime('%Y%m%d') for i in _x]

plt.figure(figsize=(20,8),dpi=80)

plt.plot(range(len(_x)),_y)

plt.xticks(range(len(_x)),_x,rotation=45)

plt.show()

