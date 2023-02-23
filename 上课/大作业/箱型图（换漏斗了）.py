# By：仰晨
# 文件名：箱型图
# 时 间：2022/12/3 2:03

import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel('热榜合并.xlsx', sheet_name=0)
counts = data['UP主'].value_counts().to_dict()
keys = [key for key in counts]
values = [counts[key] for key in counts]
# print(keys)
# print(values)

plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文
plt.figure(figsize=(10, 15), dpi=80)            # 画布
i = 0
text = 0
for value in values:
    if value > 1:
        plt.annotate(keys[i],  # 文本内容
                     xy=(1, value),  # 注释所在地
                     xytext=(1.1, value+0.3-text),  # 文本所在地
                     arrowprops=dict(arrowstyle="->"))  # 注释和文本的连接方式
        text += 0.05
    i += 1
plt.boxplot(values, showmeans=True)

plt.show()
