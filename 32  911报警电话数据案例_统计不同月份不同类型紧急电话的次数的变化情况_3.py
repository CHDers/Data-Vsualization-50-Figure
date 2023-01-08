# 开发作者：Yanjun Hao
# 开发时间：2021/1/6 0006 10:56
# coding=utf-8
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

file_path='D:/python数据处理——数据/DataAnalysis-master/911data/911.csv'

df = pd.read_csv(file_path)

# 添加列，表示分类
temp_list = df['title'].str.split(': ').tolist()
cate_list = [i[0] for i in temp_list]
df['cate'] = pd.DataFrame(np.array(cate_list).reshape((df.shape[0],1)))

# 把时间字符串转化为时间类型设置为索引
df['timeStamp'] = pd.to_datetime(df['timeStamp'])
df.set_index('timeStamp',inplace=True)

# print(df.head())

plt.figure(figsize=(20,8),dpi=80)

# 分组
for group_name,group_data in df.groupby(by='cate'):
    # 对不同的分类都进行绘图
    count_by_mouth = group_data.resample('M').count()['title']

    # 画图
    _x = count_by_mouth.index
    _y = count_by_mouth.values

    _x = [i.strftime('%Y%m%d') for i in _x]

    plt.plot(range(len(_x)), _y, label=group_name)
    pass

plt.xticks(range(len(_x)), _x, rotation=45)
plt.legend(loc='best')
plt.show()