# By：仰晨
# 文件名：推荐算法
# 时 间：2023/5/9 0:40
"""
1.实验目的
（1）了解推荐算法的基本概念；
（2）掌握推荐算法的类别；
（3）掌握基于协同过滤的推荐算法；
（4）了解其他常见的推荐算法。

2.实验内容
1、使用KNN进行图书推荐。下表是一个图书网站的数据，有6位用户对4本图书进行了评分。详细评分的值越大表示喜好越强烈。使用KNN模型找出与用户F最相似的用户。
用户编号	图书1	图书2	图书3	图书4
  A	     1.1	1.5 	1.4 	0.2
  B	     1.9	1.0 	1.4 	0.2
  C	     1.7	1.2 	1.3 	0.2
  D	     2.6	2.1 	1.5 	0.2
  E	     2.0	2.6 	1.4 	0.2
  F	     1.6	1.5 	1.2 	0.1
2、基于用户的产品推荐。根据用户的特征找到相似的用户，并且把相似用户的喜爱产品推荐给当前用户。例如。客户A和B相似，则将客户A所购买过的产品推荐给客户B，反之亦然。
"""

import pandas as pd
from sklearn.neighbors import NearestNeighbors

# ------------创建一个DataFrame来表示用户评分数据，并计算KNN---------
# 用户评分数据
data = {
    '用户编号': ['A', 'B', 'C', 'D', 'E', 'F'],
    '图书1': [1.1, 1.9, 1.7, 2.6, 2.0, 1.6],
    '图书2': [1.5, 1.0, 1.2, 2.1, 2.6, 1.5],
    '图书3': [1.4, 1.4, 1.3, 1.5, 1.4, 1.2],
    '图书4': [0.2, 0.2, 0.2, 0.2, 0.2, 0.1]
}

df = pd.DataFrame(data)
ratings_matrix = df.drop('用户编号', axis=1).values

# 计算 KNN
knn = NearestNeighbors(n_neighbors=2, metric='euclidean')
knn.fit(ratings_matrix)

# 找出与用户F最相似的用户
user_f_index = df[df['用户编号'] == 'F'].index[0]
distances, indices = knn.kneighbors(ratings_matrix[user_f_index].reshape(1, -1))

# 输出结果
print("与用户F最相似的用户：", df.loc[indices.flatten()[1], '用户编号'])

# ----------基于用户的产品推荐--------------
# 假设用户购买的图书数据
user_purchases = {
    'A': ['book1', 'book2'],
    'B': ['book3', 'book4'],
    'C': ['book5', 'book6'],
    'D': ['book7', 'book8'],
    'E': ['book9', 'book10'],
    'F': ['book11', 'book12']
}

# 找到与用户F最相似的用户
similar_user = df.loc[indices.flatten()[1], '用户编号']

# 获取相似用户购买过的产品，并将其推荐给用户F
recommended_books = user_purchases[similar_user]
print("推荐给用户F的图书：", recommended_books)
