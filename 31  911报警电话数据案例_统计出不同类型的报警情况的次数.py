# 开发作者：Yanjun Hao
# 开发时间：2021/1/6 0006 10:56
# coding=utf-8
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

file_path='D:/python数据处理——数据/DataAnalysis-master/911data/911.csv'
df = pd.read_csv(file_path)
# print(df.head(10))
# print(df.info())
# print(df.shape[0])

# 获取分类情况
temp_list = df['title'].str.split(': ').tolist()
cate_list = list(set([i[0] for i in temp_list]))
print(cate_list)

# 构造全为0的数组
zeros_df = pd.DataFrame(np.zeros((df.shape[0],len(cate_list))),columns=cate_list)

# 赋值
# 赋值(第一种方法，比较快)
for cate in cate_list:
    zeros_df[cate][df['title'].str.contains(cate)] = 1
    # break
    pass
print(zeros_df)
print('*'*100)
# 赋值(第二种方法，很慢)
# for i in range(df.shape[0]):
#     zeros_df.loc[i,temp_list[i][0]] = 1
#     pass
# print(zeros_df)

sum_ret = zeros_df.sum(axis=0)
print(sum_ret)