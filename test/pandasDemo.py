# By：仰晨
# 文件名：pandasDemo
# 时 间：2023/7/12 15:59
import pandas

df = pandas.read_excel(r"E:\Users\Dell\Desktop\问题收集表.xlsx", sheet_name=0)

# print(df)


print(df.loc[0])
print('------------------------')
df.loc[0,"问题解决人"]="hhh"
print(df.loc[0,"问题解决人"])

