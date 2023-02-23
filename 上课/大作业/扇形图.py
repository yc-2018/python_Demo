# By：仰晨
# 文件名：扇形图
# 时 间：2022/11/30 23:43

# 2. plt.pie绘制扇形图

import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_excel('热榜合并.xlsx', sheet_name=0)
counts = data['分辨率'].value_counts().to_dict()
# print(counts)
# 统计视频分辨率个数，小于10个的归并到其他类别
分辨率list = []
统计数list = []
其他 = 0
for key in counts:
    if counts[key] > 10:
        分辨率list.append(key)
        统计数list.append(counts[key])
    else:
        其他 += counts[key]
分辨率list.append("其他分辨率")
统计数list.append(其他)
print(分辨率list)
print(统计数list)

plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文
labels = 分辨率list                                                # 每个版块的名字
sizes = 统计数list                                                # 每个版块的大小
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', '#95E1D3',
          '#F3D7CA', '#E6A4B4', '#C86B85', '#B9D7EA']    # 每个版块的颜色
explode = 0.05, 0, 0, 0, 0, 0, 0, 0, 0.1                           # 每个版块的间隙 （逆时针）
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=50)
plt.axis('equal')                                               # x,y轴刻度等长
plt.show()                                                      # 输出图
# # 不能同时  保存  和  显示
# f = plt.gcf()  #获取当前图像
# f.savefig("pic/扇形图", dpi=300)
# f.clear()  # 释放内存
