# By：仰晨
# 文件名：pandas库
# 时 间：2022/10/17 23:58

# to_excel每次运行会覆盖上一次生成的文件
import pandas as pd

# 创建
df = pd.DataFrame({"ID": [1, 2, 3], "Name": ['diaomao', 'ikun', 'dddd']})     # 创建一列叫ID的有列下有1 2 3  创建一列为name下面有三个数据
print(df)
df = df.set_index('ID')       # 设定索引列为ID那列列
df.to_excel("put.xlsx")       # 输出---覆盖或新建一个表
"""   
      ID     Name
0      1  diaomao
1      2     ikun
2      3     dddd
"""


print('-------------------------------------------')

# '环比':
sm = pd.Series([101.5, 101.2, 101.3, 102.0, 100.1], index=['c1', 'c2', 'c3', 'c4', 'c5'])
print(sm)
print('--------------')
dl = {'城市': pd.Series(['北京', '上海', '广州', '深圳', '沈阳']),
      '环比': pd.Series([101.5, 101.2, 101.3, 102.0, 100.1]),
      '同比': pd.Series([120.7, 127.3, 119.4, 140.9, 101.4]),
      '定基': pd.Series([121.4, 127.8, 120.0, 145.5, 101.6])}
date = pd.DataFrame(dl)
print(date)
