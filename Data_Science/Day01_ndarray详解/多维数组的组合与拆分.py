''''''
'''
    垂直方向操作
'''
import numpy as np
# a = np.arange(1,7).reshape(2,3)
# b = np.arange(7,13).reshape(2,3)
# print('a:',a)
# print('b:',b)
# # 垂直方向完成组合操作，生成新数组
# c = np.vstack((a,b))
# print('c:',c)
# # 垂直方向完成拆分操作，生成两个数组
# d,e = np.vsplit(c,2)
# print('d:',d,'e:',e)
#
# # 水平方向操作
# f = np.hstack((a,b))
# print('f:',f)
# g,h = np.hsplit(f,2)
# print('g:',g)
# print('h:',h)
#
# # 深度方向操作
# i = np.dstack((a,b))
# print('i:',i)
# j,k = np.dsplit(i,2)
# print('j:',j)
# print('k:',k)

# 多维数组组合与拆分的相关函数：
# 通过axis作为关键字参数指定组合的方向，取值如下:
# 若待组合的数组都是二维数组：
#   0：垂直方向组合
#   1：水平方向组合
# 若待组合的数组都是三维数组：
#   0：垂直方向组合
#   1：水平方向组合
#   2：深度方向组合
# np.concatenate((a,b),axis=0) # axis=2，必须运用在三维数组上
# 通过给出的数组与要拆分的份数，按照某个方向进行拆分
# np.split(c,2,axis = 0)

# 长度不等的数组组合
a = np.array([1,2,3,4,5])
b = np.array([1,2,3,4])
# 填充b数组使其长度与a相同,头部补0个，尾部补1个元素
b = np.pad(b,pad_width=(0,1),mode='constant',constant_values=0)
print(b)
# 垂直方向完成组合操作，生成新数组
c = np.vstack((a,b))
print(c)
