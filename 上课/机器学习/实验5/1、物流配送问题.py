# By：仰晨
# 文件名：1、物流配送问题
# 时 间：2023/4/18 13:34

"""
1.实验目的
（1）理解K-Means聚类算法的概念；
（2）掌握K-Means算法的步骤；
（3）掌握使用K-Means算法解决实际聚类问题；
（4）理解K-Means算法的特点。
2.实验内容
1、物流配送问题。“双十一”期间，物流公司要给M城市的50个客户配送货物。假设公司只有5辆货车，客户的地理坐标在testSet.txt文件中，如何配送效率最高？
   用聚类算法完成，并且设置不同的初始聚类中心，观察聚类的结果。
"""

# coding=utf-8
# from numpy import *
# from matplotlib import pyplot as plt
# import matplotlib
#
# matplotlib.use('TkAgg')
#
#
# def disteclud(veca, vecb):
#     return sqrt(sum(power(veca - vecb, 2)))
#
#
# def initcenter(dataset, k):
#     print('2.initalize cluster center')
#     shape = dataset.shape
#     n = shape[1]
#     classcenter = array(zeros((k, n)))
#     for j in range(n):
#         firstk = dataset[:k, j]
#         classcenter[:, j] = firstk
#     return classcenter
#
#
# def mykmeans(dataset, k):
#     m = len(dataset)
#     clusterpoints = array(zeros((m, 2)))
#     classCenter = initcenter(dataset, k)
#     clusterchanged = True
#     print('3.recompute and reallocated')
#     while clusterchanged:
#         clusterchanged = False
#         for i in range(m):
#             mindist = inf
#             minindex = -1
#             for j in range(k):
#                 distji = disteclud(classCenter[j, :], dataset[i, :])
#                 if distji < mindist:
#                     mindist = distji;
#                     minindex = j
#             if clusterpoints[i, 0] != minindex:
#                 clusterchanged = True
#             clusterpoints[i, :] = minindex, mindist ** 2
#         for cent in range(k):
#             ptsinclust = dataset[nonzero(clusterpoints[:, 0] == cent)[0]]
#             classCenter[cent, :] = mean(ptsinclust, axis=0)
#     return classCenter, clusterpoints
#
#
# def show(dataset, k, classCenter, clusterPoints):
#     print('4.load the map')
#     fig = plt.figure()
#     rect = [0.1, 0.1, 1.0, 1.0]
#     axprops = dict(xticks=[], yticks=[])
#     ax0 = fig.add_axes(rect, label='ax1', frameon=False)
#     imgp = plt.imread(r'city.png')
#     ax0.imshow(imgp)
#     ax1 = fig.add_axes(rect, label='ax1', frameon=False)
#     print('5.show the clusters')
#     numsamples = len(dataset)
#     mark = ['ok', '^b', 'om', 'og', 'sc']
#     for i in range(numsamples):
#         markindex = int(clusterPoints[i, 0]) % k
#         ax1.plot(dataset[i, 0], dataset[i, 1], mark[markindex])
#     for i in range(k):
#         markindex = int(clusterPoints[i, 0]) % k
#         ax1.plot(classCenter[i, 0], classCenter[i, 1], '^r', markersize=12)
#     plt.show()
#
#
# print('1. load the dataset')
# dataset = loadtxt(r'testSet.txt')
# k = 5
# classCenter, clssspoints = mykmeans(dataset, k)
# show(dataset, k, classCenter, clssspoints)

import numpy as np

with open('testSet.txt') as file:
    data = []
    for line in file.readlines():
        line = line.strip().split()
        data.append([float(line[0]), float(line[1])])
data = np.array(data)

from sklearn.cluster import KMeans

k = 5  # 设定聚类数目
kmeans_model = KMeans(n_clusters=k, init='k-means++', random_state=0).fit(data)

import matplotlib.pyplot as plt
from PIL import Image

# img = Image.open('city.png')  # 打开地图图片
# plt.imshow(img)  # 显示地图图片

colors = ['r', 'g', 'b', 'c', 'm', 'y']  # 设置不同类别的颜色
centers = kmeans_model.cluster_centers_  # 获得聚类中心
for i in range(k):
    members = kmeans_model.labels_ == i  # 获得属于当前类别的客户
    plt.scatter(data[members, 0], data[members, 1], s=60, c=colors[i], alpha=0.5)  # 绘制散点图
    plt.scatter(centers[i][0], centers[i][1], s=100, c='k', marker='*', linewidths=2)  # 绘制聚类中心

plt.show()  # 显示图片
