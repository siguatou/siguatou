import numpy as np

# ary = np.array([1,2,3,4,5,6])
# print(type(ary))
# print(ary.shape)# 维度
# ary.shape = (2,3) # 维度改为2行3列
# print(ary,ary.shape)
# ary.shape = (6,)
# # ary = np.array([1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6])
# # 数组的运算
# print(ary)
# print(ary*3)
# print(ary > 3)
# print(ary + ary)
#
# a = np.arange(0,50,1)
# print(a)
#
# b = np.arange(0,100,2)
# print(b)
#
# c = np.zeros(10,dtype='int32')
# c = np.zeros(10)
# print(c)
#
# d = np.ones(10)
# d.shape = (2,5)
# print(d)
#
# 5个1/5
e = np.ones(5) / 5
# print(e)
#
# 扩展 np.zero_like()  np.ones_like() -> 维度相似
# f = np.zeros_like(e)
# f = np.ones_like(e)
# print(f)

# g = f.astype('bool_')
# print(g)
#
# g = np.ones_like(d)
# print(g)
#
# ary = np.array([
#     [1,2,3,4],
#     [5,6,7,8]
# ])
# 观察维度、size、len的区别
# print(ary.shape,ary.size,len(ary))

# 元素的类型:np.ndarray.dtype
# ary = np.array([1,2,3,4,5,6])
# print(type(ary),ary,ary.dtype)
# # 转化array元素的类型
# ary.dtype = 'float32'  # 错误的修改数据类型的方式
# print(type(ary),ary,ary.dtype) # 错误的修改数据类型的方式
# b = ary.astype(float)
# print(type(b),b,b.dtype)
# print(type(ary),ary,ary.dtype)
# # 转化ary元素的类型
# c = ary.astype(str)
# print(type(c),c,c.dtype) # 注意type(c)是对象c的类型，c.dtype是向量c中元素的类型

# 数组元素的个数:np.ndarray.size
# ary = np.array([
#     [1,2,3,4],
#     [5,6,7,8],
#     [0,0,0,0]
# ])
# 观察维度、size、len的区别
# print(ary.shape,ary.size,len(ary))

# 数组元素索引(下标)
# 数组对象[...,页号,行号,列号]
# 下标从0开始，到数组len-1结束。
# a = np.array([
#     [[1,2],[3,4]],
#     [[5,6],[7,8]]
# ])
# print(a , a.shape)
# print(a[0])
# print(a[0][0])
# print(a[0][0][0]) # 页数 行数 列数
# print(a[0,0,0]) # 页数 行数 列数
# print(a.shape) # (2,2,2)
# print(a.shape[0]) # 获取页数
# print(a.shape[1]) # 获取行数
# print(a.shape[2]) # 获取列数
# for i in range(a.shape[0]):# 遍历页数
#     for j in range(a.shape[1]): # 遍历行数
#         for k in range(a.shape[2]): # 遍历列数
#             print(a[i,j,k])

# 自定义复合类型
data = [('zs',[90,80,85],15),('ls',[92,81,83],16),('ww',[95,85,95],15)]

# 第一种设置dtype的方式
# a = np.array(data,dtype='U2,3int32,int32')
# print(a)
# print(a[0]['f0'],':',a[1]['f1'])
# print('==================================')
# # 第二种设置dtype的方式
# b = np.array(data,dtype=[('name','str_',2),('scores','int32',3),('ages','int32',1)])
# print(b)
# print(b[2]['ages'])
# # 第三种设置dtype的方式
# c = np.array(data,dtype={
#     'names':['name','scores','age'], # 键必须是'names'
#     'formats':['U2','3int32','int32'] # 键必须是'formats'
# })
# print(c)
# print(c[1]['name'])

# 测试数组中存储日期数据类型
# dates = ['2011-01-01',
#          '2011',
#          '2012-01-01',
#          '2011-02',
#          '2012-02-01 10:10:00',
#          ]
# dates = np.array(dates)
# # 转换类型
# dates = dates.astype('M8[D]')
# print(dates,dates.dtype)
# print(dates[4]-dates[2])
#




