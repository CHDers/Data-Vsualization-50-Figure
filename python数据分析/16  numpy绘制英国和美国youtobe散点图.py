# 开发作者：Yanjun Hao
# 开发时间：2021/1/1 0001 11:25
import numpy as np
from matplotlib import pyplot as plt

us_file_path = 'D:/python数据处理——数据/DataAnalysis-master/day03/code/youtube_video_data/US_video_data_numbers.csv'
uk_file_path = 'D:/python数据处理——数据/DataAnalysis-master/day03/code/youtube_video_data/GB_video_data_numbers.csv'

# 加载国家数据
t_uk = np.loadtxt(uk_file_path,delimiter=',',dtype='int')

# 选择喜欢数比500000小的数据
t_uk = t_uk[t_uk[:,1]<=500000]

# 取评论的数据
t_uk_comments = t_uk[:,-1]
t_uk_like = t_uk[:,1]

# 绘图
plt.figure(figsize=(20,8),dpi=80)

plt.scatter(t_uk_like,t_uk_comments)

plt.show()