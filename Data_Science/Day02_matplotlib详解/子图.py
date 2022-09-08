import matplotlib.pyplot as mp
import numpy as np
import matplotlib.gridspec as mg
# 矩阵式布局
# mp.figure('Subplot',facecolor='lightgrey')
#
# for i in range(1,65):
#     mp.subplot(8,8,i)
#     mp.text(0.5,0.5,i,ha='center',va='center',size=20,alpha=0.6)
#     mp.xticks([]) # 清除刻度
#     mp.yticks([]) # 清除刻度
#     mp.tight_layout() # 外边距缩小
# mp.show()

# 网格式布局
# 网格式布局支持单元格合并
mp.figure('Grid Layout',facecolor='lightgrey')
gs = mg.GridSpec(3,3)
mp.subplot(gs[0,:2]) # 0行的前两列合并
mp.text(0.5,0.5,'1',size=36,alpha=0.6,ha='center',va='center')
mp.xticks([])
mp.yticks([])
mp.tight_layout()

mp.subplot(gs[:2,2]) # 第三列前两行合并
mp.text(0.5,0.5,'2',size=36,alpha=0.6,ha='center',va='center')
mp.xticks([])
mp.yticks([])
mp.tight_layout()

mp.subplot(gs[1,1]) # 第二行第二列的交叉点，不合并
mp.text(0.5,0.5,'3',size=36,alpha=0.6,ha='center',va='center')
mp.xticks([])
mp.yticks([])
mp.tight_layout()

mp.subplot(gs[1:,0]) # 第一列的第二、三行合并
mp.text(0.5,0.5,'4',size=36,alpha=0.6,ha='center',va='center')
mp.xticks([])
mp.yticks([])
mp.tight_layout()

mp.subplot(gs[2,1:]) # 第三行的第二、三列合并
mp.text(0.5,0.5,'5',size=36,alpha=0.6,ha='center',va='center')
mp.xticks([])
mp.yticks([])
mp.tight_layout()

mp.show()

# 自由式布局
# mp.figure('Flow Layout',facecolor='lightgray')
# 设置图标的位置，给出左下角点坐标与宽高即可
# left_bottom_x: 左下角点x坐标
# left_bottom_y: 左下角点y坐标
# width:宽度
# height:高度
# mp.axes([left_bottom_x,left_bottom_y,width,height])
# mp.axes([0.03,0.03,0.94,0.94])
# mp.text(0.5,0.5,'1',ha='center',va='center',size=36)
# mp.show()





