# 开发作者：Yanjun Hao
# 开发时间：2021/1/6 0006 19:57
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

file_path='D:/python数据处理——数据/DataAnalysis-master/day06/code/PM2.5/BeijingPM20100101_20151231.csv'
df = pd.read_csv(file_path)

# 把分开的时间字符串通过periodindex的方法转化为pandas的时间类型
period = pd.PeriodIndex(year=df['year'],month=df['month'],day=df['day'],hour=df['hour'],freq='H')
df['datetime'] = period
# print(df.head(10))

# 把datetime设置为索引
df.set_index('datetime',inplace=True)

# 进行降采样
df = df.resample('7D').mean()
print(df.shape)

# 处理缺失数据，删除缺失数据
# print(df['PM_US Post'])
# data = df['PM_US Post'].dropna()
# data_china = df['PM_Dongsi'].dropna()

data = df['PM_US Post']
data_china = df['PM_Dongsi']

# 画图
_x = data.index
_x = [i.strftime('%Y%m%d') for i in _x]
_x_china = [i.strftime('%Y%m%d') for i in data_china.index]
_y = data.values
_y_china = data_china.values

plt.figure(figsize=(20,8),dpi=80)

plt.plot(range(len(_x)),_y,label='PM_US Post')
plt.plot(range(len(_x_china)),_y_china,label='PM_Dongsi')

plt.xticks(range(0,len(_x),10),list(_x)[::10],rotation=45)

plt.legend(loc='best')

plt.show()

