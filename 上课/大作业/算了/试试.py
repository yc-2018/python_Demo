# By：仰晨
# 文件名：试试
# 时 间：2022/11/30 23:52

import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_excel('../热榜合并.xlsx', sheet_name=0)
counts = data['发布地点'].value_counts()
print(counts)














