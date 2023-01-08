# 开发作者：Yanjun Hao
# 开发时间：2021/1/6 0006 10:56
# coding=utf-8
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

file_path='D:/python数据处理——数据/DataAnalysis-master/911data/911.csv'
df = pd.read_csv(file_path)

# 获取分类情况
temp_list = df['title'].str.split(': ').tolist()
cate_list = [i[0] for i in temp_list]
# pd.set_option('display.max_columns', None)   #显示完整的列
# pd.set_option('display.max_rows', None)  #显示完整的行
df['cate'] = pd.DataFrame(np.array(cate_list).reshape((df.shape[0],1)))

print(df.head(5))
print(df.groupby(by='cate').count()['title'])


