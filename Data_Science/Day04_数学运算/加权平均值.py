''''''
'''
    加权平均值
    样本:S=[s1,s2,...,sn]
    权重:W=[w1,w2,...,wn]
    加权平均值:a = (s1w1+s2w2+...+snwn)/(w1+w2+...+wn)
    
    np.average(closing_prices,weights=volumes)
    
    VWAP - 成交量加权平均价格(成交量体现了市场对当前交易价格的认可度,成交量加权平均价格将会更接近这支股票的真实价值)
    
'''
import numpy as np
import datetime as dt
import matplotlib.pyplot as mp
import matplotlib.dates as md

# np.average(closing_prices,weights=volumes)
#
#     VWAP - 成交量加权平均价格(成交量体现了市场对当前交易价格的认可度,成交量加权平均价格将会更接近这支股票的真实价值)
def dmy2ymd(dmy):
    # dmy = str(dmy,encoding='utf-8')
    dmy = str(dmy)
    # 字符串日期,转成datetime时间对象
    time = dt.datetime.strptime(dmy,'%d-%m-%Y').date()
    # 日期对象,按照我们想要的格式转换成字符串
    t = time.strftime('%Y-%m-%d')
    return t

# print(dmy2ymd('23-01-2022'))

dates,opening_prices,highest_prices,lowest_prices,closing_prices,volumes = \
    np.loadtxt('../da_data/aap1.csv',
          delimiter=',',
          usecols=(1,3,4,5,6,7),
          dtype='M8[D],f8,f8,f8,f8,f8',
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

# # 求算术平均数
# mean = np.mean(closing_prices)
# # mean = closing_prices.mean()
# mp.hlines(mean,dates[0],dates[-1],color='green',label='Mean')

# VWAP
vwap = np.average(closing_prices,weights=volumes)
mp.hlines(vwap,dates[0],dates[1],colors='red',label='VWAP')

mp.legend()
mp.gcf().autofmt_xdate() # 当前窗口自动格式化x轴日期(将日期斜着写,不会覆盖)
mp.show()

#--------------------------------分割线----------------------------------
'''
    TWAP  时间加权平均价格(时间越晚权重越高,参考意义越大)
'''
times = np.linspace(1,10,closing_prices.size)
twap = np.average(closing_prices,weights=times)
mp.hlines(twap,dates[0],dates[-1],color='blue',label='TWAP')

mp.legend()
mp.gcf().autofmt_xdate() # 当前窗口自动格式化x轴日期(将日期斜着写,不会覆盖)
mp.show()
