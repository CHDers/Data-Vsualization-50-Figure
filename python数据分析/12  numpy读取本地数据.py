# 开发作者：Yanjun Hao
# 开发时间：2020/12/31 0031 19:34
import numpy as np

us_file_path = 'D:/python数据处理——数据/DataAnalysis-master/day03/code/youtube_video_data/US_video_data_numbers.csv'
uk_file_path = 'D:/python数据处理——数据/DataAnalysis-master/day03/code/youtube_video_data/GB_video_data_numbers.csv'

# t1 = np.loadtxt(us_file_path,delimiter=',',dtype='int',unpack=True)
t2 = np.loadtxt(us_file_path,delimiter=',',dtype='int')

# print(t1)
# print('*'*100)
print(t2)
print('*'*100)

# 取行
# print(t2[2])

# 取连续的多行
# print(t2[2:])

# 取不连续的多行
# print(t2[[2,8,10]])

# 取列
# print(t2[1,:])
# print(t2[2:,:])
# print(t2[[2,10,3],:])
# print(t2[:,0])

# 取连续的多列
# print(t2[:,2:])

# 取不连续的多列
# print(t2[:,[0,2]])

# 取行和列，取第三行，第四列的值
# a = t2[2,3]
# print(a)
# print(type(a))

# 取多行和多列，取第三行到第五行，第2列到第4列的结果
# 取的是行和列交叉点的位置
# b = t2[2:5,1:4]
# print(b)

# 取多个不相邻的点
# 选出来的结果是(0,0) (2,1) (2,3)
# c = t2[[0,2,2],[0,1,3]]
# print(c)















