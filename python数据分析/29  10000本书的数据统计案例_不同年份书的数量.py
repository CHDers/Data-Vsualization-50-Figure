# 开发作者：Yanjun Hao
# 开发时间：2021/1/5 0005 12:13
# coding=utf-8
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

file_path = 'D:/python数据处理——数据/DataAnalysis-master/day05/code/books.csv'
df = pd.read_csv(file_path)
# print(df.head(2))
#
# print(df.info())

data1 = df[pd.notnull(df['original_publication_year'])]

grouped = data1.groupby(by='original_publication_year').count()['title']
