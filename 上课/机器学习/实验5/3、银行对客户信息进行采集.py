# By：仰晨
# 文件名：3、银行对客户信息进行采集
# 时 间：2023/4/18 20:49

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

matplotlib.use('TkAgg')
dataset = pd.read_csv(r'Customer_Info.csv')
print(dataset)
X = dataset.iloc[:, [4, 3]].values
from sklearn.cluster import KMeans

sumDs = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(X)
    sumDs.append(kmeans.inertia_)
    print(kmeans.inertia_)
plt.plot(range(1, 11), sumDs)
plt.title('the Elbow method')
plt.xlabel('number of cluster k')
plt.ylabel('SSE')
plt.show()
kmenas1 = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=0)
y_kmeans = kmenas1.fit_predict(X)
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s=100, marker='^', c='red', label='poor')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s=100, marker='o', c='green', label='middle')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s=100, marker='*', c='blue', label='rich')
plt.scatter(kmenas1.cluster_centers_[:, 0], kmenas1.cluster_centers_[:, 1], s=250, c='yellow', label='Centroids')
plt.title('clusters of customer info')
plt.xlabel('deposit')
plt.ylabel('age')
plt.legend()
plt.show()
