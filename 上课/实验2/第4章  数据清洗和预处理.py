# By：仰晨
# 文件名：实验2_综合性数据预处理
# 时 间：2022/11/22 16:19--11/25 02：59

import pandas as pd
import numpy as np

data = pd.read_excel("demo2.xlsx", sheet_name=1)  # 读取数据，第二个表
# 行
print(data.head(3))  # 查看前3行，默认为5
print(data.tail(4))  # 查看最后4行，默认为5
print(data[3:11])  # 查看3到10行的数据
print(data[3:11][0:3])  # 查看3到10行的数据,然后把查的当做0-7行，然后查看0到2行

# 行 and 列
print(data.iloc[0:10, 0:4])  # 查看0到9行的0到3列
print(data.iloc[0:10, [0, 6]])  # 查看0到9行的第0列和第6页
print(data.iloc[0:10:2, 0:6:2])  # 查看0到9行步长为2 的第0列和第6页步长为2

print(data.loc[3:11, ['level', 'ID']])  # 查看3到10行 的level列 和 ID列   如果只看一列就不要列表
print(data.loc[:, ['level', 'ID']])  # 查看所有行 的level列 和 ID列

print(data.at[3, 'type'])  # 查看第三横 type列的数据
print(data.iat[3, 4])  # 查看3行4列的数据

# ------------2------审核数据类型-------------------------------------
print(data.dtypes)  # 查看每一列的数据类型

# -----------3-----分析数据分布趋势------------------------------------
"""
查看所有数据列的数据分布情况,数值数据小数保留两位有效位
datetime_is_numeric=True 取消警告不是数字处理已被弃用
percentiles=[0, .25, .5, .88, 1]设定数值型特征的统计量  表示百分位数，介于o和1之间。默认值为 [.25,.5,.75].分别返回第25，第50和第75百分位数。
include:all，类似于dtypes列表或None(默认值)，可选包含在结果中的数据类型的白名单，对于Series不可用。
        al1': 输入的所有列都将包含在输出中。类似于dtypes的列表: 将结果限制为提供的数据类型.
        numpy.number:将结果限制为数字类型用法。
        numpy.object: 将其限制为对象列用法。
        字符串 df.describe(include=['o'])
        默认仅统计分析数值类型数据
exclude: 类似于dtypes列表或None(默认值) ，可选从结果中除去的黑名单数据类型列表。Series不可用。以下是选项:
        类似于dtypes的列表: 从结果中排除提供的数据类型。
        无(默认) : 结果将不包含任何内容
"""
print(data.describe(include='all', datetime_is_numeric=True, percentiles=[0, .25, .5, .88, 1]).round(2))
print('----------------------------')
print(data.describe(include=object).round(2))  # 查看object（字符串）类型的数据分布情况
print('--------------------------------------')
print(data.describe(exclude=object, datetime_is_numeric=True).round(2))  # 查看不是object类型的数据分布情况
print('-----np.number-------')
print(data.describe(include=[np.number]).round(2))
print('-------查看<=25%, >25%且<=50%,>50%且<75%的数据--------')
print(data.describe(percentiles=[.25, .75]).round(2))
print(data.describe(percentiles=[.25]).round(2))  # 查看<=25%, >25%且<=50%数据分布
print(data.describe(percentiles=[.25, .50]).round(2))
print(data.describe(include=[np.number]).round(2))

# -------4---数据清洗------------------------------------------
print("数据清洗的主要规则包括： 空值的检查和处理、 非法值的检测和处理、 不一致数据的检测和处理、 相似重复记录的检测和处理。")
print("1、预处理---选择数据处理工具---查看数据的元数据即数据特征")
print("2、空值缺失值清洗---确定缺失值范围---去除不需要的字段---填充缺失之内容：（均值、中位数、众数等）填充；（如推算年龄、邮件编码）")
print("3、格式与内容清洗---可能存在格式和内容不一致的情况")
print("4、逻辑错误清洗---数据去重---去掉不合理的值---去掉不可靠的字段值---对来源不可靠的数据重点关注")
print("5、多余的数据清洗---清洗不需要的数据时，将影响模型构建不必要的字段删除，以达到最好的模型效果，最好考虑备份原始数据。")
print("6、关联性验证---数据有多个来源，有必要进行关联性验证，用以选择准确的特征属性。")
print("""空值和缺失值处理
        ·一般空值使用None表示，缺失值使用NaN表示。
        ·isnull()函数↓会返回一个布尔类型的值，如果返回的结果为True，则说明有空值或缺失值，否则为False。（NaN或None映射到True值，其它内容映射到False）
        """)
print(data.isnull())
print("---isnull()函数可以直接判断某列中的哪个数据为NaN或None ，利用isnull().sum()可以统计空值和缺失值的缺失数目。")
print(data.isnull().sum(), type(data.isnull().sum()))
print("***************·axis=1为横向，axis=0为纵向，而不是行和列---**********************************************************")
print(data.isnull().any(axis=1))  # 获取每行是否包含NA判断结果
print(data.isnull().any(axis=1)[data.isnull().any(axis=1)] == True)  # NA记录的行号

# 更加明确地查看缺失值行列信息
print(data.columns[6])
print(len(data), "长度")
for 列名 in data.columns:
    if data[列名].count() != len(data):  # 这一列有内容的数量  不等于   表列的总长   才执行   //等于就代表没有缺失值
        loc = data[列名][data[列名].isnull().values == True].index.tolist()
        print(f'列名："{列名}", 第{loc}行位置有缺失值')

# 查看缺失值列（补充）----------------------------------------------------------------数据填充---------------
print(data.isnull().any())  # 获取NA列的总数量
print(data.isnull().any()[data.isnull().any()] == True)  # NA记录的列号

"""
缺失值所在的特征为数值型时，通常利用其均值、中位数和众数等描述其集中趋势的统计量来填充；
缺失值所在特征为类别型数据时，则选择众数来填充。
Pandas库中提供了缺失值替换的方法fillna，格式如下：DataFrame.fillna(value=None, method=None, axis=None, inplace=False, limit=None)

参数名称	参数说明
value	用于填充缺失值的标量值或字典对象----（“其他”）这种方式常用于将缺失值表示为一种规律，而非随机因素
method	插值方式
axis	待填充的轴，默认axis=0
inplace	修改调用者对象而不产生副本
limit	(对于前向和后向填充)可以连续填充的最大数量
"""
print(data[["action_amount"]].fillna("未知"))
"""
data['age'] = data['age'].fillna(0) # 用0填充
data['age'] = data['age'].fillna(data['age'].mean()) # 均值填充
data['age'] = data['age'].fillna(method='pad') # 用前一个数据填充
data['age'] = data['age'].fillna(method='bfill') # 用后一个数据填充
data['age'] = data['age'].interpolate(method='linear') # 用差值法填充，可指定不同的方法

"""

# -----------------丢弃缺失值--------------------------------
data.dropna()
"""
丢弃缺失值是直接将含有NA值的记录丢弃，适用于NA值的记录较少，且整体样本量较大的情况。
dropna方法的格式：dropna(axis=0, how=‘any’, thresh=None, subset=None,  inplace=False) 
    data_dropna = data.dropna(axis=0, how='any',subset=['level'],thresh=2)
    data_dropna = data.dropna(axis=0, how='any',subset=['level'],thresh=2,inplace=True)
        参数名称	                使用说明
        axis 	    默认为axis=0，当某行出现缺失值时，将该行丢弃并返回，当axis=1，当某列出现缺失值时，将该列丢弃
        how	        表示删除的形式。any表示只要有缺失值存在就执行删除操作。all表示当且仅当全部为缺失值时执行删除操作。默认为any。
        thresh	    阈值设定，当行列中非空值的数量少于给定的值就将该行丢弃
        subset      表示进行去重的列∕行      如：subset=[’a’ ,’d’], 即丢弃子列 a d 中含有缺失值的行
        inplace     是否原地替换。布尔值，默认为False，即创建新的对象进行修改，原对象不变。如果为True，则在原DataFrame上进行操作，返回值为None。
        
            示例
            data.dropna(axis=0,how='any') # 按行删除：该行只要存在缺失值，即删除该行 

            data.dropna(axis=0,how='all') # 按行删除：该行的所有值缺失，即删除该行

            data.dropna(axis=1,thresh=5) # 按列删除：该列非空元素小于5个的，即删除该列

            data.dropna(axis=1,how='all',subset=[2,3]) # 设置子集：删除第2，3列都为空的行

            data.dropna(axis=0,how='any',inplace=True) # 按行删除：该行只要存在缺失值，即删除该行，直接在原数据文件中删除
"""

# ---------------1.基于经验值的判断和选择----------------
"""
数据中的age，属于有订单的人群的年龄，一般是在0-100之间，因此可基于该方法直接选择该区间内的数据，从而实现去除异常数据的目的
"""
data_sets = data[(data['type'] > 10) & (data['type'] <= 100)]
print(data_sets.head(25))

# ---------------判断重复值-----------------------------------
"""
重复值是出现在数据中值相同的记录，重复的记录大多意味着数据采集重复或存储问题。
在DataFrame中利用duplicates方法判断各行是否有重复数据。
duplicates方法返回一个布尔值的series，反映每一行是否与之前的行重复。
用法示例：
"""
print(data[data.duplicated()])
print(data['type'].duplicated())  # 重复值的第一个必然为False  后面再有才为True

# ------------去除重复值-------------------------------
"""
使用drop_duplicates方法去重时，当且仅当subset参数中的特征重复时候才会执行去重操作，去重时可以选择保留哪一个或者不保留。
默认保留的数据为第一个出现的记录，通过传入keep = 'last'可以保留最后一个出现的记录。
用法示例：
"""
data_dropduplicates = data.drop_duplicates()
"""     参数名称	                使用说明
        subset	    接收string或sequence，表示进行去重的列，默认全部列
        keep	    接收string，表示重复时保留第几个数据，‘first’保留第一个，
                    ‘last’保留最后一个，‘false’只要有重复都不保留，默认为first
        inplace	    接收布尔型数据，表示是否在原表上进行操作，默认为False"""


# -----------随机抽样--------------------
'''随机抽样即随机的抽取样本，可使用数据框的sample实现，并可通过参数n设置指定抽样数量，或通过frac指定抽样比例
'''
data_sample1 = data.sample(n=1000)    # 指定抽样数量为1000
data_sample2 = data.sample(frac=0.8)  # 指定抽样比例为80%

# -----------分层抽样-----------------------
'''
·分层抽样是根据不同的目标（一般是分类型字段），等比例抽样每个类别内的样本，保持抽样后的样本的目标分布相对于整体分布是等比例的
·这种方法的优点是，样本的代表性比较好，抽样误差比较小。缺点是抽样手续较简单随机抽样还要繁杂些。定量调查中的分层抽样是一种卓越的概率抽样方式，在调查中经常被使用。
'''


def sub_sample(data, group_name):  # ①定义一个名为sub_sample的函数
    return data[data['level'] == group_name].sample(frac=0.8)  # ②基于group_name按80%随机抽样


names = data['level'].unique()  # ③获得唯一level值域
all_samples = [sub_sample(data, group_name) for group_name in names]  # ④通过列表推导式获取所有抽样后的结果列表，列表中每个元素都是一个抽样后的数据框
print(all_samples)
print('------------------------------------------------------------------')
samples_pd = pd.concat(all_samples, axis=0)  # ⑤将列表内的数据框组合起来
print(samples_pd)

'''
def sub_sample1(data,group_name):
    return data[data[['level','sex']]==group_name].sample(frac=0.8)
    
names2=data['sex'].unique()
all_samples2=[sub_sample(data,group_name) for group_name in names2]
samples_pd2=pd.concat(all_samples2,axis=0)

names2=data['sex'].unique()
all_samples2=[sub_sample(data,group_name) for group_name in names2]
samples_pd2=pd.concat(all_samples2,axis=0)

print(samples_pd.groupby(['level'],as_index=False)['user_id'].count().T)
print(samples_pd.groupby(['sex'],as_index=False)['user_id'].count().T)
'''

# -----------字符串转日期----------------------
'''字符串和日期的转换，可通过time或datetime库的strptime和strftime实现
'''
"""
print(data['recent_date'].dtype)
data['recent_date'] = [pd.datetime.strptime(i, '%Y/%m/%d %H:%M:%S') for i in data['recent_date']]
print(data['recent_date'].dtype)
"""

# 多表合并
"""
files = [pd.read_excel(os.path.join("./", file)) for file in os.listdir("./") if file.endswith('热榜.xlsx')]
data = pd.concat(files)
---若Excel表中存在多个Sheet表，需指定需要合并的Sheet表名
files = [pd.read_excel(os.path.join(target_dir, file), sheet_name='demo') for file in os.listdir(target_dir) if file.endswith('.xlsx')]
---选择所需要的列，如果是一列，则只需传入一个列名；如果同时选择多列，则传入多个列名即可，多个列名用列表形式封存
files = [pd.read_excel(os.path.join(target_dir, file), sheet_name='demo')[['date','city']] for file in os.listdir(target_dir) if file.endswith('.xlsx')]
---如果多个excel文件中的列名一致，则不需此项
"""