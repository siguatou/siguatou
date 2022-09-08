import matplotlib.pyplot as mp

locators = ['mp.NullLocator()',
            'mp.MaxNLocator(nbins=4)',
            'mp.FixedLocator([3,6,9])',
            'mp.AutoLocator()'
            ]
mp.figure('locators',facecolor='lightgray')

for i,locator in enumerate(locators):
    mp.subplot(len(locators),1,i+1)
    mp.xlim(1,10)
    # 整理坐标轴
    # 获取当前坐标轴
    ax = mp.gca() # get current axis
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position(('data',0.5))
    mp.yticks([])
    # 设置水平坐标轴的主刻度定位器
    loc = eval(locator)
    ax.xaxis.set_major_locator(loc)
    # 设置水平坐标轴的次刻度定位器为多点定位器，间隔0.1
    ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))

mp.show()

