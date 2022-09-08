import numpy as np
import matplotlib.pyplot as mp

x = np.array([1,2,3,4,5,6])
y = np.array([12,39,36,25,16,4])
mp.plot(x,y)
# mp.show()

# vertical 绘制垂直线
mp.vlines(3,12,25)

# horizontal 绘制水平线
mp.hlines([25,10,12,8],[1,2,3,4],[4,5,6,7])
mp.plot(x,y)
# 显示图表
mp.show()