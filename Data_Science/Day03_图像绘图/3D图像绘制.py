import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d

# n = 300
# x = np.random.normal(0,1,n)
# y = np.random.normal(0,1,n)
# z = np.random.normal(0,1,n)

# 绘制三维点阵
# mp.figure('3D scatter',facecolor='lightgray')
# ax3d = mp.gca(projection='3d')
# ax3d.set_xlabel('x')
# ax3d.set_ylabel('y')
# ax3d.set_zlabel('z')
# d = x**2 + y**2 + z**2
# ax3d.scatter(x, y, z,s =70,marker='o',c=d,cmap='jet')
# mp.show()

# 绘制三维曲面图
# n = 1000
# # 分别生成x,y,两个二维数组
# x , y = np.meshgrid(np.linspace(-3,3,n),
#                     np.linspace(-3,3,n))
# z = (1 -x/2 + x**5 +y**3) * np.exp(-x**2 - y**2)
#
# mp.figure('Contour',facecolor='lightgray')
# ax3d = mp.gca(projection='3d')
# ax3d.set_xlabel('X')
# ax3d.set_ylabel('Y')
# ax3d.set_zlabel('Z')
# ax3d.plot_surface(x,y,z,cstride=1,rstride=1,cmap='jet')
# mp.show()

# 绘制3D线框图
# rstride:行跨距
# cstride:列跨距
n = 5
# 分别生成x,y,两个二维数组
x , y = np.meshgrid(np.linspace(-3,3,n),
                    np.linspace(-3,3,n))
print(x ,'->x')
print(y ,'->y')
z = (1 -x/2 + x**5 +y**3) * np.exp(-x**2 - y**2)

mp.figure('Contour',facecolor='lightgray')
ax3d = mp.gca(projection='3d')
ax3d.set_xlabel('X')
ax3d.set_ylabel('Y')
ax3d.set_zlabel('Z')
ax3d.plot_wireframe(x,y,z,rstride=30,cstride=30,linewidth=1,color='dodgerblue')
# mp.show()
