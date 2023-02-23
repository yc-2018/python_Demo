# By：仰晨
# 文件名：data cleansing
# 时 间：2022/11/22 12:57
"""
数据清洗：解决格式、单位、冗余问题。
数据预处理：处理缺失值、异常值等数据的过程。大部分机器学习模型不支持缺失值或对异常值敏感，所以预处理可以保证模型的准确性。"""

import pandas as pd
import os

# 项目数据清洗要求
# 把全部热榜合并成一个新的表
files = [pd.read_excel(os.path.join("./", file)) for file in os.listdir("./") if file.endswith('热榜.xlsx')]
data = pd.concat(files)

# 排行和视频链接这两列是不需要的删除
data.drop(["排名", "视频链接"], axis=1, inplace=True)

# 视频名这列合并会有锁屏会在多个榜单上的，所以会存在重复值，
data.drop_duplicates("视频名", inplace=True)

# # 检查是否有空值
# print(data["发布地点"].isnull().value_counts())

# 发布地点存在空字符串，全部填充为“未知”
data["发布地点"].fillna("未知", inplace=True)

# 查看统计信息
print(data.describe())

# 把处理好的数据进行输出
data.to_excel('热榜合并.xlsx', index=False)

# print(data.head(10))
