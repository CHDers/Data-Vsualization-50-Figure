# 开发作者：Yanjun Hao
# 开发时间：2021/1/4 0004 18:45
import pandas as pd
from matplotlib import pyplot as plt

file_path = 'D:/python数据处理——数据/DataAnalysis-master/day05/code/IMDB-Movie-Data.csv'

df = pd.read_csv(file_path)
# print(df.head(1))
# print(df.info())

# rating,runtime分布情况
# 选择图形，直方图
# 准备数据
runtime_data = df['Rating'].values

max_runtime = runtime_data.max()
min_runtime = runtime_data.min()

# 计算组数
print(max_runtime,min_runtime)
num_bin_list = [1.9]

i = 1.9
while i<=max_runtime:
    i += 0.5
    num_bin_list.append(i)
print(num_bin_list)

# 设置图形大小
plt.figure(figsize=(20,8),dpi=80)
plt.hist(runtime_data,num_bin_list)

plt.xticks(num_bin_list)

plt.show()
