# By：仰晨
# 文件名：del_excel_data_demo.py
# 时 间：2023/7/12 19:24

import pandas as pd


def one():
    # 读取Excel文件
    # df = pd.read_excel(r'E:\Users\Dell\Desktop\物料移动 (6) - 副本.xlsx', sheet_name="物料移动")
    df = pd.read_excel(r'E:\Users\Dell\Desktop\test.xlsx', sheet_name="物料移动")

    # 使用向前填充的方式填充“记帐日期”列中的空值
    df['记帐日期'] = df['记帐日期'].fillna(method='ffill')

    # 将“记帐日期”转换为日期格式
    df['记帐日期'] = pd.to_datetime(df['记帐日期'])

    # 删除“记帐日期”列中的值小于2023/7/1的行
    df = df[df['记帐日期'] >= '2023-07-01']

    # 将修改后的数据框导出为新的Excel文件
    df.to_excel(r'E:\Users\Dell\Desktop\物料移动666.xlsx', index=False)


def two():
    # 读取Excel文件
    # df = pd.read_excel(r'E:\Users\Dell\Desktop\物料移动 (6) - 副本.xlsx', sheet_name="物料移动")
    df = pd.read_excel(r'E:\Users\Dell\Desktop\test.xlsx', sheet_name="物料移动")

    # 将“记帐日期”转换为日期格式
    df['记帐日期'] = pd.to_datetime(df['记帐日期'], errors='coerce')

    # 删除“记帐日期”列中的值小于2023/7/1的行
    df = df[df['记帐日期'] >= '2023-07-01']

    # 将修改后的数据框导出为新的Excel文件
    df.to_excel(r'E:\Users\Dell\Desktop\物料移动666.xlsx', index=False)


def three():
    import numpy as np

    # 读取Excel文件
    # df = pd.read_excel(r'E:\Users\Dell\Desktop\物料移动 (6) - 副本.xlsx', sheet_name="物料移动")
    df = pd.read_excel(r'E:\Users\Dell\Desktop\test.xlsx', sheet_name="物料移动")

    # 将“记帐日期”转换为日期格式
    df['记帐日期'] = pd.to_datetime(df['记帐日期'], errors='coerce')

    # 找出与特定日期相同的索引
    indices = np.where(df['记帐日期'] >= pd.Timestamp('2023-07-01'))[0]

    # 根据索引保留原始数据的对应行
    df = df.loc[min(indices): max(indices) + 1]

    # 将修改后的数据框导出为新的Excel文件
    df.to_excel(r'E:\Users\Dell\Desktop\物料移动666.xlsx', index=False)


def foru():

    # 读取Excel文件
    # df = pd.read_excel(r'E:\Users\Dell\Desktop\物料移动 (6) - 副本.xlsx', sheet_name="物料移动")
    df = pd.read_excel(r'E:\Users\Dell\Desktop\test.xlsx', sheet_name="物料移动")

    # 将“记帐日期”转换为日期格式
    df['记帐日期'] = pd.to_datetime(df['记帐日期'], errors='coerce')

    # 找出与特定日期相同或大于的索引
    indices = df[df['记帐日期'] >= pd.Timestamp('2023-07-01')].index

    # 找出每个符合条件的日期下方的所有空值的索引
    indices_to_keep = []
    for idx in indices:
        indices_to_keep.extend(range(idx, df[df['记帐日期'].first_valid_index():idx].last_valid_index() + 2))

    # 根据索引保留原始数据的对应行
    df = df.loc[indices_to_keep]

    # 将修改后的数据框导出为新的Excel文件
    df.to_excel(r'E:\Users\Dell\Desktop\物料移动666.xlsx', index=False)


def five():

    # 读取Excel文件
    # df = pd.read_excel(r'E:\Users\Dell\Desktop\物料移动 (6) - 副本.xlsx', sheet_name="物料移动")
    df = pd.read_excel(r'E:\Users\Dell\Desktop\test.xlsx', sheet_name="物料移动")

    # 将“记帐日期”转换为日期格式
    df['记帐日期'] = pd.to_datetime(df['记帐日期'], errors='coerce')

    # 找出与特定日期相同或大于的索引
    indices = df[df['记帐日期'] >= pd.Timestamp('2023-07-01')].index

    # 找出每个符合条件的日期下方的所有空值的索引
    indices_to_keep = []
    for idx in indices:
        last_valid_index = df[df['记帐日期'].first_valid_index():idx].last_valid_index()
        if last_valid_index is not None:
            indices_to_keep.extend(range(idx, last_valid_index + 2))

    # 根据索引保留原始数据的对应行
    df = df.loc[indices_to_keep]

    # 将修改后的数据框导出为新的Excel文件
    df.to_excel(r'E:\Users\Dell\Desktop\物料移动666.xlsx', index=False)


# -----------------------成功-----------------比较慢
def six():

    # 读取Excel文件
    # df = pd.read_excel(r'E:\Users\Dell\Desktop\物料移动 (6) - 副本.xlsx', sheet_name="物料移动")
    df = pd.read_excel(r'E:\Users\Dell\Desktop\test.xlsx', sheet_name="物料移动")

    # 将“记帐日期”转换为日期格式
    df['记帐日期'] = pd.to_datetime(df['记帐日期'], errors='coerce')

    # 找出符合日期条件的行和它们下方的空日期行
    keep = False
    indices_to_keep = []
    for idx, row in df.iterrows():
        if pd.isna(row['记帐日期']):
            if keep:
                indices_to_keep.append(idx)
        else:  # 非空日期
            if row['记帐日期'] >= pd.Timestamp('2023-07-01'):
                keep = True
            else:
                keep = False
            if keep:
                indices_to_keep.append(idx)

    df = df.loc[indices_to_keep]

    # 将修改后的数据框导出为新的Excel文件
    df.to_excel(r'E:\Users\Dell\Desktop\物料移动666.xlsx', index=False)


# ---------------------------------------------------------
# -----------------------还是改改第一个快-----------------------
def one_plus(file_path):
    # 读取Excel文件
    df = pd.read_excel(file_path, sheet_name=0)

    # 使用向前填充的方式填充“记帐日期”列中的空值
    df['编号'] = df['编号'].fillna(method='ffill')
    df['生产工单'] = df['生产工单'].fillna(method='ffill')
    df['移动类型'] = df['移动类型'].fillna(method='ffill')
    df['记帐日期'] = df['记帐日期'].fillna(method='ffill')
    df['记帐时间'] = df['记帐时间'].fillna(method='ffill')
    df['数量'] = df['数量'].fillna(method='ffill')

    # 删除“记帐日期”列中的值小于2023/7/1的行
    # df = df[df['记帐日期'] >= '2023-07-01']
    df = df[df['记帐日期'] < '2023-07-11']

    # 将修改后的数据框导出为新的Excel文件
    df.to_excel(file_path.replace(".xlsx", "fill.xlsx"), index=False)


one_plus(r'E:\Users\Dell\Desktop\物料移动 (6).xlsx')
