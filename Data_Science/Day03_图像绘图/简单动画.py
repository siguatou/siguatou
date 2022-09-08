# 简单动画
# 动画即是在一段时间内快速连续地重新绘制图像的过程。
# matplotlib提供了方法用于处理简单动画的绘制。定义update函数用于即时更新图像。

import matplotlib.animation as ma
import numpy as np
import matplotlib.pyplot as mp

# 自定义一种可以存放在ndarray里的类型，用于保存一个球
ball_type = np.dtype([
    ('position',float,2),  # 位置(水平和垂直坐标)
    ('size',float,1),      # 大小
    ('growth',float,1),    # 生长速度
    ('color',float,4),     # 颜色(红、绿、蓝和透明)
])
# 随机生成100个点对象
n = 100
balls = np.zeros(100,dtype=ball_type)
# 初始化balls数组每个字段的属性值
balls['position'] = np.random.uniform(0,1,(n,2)) # 随机生成位置的数值(100行2列)
balls['size'] = np.random.uniform(50,70,n)
balls['growth'] = np.random.uniform(10,20,n)
balls['color'] = np.random.uniform(0,1,(n,4))

# 画图
mp.figure('Animation',facecolor='lightgray')
mp.title('Animation',fontsize=16)
mp.xticks([])
mp.yticks([])
sc = mp.scatter(balls['position'][:,0],  # 100个点的x坐标
           balls['position'][:,1], # 100个点的y坐标
           s=balls['size'],
           color=balls['color']
           )
# 定义更新函数行为
def update(number):
    # 选择一个点
    index = number % 100
    # 重新修改index位置元素的属性
    balls['position'][index] = np.random.uniform(0,1,(1,2))  # 取值0~1,在当前index位置生成一个1行2列的数据
    balls['size'][index] = np.random.uniform(50,70,1)
    balls['size'] += balls['growth']
    # 重新绘制
    sc.set_sizes(balls['size']) # 更新大小
    sc.set_offsets(balls['position']) # 更新位置
# 每隔30毫秒执行一次Update更新函数，作用于mcp.gcf()当前窗口对象
# mp.gcf():  获取当前窗口 get current figure
# update：   更新函数
# interval:  间隔时间(单位:毫秒)
anim = ma.FuncAnimation(mp.gcf(),update,interval=10)
mp.show()

#---------------------------------分割线----------------------------

# mp.figure('Signal',facecolor='lightgray')
# mp.title('Signal',fontsize=14)
# mp.xlim(0,10)
# mp.ylim(-3,3)
# mp.grid(linestyle='--',color='lightgray',alpha=0.5)
# pl = mp.plot([],[],color='dodgerblue',label='Signal')
# pl.set_data([],[])
#
# x = 0
#
# def update(data):
#     t,v = data
#     x,y = pl.get_data()
#     x.append(t)
#     y.append(v)
#     # 重新设置数据源
#     pl.set_data(x,y)
#     # 移动坐标轴
#     if(x[-1]>10):
#         mp.xlim(x[-1] - 10, x[-1])
#
# def y_generator():
#     global x
#     y = np.sin(2*np.pi*x)*np.exp(np.sin(0.2*np.pi*x))
#     yield (x,y)
#     x += 0.05
#
# anim = ma.FuncAnimation(mp.gcf(),update,y_generator,interval=20)
# mp.tight_layout()
# mp.show()


