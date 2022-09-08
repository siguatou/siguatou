import numpy as np

# 一维数组的组合方案
a = np.arange(1,9)
b = np.arange(9,17)
print(a)
print(b)
print(np.row_stack((a,b))) # 形成两行
print(np.column_stack((a,b))) # 形成两列