import numpy as np
import matplotlib.pyplot as mp

apples = np.array([34,98,54,56,89,79,45,65,34,10,32,96])
oranges = np.array([34,9,59,34,75,72,34,90,53,27,45,79])
x = np.arange(apples.size)

# 绘制柱状图
mp.figure('Bar',facecolor='lightgray')
mp.title('Bar Chart',fontsize=18)
mp.grid(linestyle=':')
mp.bar(x-0.2,apples,0.4,color='limegreen',label='Apples',align='center')
mp.bar(x+0.2,oranges,0.4,color='orangered',label='Oranges',align='center')

# 设置刻度
mp.xticks(x,['Jan','Feb','Mar','Apri','May','June','July','Aug','Sep','Oct','Nov','Dec'])
mp.legend()
mp.show()