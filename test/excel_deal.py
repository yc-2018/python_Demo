# By：仰晨
# 文件名：excel_deal
# 时 间：2023/7/12 16:12
import pandas as pd


def date_compare(date2):
    print(f"2023-07-01 00:00:00 > {str(date2)}")
    return "2023-07-01 00:00:00" > str(date2)


# df = pd.read_excel(r'E:\Users\Dell\Desktop\物料移动 (6) - 副本.xlsx', sheet_name=0,usecols="D",nrows=4)
# df = pd.read_excel(r'E:\Users\Dell\Desktop\test.xlsx', sheet_name="物料移动", usecols="D",nrows=4)
df = pd.read_excel(r'E:\Users\Dell\Desktop\物料移动 (6) - 副本.xlsx', sheet_name="物料移动", usecols="D", nrows=4)
for index, row in df.iterrows():
    if (not pd.isna(row['记帐日期']) and date_compare(row['记帐日期'])):
        print(type(row['记帐日期']))
