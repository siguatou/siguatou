import matplotlib.pyplot as mp
import numpy as np
mp.figure('Grid Line',facecolor='lightgray')
ax = mp.gca()
# 修改刻度定位器
ax.xaxis.set_major_locator(mp.MultipleLocator(1)) # x轴主刻度
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1)) # x轴副刻度

ax.yaxis.set_major_locator(mp.MultipleLocator(250)) # y轴主刻度
ax.yaxis.set_minor_locator(mp.MultipleLocator(50)) # y轴副刻度

ax.grid(which='major',axis='both',color='orangered',linewidth=1) # 主刻度网格线设置
ax.grid(which='minor',axis='both',color='orangered',linewidth=0.25) # 副刻度网格线设置

# 绘制曲线
y = np.array([1,10,100,1000,100,10,1])
# mp.plot(y,'o-',color='dodgerblue')
# mp.show()

# 半对数坐标
# y轴将以指数方式递增.基于半对数坐标绘制第二个子图.
mp.semilogy(y,'o-',color='dodgerblue')
mp.show()