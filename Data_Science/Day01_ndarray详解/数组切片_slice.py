import numpy as np

# # 一维数组切片
# a = np.arange(1,10)
# print(a)
# print(a[:3])
# print(a[3:6])
# print(a[6:])
# print(a[::-1])
# print(a[:-4:-1]) # [9 8 7]
# print(a[-4:-7:-1])
# print(a[-7::-1])
# print(a[::])
# print(a[:])
# print(a[::3])
# print(a[1::3])
# print(a[2::3])
#
# # 二维数组切片
# a.resize(3,3)
# print(a)
# print(a[:2,:2])
# print(a[::2,::2])

# 三维数组切片
a = np.arange(1,28)
a.resize(3,3,3)
print(a)
# 切出1页
print(a[1,:,:])
# 切出所有页的1行
print(a[:,1,:])
# 切出0页的1行1列
print(a[0,:,1])





