# By：仰晨
# 文件名：全热门榜平均播放量柱形图
# 时 间：2022/11/29 3:07
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def 平均播放量(文件名):
    data = pd.read_excel(文件名, sheet_name=0)  # 读取数据，第1个表
    播放量list = data['播放量'].tolist()

    sun = 0
    for z in 播放量list:
        sun += z

    return int(sun / len(播放量list)/10000)


xlsx_name = ["全站综合热榜.xlsx",
             "动画热榜.xlsx",
             "音乐热榜.xlsx",
             "舞蹈热榜.xlsx",
             "游戏热榜.xlsx",
             "知识热榜.xlsx",
             "科技热榜.xlsx",
             "运动热榜.xlsx",
             "汽车热榜.xlsx",
             "生活热榜.xlsx",
             "美食热榜.xlsx",
             "动物热榜.xlsx",
             "鬼畜热榜.xlsx",
             "时尚热榜.xlsx",
             "娱乐热榜.xlsx",
             "国创相关热榜.xlsx"]
# 柱状图
avs_view_counts = [平均播放量(文件名) for 文件名 in xlsx_name]
# print(avs_view_counts)
name = [s.split("热榜")[0] for s in xlsx_name]
# print(name)
len_s = [i for i in range(len(xlsx_name))]
# print(len_s)
# ----------------------------------------------------------
plt.figure(figsize=(20, 12), dpi=300)       # ----设置画布 在.bar前
plt.tick_params(axis='x', labelsize=16)      # ----设置x轴标签大小
plt.xticks(rotation=-15)                    # ----设置x轴标签旋转角度

for y in range(len(avs_view_counts)):
    plt.text(y-0.2, avs_view_counts[y]+1, f"{avs_view_counts[y]}万")

x = np.arange(len(xlsx_name))   # 总共有几组，就设置成几
plt.bar(x, avs_view_counts, color='c', edgecolor='k')     # 每条柱子的高的数据  .barh就是横纵颠倒
plt.title("B站各个热门榜单的平均播放量/万", fontsize=30, fontweight=900)
plt.xlabel("榜单名称", fontsize=20, fontweight=900, color="b")            # X轴名字 字体大小 加粗100-900 颜色
plt.ylabel("平均播放量（万）", fontsize=20, fontweight=900, color="b")          # Y轴名字
plt.xticks(len_s, name)         # 柱子的序号 和名字  数量要对应
plt.ylim((10, 300))      # y轴显示是最小值和最大值
plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文


# f = plt.gcf()  #获取当前图像
# f.savefig("pic/柱形图", dpi=300)
# f.clear()  # 释放内存
# 不能同时  保存  和  显示
plt.show()
