''''''
'''
    ndarray数组对象的维度操作
    视图变维(数据共享) (重要！！): reshape() 与 ravel()
'''
import numpy as np
a = np.arange(1,9)
print(a)  # [1,2,3,4,5,6,7,8,9]
b = a.reshape(2,4) # 视图变维：变为 2行4列的二维数组
print(b)
c = b.reshape(2,2,2) # 视图变维: 变为2页2行2列的三维数组
print(c)
d = c.ravel() # 视图变维   变为1维数组
print(d)

# 复制变维(数据独立) : flatten()
e = c.flatten()
print(e)