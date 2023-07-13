# By：仰晨
# 文件名：向上填充excel
# 时 间：2023/7/13 11:37
import pandas as pd
df = pd.read_excel(r'E:\Users\Dell\Desktop\物料移动7月1-10号结果.xlsx', sheet_name=0)

# 使用向前填充的方式填充“记帐日期”列中的空值
df['编号'] = df['编号'].fillna(method='ffill')
df['生产工单'] = df['生产工单'].fillna(method='ffill')
df['移动类型'] = df['移动类型'].fillna(method='ffill')
df['记帐日期'] = df['记帐日期'].fillna(method='ffill')
df['记帐时间'] = df['记帐时间'].fillna(method='ffill')
df['数量'] = df['数量'].fillna(method='ffill')

df.to_excel(r'E:\Users\Dell\Desktop\物料移动7月1-10号结果fill.xlsx', index=False)
