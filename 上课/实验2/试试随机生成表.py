# By：仰晨
# 文件名：试试1
# 时 间：2022/11/24 16:52

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(4, 3), columns=["A", "B", "C"])
data = df.drop(["A"], axis=1, inplace=True)
print(data)  # 是否原地替换。布尔值，默认为False，即创建新的对象进行修改，原对象不变。如果为True，则在原DataFrame上进行操作，返回值为None。
print(df)

print('---------------------------------------------')

df = pd.DataFrame(np.random.randn(4, 3), columns=["A", "B", "C"])  # randn(4,3)   4行3列
data = df.drop(["A"], axis=1, inplace=False)
print(data)
print(df)
