import numpy as np
import datetime as dt
import matplotlib.pyplot as mp
import matplotlib.dates as md

def dmy2ymd(dmy):
    # dmy = str(dmy,encoding='utf-8')
    dmy = str(dmy)
    # 字符串日期,转成datetime时间对象
    time = dt.datetime.strptime(dmy,'%d-%m-%Y').date()
    # 日期对象,按照我们想要的格式转换成字符串
    t = time.strftime('%Y-%m-%d')
    return t

# print(dmy2ymd('23-01-2022'))

dates,opening_prices,highest_prices,lowest_prices,closing_prices = \
    np.loadtxt('../da_data/aap1.csv',
          delimiter=',',
          usecols=(1,3,4,5,6),
          dtype='M8[D],f8,f8,f8,f8',
          unpack=True,
          converters={1:dmy2ymd})

# print(dates,opening_prices,highest_prices,lowest_prices,closing_prices )
# 绘制收盘价的折线图
mp.figure('AAPL',facecolor='lightgray')
mp.title('AAPL',fontsize=16)
mp.xlabel('Date',fontsize=14)
mp.ylabel('closing prices',fontsize=14)
mp.grid(linestyle=":")

# 拿到坐标轴
ax = mp.gca()
# 设置主刻度定位器为周定位器(每周一显示主刻度文本)
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_major_formatter(md.DateFormatter('%d %b %Y'))

# 设置次刻度定位器为日定位
ax.xaxis.set_minor_locator(md.DateLocator())

dates = dates.astype(md.datetime.datetime)
mp.plot(dates,closing_prices,color='dodgerblue',label='AAPL',linestyle='--',linewidth=2)
mp.legend()
mp.gcf().autofmt_xdate() # 当前窗口自动格式化x轴日期(将日期斜着写,不会覆盖)
mp.show()

