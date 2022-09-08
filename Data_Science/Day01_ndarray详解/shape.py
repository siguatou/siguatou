import numpy as np

a = np.arange(1,10)
print(a,a.shape)

# 视图变维
b = a.reshape(3,3) # 这里a不会作任何改变，b是新生成的数组
print('a:',a)
a[0] = 999
print('b:',b)
print(b.ravel()) # 称平数组

# 复制变维
c = b.flatten()
b[0][0] = 88
print('b:',b)
print('c:',c)

# 就地变维
c.shape = (3,3)
print('c:',c)
c.resize((9,))
print('c:',c)
c.resize((3,3))
print('c:',c)