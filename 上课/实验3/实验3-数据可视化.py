# By：仰晨
# 文件名：实验3-数据可视化
# 时 间：2022/12/6 14:27

import numpy as np
import matplotlib.pyplot as plt

# 1：绘制条形图
# 读取stock.csv文件中的收盘价，并绘制收盘价位于[9,14)、宽度为0.2的各区段内次数的直方图。


close_price = np.loadtxt('stock.csv', delimiter=",", usecols=(4,), unpack=True, skiprows=1)  # 拿这个表的第5行 转换为np格式
# print(close_price)
bins = np.arange(9, 14, 0.2)                          # 起点为9，终点为14（不包括），步长为0.2
# print(bins)
plt.hist(close_price, bins, rwidth=0.8)               # 条形宽度80%
plt.rcParams['font.sans-serif'] = ['SimHei']          # 中文----------------
plt.xticks(fontsize=15)                               # 设置刻度字体大小-------
plt.yticks(fontsize=15)                               # 设置刻度字体大小-------
plt.xlabel('股票价格', fontsize=15)
plt.ylabel('出现次数', fontsize=15)
plt.title('收盘价分布直方图', fontsize=18)
plt.show()


# 2：绘制单折线图
# 读取stock.csv文件的股票交易信息，绘制收盘价历史走势的折线图，并为该图添加图标题、轴标题和轴坐标范围。

"""
close_price = np.loadtxt('stock.csv', delimiter=",", usecols=(4,), unpack=True, skiprows=1)  # 拿这个表的第5行 转换为np格式
x = np.arange(len(close_price))                       # 横坐标 0--39
# print(x)
plt.plot(x, close_price)                              # 折线图
plt.rcParams['font.sans-serif'] = ['SimHei']          # 中文---------------------
plt.xticks(fontsize=15)                               # 设置刻度字体大小-----------
plt.yticks(fontsize=15)                               # 设置刻度字体大小-----------
plt.xlabel('时间顺序', fontsize=15)
plt.ylabel('收盘价', fontsize=15)
plt.title('股票收盘价走势图', fontsize=18)
plt.xlim(0.0, max(x)+1)                               # X轴显示的最小值  最大值----
plt.ylim(min(close_price)-1, max(close_price)+1)      # Y轴显示的~       ~-------
# plt.savefig('股票收盘价走势图.png')
plt.show()
"""

# 3：多条折线图
# 读取stock.csv文件的股票交易信息，在同一个图中绘制开盘价和收盘价历史走势的折线图，并分别赋以不同的颜色和线型，添加图例。
"""
open_price, close_price = np.loadtxt('stock.csv', delimiter=",", usecols=(1, 4), unpack=True, skiprows=1)
print(open_price)   # 第二行
print(close_price)  # 第五行
x = np.arange(len(close_price))                       # 横坐标 0--39
plot1, = plt.plot(x, open_price, 'g--', linewidth=1)  # 开盘折线图
plot2, = plt.plot(x, close_price, 'r', linewidth=2)  # 收盘折线图
plt.rcParams['font.sans-serif'] = ['SimHei']          # 中文-----------------
plt.xticks(fontsize=15)                               # 设置刻度字体大小-------
plt.yticks(fontsize=15)                               # 设置刻度字体大小------
plt.xlabel('时间顺序', fontsize=15)
plt.ylabel('开盘价与收盘价', fontsize=15)
plt.title('股票收盘价走势图', fontsize=18)
plt.xlim(0.0, max(x)+1)                                 # X轴显示的最小值 & 最大值---
plt.ylim(min(min(open_price), min(close_price))-1,      # Y轴显示的最小值---
         max(max(open_price), max(close_price))+1)      # Y轴显示的最大值---
plt.legend((plot1, plot2), ("开盘价", "收盘价"),          # 添加图例
           loc='lower right', fontsize=15, numpoints=1)
plt.show()
"""

# 4：散点图
# 读取文件stock.csv中股票收盘价，根据时间顺序绘制收盘价分布的散点图。
"""
close_price = np.loadtxt('stock.csv', delimiter=",", usecols=(4,), unpack=True, skiprows=1)  # 拿这个表的第5行 转换为np格式
x = np.arange(len(close_price))                       # 横坐标 0--39
plt.scatter(x, close_price, c='r', marker='o')
plt.rcParams['font.sans-serif'] = ['SimHei']          # 中文---------------------
plt.xticks(fontsize=15)                               # 设置刻度字体大小-----------
plt.yticks(fontsize=15)                               # 设置刻度字体大小-----------
plt.xlabel('时间顺序', fontsize=15)
plt.ylabel('收盘价', fontsize=15)
plt.title('股票收盘价走势图', fontsize=18)
plt.xlim(0.0, max(x)+1)                               # X轴显示的最小值  最大值----
plt.ylim(min(close_price)-1, max(close_price)+1)      # Y轴显示的~       ~-------
plt.show()
"""

# 5：绘制多轴图
# 绘制多轴图分别展示开盘价、收盘价、最di高价情况

"""
open_price, high_price, low_price, close_price = \
    np.loadtxt('stock.csv', delimiter=",", usecols=(1, 2, 3, 4), unpack=True, skiprows=1)  # 开盘  最高  最低  收盘

x = np.linspace(0, len(open_price), 40)
plt.rcParams['font.sans-serif'] = ['SimHei']          # 中文---------------------
plt.figure(figsize=(12, 10))                          # 图像大小
ax1 = plt.subplot(2, 2, 1)
ax2 = plt.subplot(2, 2, 2)
ax3 = plt.subplot(2, 2, 3)
ax4 = plt.subplot(2, 2, 4)
plt.sca(ax1)
plt.plot(x, open_price, color='red')
plt.xticks(fontsize=15)                               # 设置刻度字体大小-----------
plt.yticks(fontsize=15)                               # 设置刻度字体大小-----------
plt.title('开盘价', fontsize=15)

plt.sca(ax2)
plt.plot(x, close_price, 'b--')
plt.xticks(fontsize=15)                               # 设置刻度字体大小-----------
plt.yticks(fontsize=15)                               # 设置刻度字体大小-----------
plt.title('收盘价', fontsize=15)

plt.sca(ax3)
plt.plot(x, high_price, 'g--')
plt.xticks(fontsize=15)                               # 设置刻度字体大小-----------
plt.yticks(fontsize=15)                               # 设置刻度字体大小-----------
plt.title('最高价', fontsize=15)

plt.sca(ax4)
plt.plot(x, high_price)
plt.xticks(fontsize=15)                               # 设置刻度字体大小-----------
plt.yticks(fontsize=15)                               # 设置刻度字体大小-----------
plt.title('最低价', fontsize=15)

# 调整子图间距
plt.subplots_adjust(wspace=0.2, hspace=0.5)
plt.show()
"""

"""
# 6：绘制饼图
# 某学院有信息管理与信息系统、应用统计、经济统计、数据科学与大数据技术四个专业，
# 2018级各专业新生报到人数分别为33、65、30和30。
# 请用饼图表示各专业人数所占的比例，并突出显示信息管理与信息系统专业相关信息。
persons = [33, 65, 30, 30]
majors = ['信息管理与信息系统', '应用统计', '经济统计', '数据科学与大数据技术']
colors = ['c', 'm', 'r', 'y']
plt.rcParams['font.sans-serif'] = ['SimHei']          # 中文---------------------
plt.figure(figsize=(7.5, 5))                          # 图像大小
                                                      # startangle套数表示逆时针方向开始绘制的角度
                                                      # shadow表示是否显示阴影，explode表示突出显示某些切片
plt.pie(persons, labels=majors, colors=colors, startangle=90, shadow=True, explode=(0.1, 0, 0, 0,),
        autopct='%.1f%%', textprops={'fontsize': 15})
plt.title('各专业新生人数分布', fontsize=15, c='b')
plt.show()
"""
