import numpy as np
a = np.array([
    [1+1j,2+4j,3+7j],
    [4+2j,5+5j,6+8j],
    [7+3j,8+6j,9+9j]
])
# print(a.shape) # a几行几列
# print(a.dtype) # a中数据的类型
# print(a.ndim)
# print(a.size) # a中元素的个数总数
# print(a.itemsize)
# print(a.nbytes)
# print(a.real) # a中所有数据的实部
# print(a.imag) # a中所有数据的虚部
# print(a.T) # a的转置视图
# print([x for x in a.flat]) # a.flat 返回a的一维数组


b = np.array([[1., 2., 3.],
 [4., 5. ,6.],
 [7., 8. ,9.]])
print(b)
print(b.T)