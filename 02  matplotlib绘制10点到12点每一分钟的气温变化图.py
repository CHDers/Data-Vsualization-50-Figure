# 开发作者：Yanjun Hao
# 开发时间：2020/12/30 0030 11:19
from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager

# windows和linux设置字体的方法
# font = {'family':'MicroSoft YaHei',
#         'weight':'bold',
#         'size':'15'}
# matplotlib.rc('font',**font)
# matplotlib.rc('font',family='MicroSoft YaHei',weight='bold',size='15')

# 另外一种设置字体的方式
my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')

x = range(0,120)
y = [random.randint(20,35) for i in range(120)]

plt.figure(figsize=(20,8),dpi=80)

plt.plot(x,y)

# 调整x轴的刻度
_xtick_labels = ['10点{}分'.format(i) for i in range(0,60)]
_xtick_labels += ['11点{}分'.format(i) for i in range(0,60)]
# 取步长，数字和字符串一一对应，数据的长度一样
plt.xticks(list(x)[::3],_xtick_labels[::3],rotation=45,fontproperties=my_font)  #rotation旋转的度数

# 添加描述信息
plt.xlabel('时间',fontproperties=my_font)
plt.ylabel('温度 单位（℃）',fontproperties=my_font)
plt.title('10点到12点每分钟的气温变化情况',fontproperties=my_font)
plt.show()