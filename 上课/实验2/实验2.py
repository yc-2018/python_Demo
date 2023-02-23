# By：仰晨
# 文件名：实验2
# 时 间：2022/11/25 21:56

import pandas as pd
from sklearn import preprocessing

data = pd.read_excel("demo2.xlsx", sheet_name=1)  # 读取数据，第二个表

# 1111111111111111111111111111111111111111111111111111111111111111111111
data['level'] = data['level'].replace(0, 'others')
# print(data['level'])
# -----------------
# 获取LabelEncoder
le = preprocessing.LabelEncoder()
# 并训练LabelEncoder, 把High编码为0，Normal编码为1，Low为2，Other为3，others为4
le = le.fit(y=['others', 'Other', 'Low', 'Normal', 'High'])
datalevel = le.transform(data['level'])     # 这一列存在的 必须 le 定义
# print(datalevel)
# 22222222222222222222222222222222222222222222222222222222222222222222
# 数字索引代替了字符串类型的分类值  所以先转换成字符串 放在新的一列上
data['type_str'] = data['type'].astype(str)
# print(data)
OneHotEncode = data[['type_str']]  # ①单独将type_str列拿出来
OneHotEncode_data = pd.get_dummies(OneHotEncode)  # ②转换
# print(data[['type_str']])
# 限制 pandas显示的行列数
pd.options.display.max_rows = 4     # 行
pd.options.display.max_columns = 40  # 列
# print(OneHotEncode_data)  # ③打印
# 33333333333333333333333333333333333333333333333333333333333333333333
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns
data1 = data[['total_visits']].sample(frac=0.8)     # 随机抽样80%
plt.plot(data1)
plt.show()  # 未归一图
# 归一化
scales_mm = MinMaxScaler()
data_rn_new = scales_mm.fit(data1).transform(data1)
plt.plot(data_rn_new)
plt.show()      # 归一图
sns.distplot(data_rn_new)   # 归一直方图
plt.show()
# 44444444444444444444444444444444444444444444444444444444444444444444
pd.options.display.max_columns = 40  # 列
data.drop('orders', axis=1, inplace=True)
print(data.head(5))
# 5555555555555555555555555555555555555555555555555555555555555555555
# print('先看看均值是：', data['action_amount'].mean())
# 均值填充
data['action_amount'] = data['action_amount'].fillna(data['action_amount'].mean())
# print(data['action_amount'].head(20))
# 666666666666666666666666666666666666666666666666666666666666666666666666666

data['log_in_week'] = data['log_in_time'].dt.dayofweek
data['log_in_week'] = data['log_in_week'].replace(0, '星期一').replace(1, '星期二').replace(2, '星期三').replace(3, '星期四')\
                                         .replace(4, '星期五').replace(5, '星期六').replace(6, '星期天')
# print(data[['log_in_week', 'log_in_time']])
# 月份
data['log_in_month'] = data['log_in_time'].dt.month
# print(data[['log_in_month', 'log_in_time']])
# 日期
data['log_in_date'] = data['log_in_time'].dt.date
# print(data[['log_in_date', 'log_in_time']])

# 时间
data['时间'] = data['log_in_time'].dt.time
# print(data[['时间', 'log_in_time']])

data.to_excel('实验2后.xlsx', index=False)
print('输出完成')



