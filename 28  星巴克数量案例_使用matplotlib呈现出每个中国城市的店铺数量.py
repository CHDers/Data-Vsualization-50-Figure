# 开发作者：Yanjun Hao
# 开发时间：2021/1/4 0004 20:35
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')

file_path = 'D:/python数据处理——数据/DataAnalysis-master/day05/code/starbucks_store_worldwide.csv'

df = pd.read_csv(file_path)
df = df[df['Country']=='CN']

# 使用matplotlib呈现出店铺总数排名前10的国家
# 准备数据
data1 = df.groupby(by='City').count()['Brand'].sort_values(ascending=False)[:25]

_x = data1.index
_y = data1.values

# 画图
plt.figure(figsize=(20,12),dpi=80)

# plt.bar(range(len(_x)),_y,width=0.3,color='orange')
plt.barh(range(len(_x)),_y,height=0.3,color='orange')

plt.yticks(range(len(_x)),_x,fontproperties=my_font)

plt.show()