# By：仰晨
# 文件名：基于分位数的判断和选择
# 时 间：2022/11/24 18:45
import pandas as pd
import numpy as np

data = pd.read_excel("demo2.xlsx", sheet_name=1)  # 读取数据，第二个表


def process_outlier(sub_data, each_col):    # ①
    desc = sub_data.describe().T            # ②
    per_25 = desc['25%'].values[0]          # ③ 定义25%分位数边界值
    per_75 = desc['75%'].values[0]          # ④ 定义75%分位数边界值
    spacing = per_75 - per_25               # ⑤ 计算75%-25%分位数间距
    scope_min, scope_max = per_25 - 1.5 * spacing, per_75 + 1.5 * spacing                   # ⑥ 定义正常数据分布范围边界
    is_outlier = (sub_data[each_col] < scope_min) | (sub_data[each_col] > scope_max)        # ⑦
    sub_data[is_outlier] = desc['mean'].values[0]   # ⑧
    print(desc['mean'].values[0])
    print(np.sum(is_outlier))                       # ⑨
    return sub_data                                 # ⑩


data['type'] = process_outlier(data[['type']], 'type')
print('---------------------------------------------')
print(data['type'])

"""带有复制警告的设置:
在DataFrame切片的副本上尝试设置一个值。
请尝试使用。loc[row_indexer,col_indexer] = value代替
请参阅文档中的注意事项:https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
Sub_data [is_outlier] = desc['mean']。值[0]#⑧
"""