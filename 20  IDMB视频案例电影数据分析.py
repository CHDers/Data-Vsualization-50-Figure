# 开发作者：Yanjun Hao
# 开发时间：2021/1/4 0004 18:26
import pandas as pd
import numpy as np

file_path='D:/python数据处理——数据/DataAnalysis-master/day05/code/IMDB-Movie-Data.csv'
df = pd.read_csv(file_path)

# print(df.info())

print(df.head(1))

# 获取平均评分
print(df['Rating'].mean())

# 获取导演人数
# print(len(set(df['Director'].tolist())))
print(len(df['Director'].unique()))

# 获取演员的人数
temp_actors_list = df['Actors'].str.split(', ').tolist()
actors_list = [i for j in temp_actors_list for i in j]
# actors_list = list(np.array(temp_actors_list).flatten())
actors_num1 = len(set(actors_list))
print(actors_num1)
