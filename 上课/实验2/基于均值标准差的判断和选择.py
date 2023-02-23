# By：仰晨
# 文件名：基于均值标准差的判断和选择
# 时 间：2022/11/24 18:25

"""
该方法基于不同字段的均值和标准差求出异常数据分布范围，然后再对异常范围外的数据做处理，例如填充为均值
"""
import pandas as pd
import numpy as np  # ①导入numpy库

data = pd.read_excel("demo2.xlsx", sheet_name=1)  # 读取数据，第二个表


def process_outlier(sub_data, each_col):  # ②定义一个名为process_outler的函数
    _mean = sub_data[each_col].mean()  # ③计算均值
    print("打印均值", _mean)
    _std = sub_data[each_col].std()  # ④计算标准差
    scope_min, scope_max = _mean - 2 * _std, _mean + 2 * _std  # ⑤计算均值±2倍标准差的边界值
    is_outlier = (sub_data[each_col] < scope_min) | (sub_data[each_col] > scope_max)  # ⑥定义异常条件
    sub_data[is_outlier] = _mean  # ⑦将异常值用均值重写
    print(np.sum(is_outlier))  # ⑧打印异常的记录数量
    return sub_data  # ⑨返回处理后的数据


data['type'] = process_outlier(data[['type']], 'type')  # 处理orders列
print(data['type'])


"""
带有复制警告的设置:
在DataFrame切片的副本上尝试设置一个值。
请尝试使用。loc[row_indexer,col_indexer] = value代替
请参阅文档中的注意事项:https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
Sub_data [is_outlier] = _mean #⑦将异常值用均值重写
"""