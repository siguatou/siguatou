import numpy as np
import matplotlib.pyplot as mp

# 热成像图
# 用图形的方式显示矩阵及矩阵中值的大小
'''
    1 2 3
    4 5 6
    7 8 9
'''
n = 1000
# 分别生成x,y,两个二维数组
x , y = np.meshgrid(np.linspace(-3,3,n),
                    np.linspace(-3,3,n))
# print(x ,'->x')
# print(y ,'->y')
z = (1 -x/2 + x**5 +y**3) * np.exp(-x**2 - y**2)

mp.imshow(z,cmap='jet',origin='lower')
mp.colorbar()
mp.show()