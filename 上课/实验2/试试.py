# By：仰晨
# 文件名：试试
# 时 间：2022/11/22 21:48
import pandas as pd

data = pd.read_excel("demo2.xlsx", sheet_name=1)  # 读取数据，第二个表


# print(data["level"].count())
# print(data["ID"].count())
# print(data["type"].count())
# print(data["log_in_time"].count())
# print(data["orders"].count())
# print(data["orders"][data["orders"].isnull().values == True].index)

# 查看缺失值列（补充）
# print(data.isnull().any())    # 获取NA列的总数量
# print('-'*100)
# print(data.isnull().any()[data.isnull().any()] == True)     # NA记录的列号

# na_records = data[['action_amount']].isnull().any(axis=1)
# print(na_records[na_records]==True)
# print('*'*100)
# na_records = data[['action_amount','level']].isnull().any(axis=1)
# print(na_records[na_records]==True)

# var = data.loc[:, 'level'].tolist()
# print(var)

# print(data.iloc[3:5, 0:6])

# data[["action_amount"]]=data[["action_amount"]].fillna("未知")
# data.to_excel('ss.xlsx')
# n=data[["action_amount"]].isnull().any()
# print(n)

# print(data["action_amount"].fillna(method='pad'))
# print(data["action_amount"])
# data.dropna(axis=0, how='any', inplace=True)
# print(data.iloc[3,1])
# print(data.plot())
# import numpy as np
#
# wdf = pd.DataFrame(np.arange(20), columns=['W'])
# wdf['Y'] = wdf['W'] * 1.5 + 2
# wdf.iloc[3, 1] = 128
# wdf.iloc[18, 1] = 150
# wdf.plot(kind='scatter', x='W', y='Y', c='red')
# data_sets = data[(data['type'] > 10) & (data['type'] <= 100)]
# print(data_sets.iloc[0:25, 1:4])
# print(data.drop_duplicates(subset="level"))

# print(data['type'].unique())
# data_sample1 = data.sample(n=10)    # 指定抽样数量为1000
# data_sample2 = data.sample(frac=0.8)  # 指定抽样比例为80%
#
# print(data_sample1)
# print('-------------------------------------------------------')
# print(data_sample2)
import numpy as np

import datetime

# import matplotlib.pyplot as plt
#
# data1=data[['type']].sample(n=1000)
# print(data1)
# plt.subplots(figsize=(10, 4))
# # figsize用来设置图形的大小，a为图形的宽， b为图形的高，单位为英寸。
# plt.subplot(1, 2, 1)
# # subplot(nrows子图的行数, ncols子图的列数, plot_number索引值，表示把图画在第plot_number个位置（从左下角到右上角）)
# plt.plot(data1)
# plt.show()

# print(data['log_in_time'].dtype)
# data['log_in_time'] = [datetime.datetime.strptime(i, '%Y/%m/%d %H:%M:%S') for i in data['log_in_time']]
# print('*'*100)
# print(data['log_in_time'].dtype)
#
# from sklearn import preprocessing
# sex = pd.Series(["male", "female", "female", "male"])
# print('-------------------------------------------------')
#
# le = preprocessing.LabelEncoder()    #获取一个LabelEncoder
# le = le.fit(["male", "female"])      #训练LabelEncoder, 把male编码为0，female编码为1
#
# sex = le.transform(sex)                #使用训练好的LabelEncoder对原数据进行编码
# print(sex)

# s1=['a','b',np.nan]
# print(s1)
data11 = pd.DataFrame({"学号":[1,2,3,4],
                    "录取":["清华","北大","清华","蓝翔"],
                    "学历":["本科","本科","本科","专科"]})
print(data11)
print('------------------------------------------------')
print(pd.get_dummies(data11))
"""   
   学号  录取  学历
0   1  清华  本科
1   2  北大  本科
2   3  清华  本科
3   4  蓝翔  专科
------------------------------------------------
   学号  录取_北大  录取_清华  录取_蓝翔  学历_专科  学历_本科
0   1      0      1      0      0      1
1   2      1      0      0      0      1
2   3      0      1      0      0      1
3   4      0      0      1      1      0

"""
