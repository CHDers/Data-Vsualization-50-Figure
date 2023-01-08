# 开发作者：Yanjun Hao
# 开发时间：2020/12/30 0030 18:05
from matplotlib import pyplot as plt
from matplotlib import font_manager
import random

a = [random.randint(70,154) for i in range(320)]

# 计算组数
d = 3  #组距
num_bins = (max(a)-min(a))//d
print(max(a),min(a),max(a)-min(a))
print(num_bins)

# 设置图形大小
plt.figure(figsize=(20,8),dpi=80)

# 绘图
plt.hist(a,num_bins,density=True)

# 设置x轴的刻度
plt.xticks(range(min(a),max(a)+d,d))

plt.grid()

plt.show()
