# By：仰晨
# 文件名：散点图
# 时 间：2022/12/2 22:50
# 4.绘制散点图

import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel('热榜合并.xlsx', sheet_name=0)
data['时长（秒）'] = data['时长（秒）']/60                                        # 转化为分钟
counts = data['时长（秒）'].values.tolist()
# print(counts)
plt.figure(figsize=(8, 10))     # 尺寸
plt.ylim((1, 20))               # y轴显示是最小值和最大值
plt.plot(counts, 'o', c='c')    # 表示绘制散点图，且为蓝色圆标记
plt.rcParams['font.sans-serif'] = ['SimHei']                                    # 中文
plt.title("B站热门榜单播放时长", fontsize=30, fontweight=900)
plt.xlabel("数据数量", fontsize=20, fontweight=900, color="b")                  # X轴名字 字体大小 加粗100-900 颜色
plt.ylabel("播放时长（分钟）", fontsize=20, fontweight=900, color="b")            # Y轴名字
# f = plt.gcf()  #获取当前图像
# f.savefig("pic/散点图", dpi=300)
# f.clear()  # 释放内存
# 不能同时  保存  和  显示
plt.show()
