# By：仰晨
# 文件名：折线图
# 时 间：2022/12/2 18:28

import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_excel('热榜合并.xlsx', sheet_name=0)
counts = data['发布地点'].value_counts().to_dict()
keys = [key for key in counts]
values = [counts[key] for key in counts]
# print(counts)
# print(keys)
# print(values)
# 有序不好看，打乱顺序---------
import random
tiem = [i for i in range(len(counts))]
random.shuffle(tiem)
ii = 0
for i in tiem:
    keys[ii], keys[i], values[ii], values[i] = keys[i], keys[ii], values[i], values[ii]
    ii += 1

# print(tiem)
# print(keys)
# print(values)

plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文
plt.figure(figsize=(10, 20), dpi=80)            # 画布
plt.title("B站热门榜单UP主发布地点", fontsize=30, fontweight=900)     # 图名字
# drawstyle='steps-post'尖角变方角
plt.plot(values, keys, '-', drawstyle='steps-post', color='r', marker='o')                    # 折线图
plt.plot(values, keys, ':', color='y', marker='<')                    # 折线图     markersize=50 点的大小
plt.show()                                              # 显示图
# f = plt.gcf()  # 获取当前图像
# f.savefig("pic/折线图", dpi=300)
# f.clear()  # 释放内存
# # 不能同时  保存  和  显示
