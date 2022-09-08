import numpy as np
import matplotlib.pyplot as mp

# 极坐标系
# 与笛卡尔坐标系不同，某些情况下极坐标系适合显示与角度有关的图像。例如雷达等。
# 极坐标系可以描述极径p与极角0的线性关系

mp.figure('Polar',facecolor='lightgray')
mp.gca(projection='polar')
mp.title('Polar',fontsize=20)
mp.xlabel(r'$\theta$',fontsize=14)
mp.ylabel(r'$\rho$',fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
# mp.show()
# 准备数据
t = np.linspace(0,4*np.pi,1000)
r = 0.8*t
mp.plot(t,r)
mp.show()