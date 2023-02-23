# By：仰晨
# 文件名：数据标准化和归一化
# 时 间：2022/11/25 2:24
import pandas as pd
import matplotlib.pyplot as plt     # 要3.6及一下的
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
import matplotlib as mpl
import seaborn as sns


data = pd.read_excel("demo2.xlsx", sheet_name=1)  # 读取数据，第二个表

data1=data[['type']].sample(n=1000)
print(data1)
plt.subplots(figsize=(10, 4))
# figsize用来设置图形的大小，a为图形的宽， b为图形的高，单位为英寸。
plt.subplot(1, 2, 1)
# subplot(nrows子图的行数, ncols子图的列数, plot_number索引值，表示把图画在第plot_number个位置（从左下角到右上角）)
plt.plot(data1)
plt.show()              # 1111111111111111111111111111111111111
"""
E:/Pycharm/上课/实验2/数据标准化和归一化.py:11: MatplotlibDeprecationWarning:在Matplotlib 3.6中，不支持required_interactive_framework属性的figurecanases已被弃用，并将在之后的两个次要版本中删除。
plt。次要情节(figsize = (10, 4))
E:/Pycharm/上课/实验2/数据标准化和归一化.py:13: MatplotlibDeprecationWarning:自动删除重叠轴自3.6起已弃用，并将在两个次要版本后被删除;需要时显式调用ax.remove()。
plt。子图(1,2,1)
E:/Pycharm/上课/实验2/数据标准化和归一化.py:16: MatplotlibDeprecationWarning:在Matplotlib 3.6中不支持没有required_interactive_framework属性的figurecanases，并将在之后的两个次要版本中删除。
plt.show ()
"""

# 归一化
scales_mm = MinMaxScaler()
data_rn_new = scales_mm.fit(data1).transform(data1)
# 标准化
scales_ss = StandardScaler()
data_rn_new1 = scales_ss.fit(data1).transform(data1)

plt.subplots(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(data_rn_new)
plt.show()  # 归一化图      # 2222222222222222222222222222222222222222
plt.subplot(1, 2, 2)
plt.plot(data_rn_new1)
plt.show()  # 标准化图      # 3333333333333333333333333333333333333333


# 5.数据标准化和归一化完整实例（用图形表示结果）
plt.subplots(figsize=(10, 4))   # 指定绘图区为(10,4)
plt.subplot(1, 2, 1)
sns.distplot(data_rn_new)   #直方图
plt.show()                  # 44444444444444444444444444444444444444
plt.subplot(1, 2, 2)
sns.distplot(data_rn_new1)
plt.show()                  # 555555555555555555555555555555555555555












