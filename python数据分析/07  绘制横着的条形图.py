# 开发作者：Yanjun Hao
# 开发时间：2020/12/30 0030 17:04
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')
a=["战狼2","速度与激情8","功夫伽","西游伏妖篇","变形金5:最后的骑士","摔跤吧！爸爸","加勒比海盜5:死无对证","金刚：骷島","极限特工：终极回归","生化危机6终章","乘风破浪","神愉奶爸3","智取威虎山","大闹天竺","金刚狼3:殊死一战","蛛侠英雄归来","悟空传","银河护卫队2","情圣","新木乃伊",]
b = [56.01,26.94,17.53,16.49,15.45,12.96,11.8,11.61,11.28,11.12,10.49,10.3,8.75,7.55,7.32,6.99,6.88,6.86,6.58,6.23]

# 设置图形大小
plt.figure(figsize=(20,8),dpi=80)

# 绘制条形图
plt.barh(range(len(a)),b,height=0.3,color='orange')

# 设置字符串到y轴
plt.yticks(range(len(a)),a,fontproperties=my_font)

# 添加网格
plt.grid(alpha=0.3)

# 展示图形
plt.show()

