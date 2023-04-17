# By：仰晨
# 文件名：水果数据集
# 时 间：2023/4/17 20:20
"""
1.水果数据集由爱丁堡大学的Iain Murray博士创建。他买了几十个不同种类的橘子、橙子、柠檬和苹果，并把他们的尺寸记录在一张表格中。
本实验对水果数据进行简单预处理，存为素材文件fruit_data.txt。文件中包含59个水果的测量数据。每行表示一个待测定水果，每列为一个特征。特征从左到右依次
如下：
fruit_label：标记值，表示水果的类别，1-苹果，2-橘子，3-橙子，4-柠檬。
mass：水果的重量。
width：测量出的宽度。
height:测量出的高度。
color_score：颜色值。
本实验要求使用SKlearn的neighbors模块，对水果数据进行KNN分类，然后预测下表中A、B两种水果的类别。
样本	    mass    width	 heigth  	color_score
 A	    192   	 8.4	  7.3	       0.55
 B	    200	     7.3	 10.5	       0.72
"""
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# 读取素材文件
with open('fruit_data.txt') as file:
    data_list = file.readlines()

# 转换为数组形式，并提取标签和特征
data_array = np.array([line.strip().split('\t') for line in data_list], dtype=float)
labels = data_array[:, 0].astype(int)
features = data_array[:, 1:]

# 使用KNeighborsClassifier进行分类
model = KNeighborsClassifier(n_neighbors=5)
model.fit(features, labels)


def sample(sam):
    predict = model.predict(sam)
    # print(predict)
    # if predict == 1:
    #     return '苹果'
    # if predict == 2:
    #     return '橘子'
    # if predict == 3:
    #     return '橙子'
    # if predict == 4:
    #     return '柠檬'
    lst = ['苹果', '橘子', '橙子', '柠檬']
    return lst[predict[0]-1]


# 预测样本A和B的类别
sample_A = np.array([192, 8.4, 7.3, 0.55]).reshape(1, -1)
sample_B = np.array([200, 7.3, 10.5, 0.72]).reshape(1, -1)
print("样本 A 分类结果:", sample(sample_A))
print("样本 B 分类结果:", sample(sample_B))
