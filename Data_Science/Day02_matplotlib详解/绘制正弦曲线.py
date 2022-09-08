import numpy as np
import matplotlib.pyplot as mp

# 线性拆分1000个点
x = np.linspace(-np.pi,np.pi,1000)
y = np.sin(x)
cosx = np.cos(x)/2

# 设置坐标轴的范围
# mp.xlim(0,np.pi)
# mp.ylim(0,1)

# 设置坐标刻度
# 修改x轴的刻度文本
vals = [-np.pi, -np.pi/2, 0 , np.pi/2 , np.pi]
# LaTex排版语法字符串
texts = [r'$-\pi$',r'$-\frac{\pi}{2}$','0',r'$\frac{\pi}{2}$',r'$\pi$'] # 非常重要！！
mp.xticks(vals,texts)

# 修改坐标轴
ax = mp.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))
mp.yticks([-1.0,-0.5,0.5,1])

mp.plot(x,y,linestyle='--',linewidth=2,color = 'orangered',alpha = 0.5,label=r'$y=sin(x)$')
mp.plot(x,cosx,linestyle='-.',linewidth=2,color = 'dodgerblue',alpha = 0.9,label=r'$y=\frac{1}{2}cos(x)$')

# 绘制特殊点
pointx=[np.pi/2,np.pi/2]
pointy=[1,0]
mp.scatter(pointx,pointy,marker='s',s=70,color='red',label='sample points',zorder=3)

# 在图表中为某个点添加备注。包括备注文本，备注箭头等图像的设置
mp.annotate(
    r'$[\frac{\pi}{2},1]$',     # 备注中显示的文本内容
    xycoords ='data',           # 备注目标点所使用的坐标系(data表示数据坐标系)
    xy = (np.pi/2,1),           # 备注目标点的坐标
    textcoords='offset points', # 备注文本所使用的坐标系(offset points)
    xytext = (40,20),           # 备注文本的坐标
    fontsize = 14,              # 备注文本的字体大小
    arrowprops = dict(          # 使用字典定义文本指向目标点的箭头
        arrowstyle='->',        # 定义箭头样式
        connectionstyle='arc3'# 定义连接线样式  angle,angle3,arc,arc3,bar
    )
)

# 图例，在plot中添加label值
mp.legend()
mp.show()