# By：仰晨
# 文件名：鸢尾花数据集
# 时 间：2023/4/17 20:40

"""
使用SKlearn的KNeighborsClassifier功能，对鸢尾花数据集进行KNN分类，将分类结果以分类图的形式显示。学习meshgrid()、pcolormesh()函数的使用。
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

# 载入iris数据集
iris = load_iris()
X = iris.data[:, :2]  # 取前两个特征值
y = iris.target

# 生成网格坐标
h = .02  # 步长
x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# 使用KNN分类
k = 15
model = KNeighborsClassifier(k)
model.fit(X, y)

# 绘制分类图
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.figure(1, figsize=(8, 6))
plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Paired)

# 绘制散点图
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', cmap=plt.cm.Paired)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')

# 设置边界
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title("Classification results with k = %d" % k)
plt.show()
