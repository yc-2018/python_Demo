# By：仰晨
# 文件名：利用箱线图检测
# 时 间：2022/11/24 17:26

import pandas as pd  # ①
import numpy as np  # ①导入numpy库
import matplotlib.pyplot as plt


data = pd.read_excel('demo2.xlsx', sheet_name=1)
d1 = data.iloc[:, [3]]
print(d1)
# plt.boxplot(d1,whis=15,showmeans=True)         # 默认垂直显示
# plt.boxplot(d1, vert=False,whis=20)  # 水平显示
f = d1.boxplot(sym='o',  # 异常点形状
               vert=True,  # 是否垂直
               whis=5,  # IQR，# 上下四分位的距离，默认为1.5倍的四分位差；
               patch_artist=True,  # 上下四分位框是否填充
               meanline=False, showmeans=True,  # 是否有均值线及其形状
               showbox=True,  # 是否显示箱线
               showfliers=True,  # 是否显示异常值
               notch=False  # 中间箱体是否缺口
               )  # 返回类型为字典
plt.show()
"""报警告
MatplotlibDeprecationWarning:不支持required_interactive_framework属性的FigureCanvases在Matplotlib 3.6中已弃用，并将在之后的两个次要版本中删除。
plt.show ()
"""