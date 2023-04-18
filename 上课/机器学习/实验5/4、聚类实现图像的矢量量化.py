# By：仰晨
# 文件名：4、聚类实现图像的矢量量化
# 时 间：2023/4/18 21:05
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans


im = Image.open('Tiger_Woods_0023.jpg')


im_arr = np.array(im)
X = im_arr.reshape(-1, 3)


# 聚类个数为2
kmeans_2 = KMeans(n_clusters=2, random_state=0).fit(X)
labels_2 = kmeans_2.labels_
centers_2 = kmeans_2.cluster_centers_

# 聚类个数为6
kmeans_6 = KMeans(n_clusters=6, random_state=0).fit(X)
labels_6 = kmeans_6.labels_
centers_6 = kmeans_6.cluster_centers_

# 聚类个数为30
kmeans_30 = KMeans(n_clusters=30, random_state=0).fit(X)
labels_30 = kmeans_30.labels_
centers_30 = kmeans_30.cluster_centers_


# 聚类个数为2
X_compressed_2 = np.array([centers_2[label] for label in labels_2])
im_compressed_2 = Image.fromarray(X_compressed_2.reshape(im_arr.shape).astype('uint8'))

# 聚类个数为6
X_compressed_6 = np.array([centers_6[label] for label in labels_6])
im_compressed_6 = Image.fromarray(X_compressed_6.reshape(im_arr.shape).astype('uint8'))

# 聚类个数为30
X_compressed_30 = np.array([centers_30[label] for label in labels_30])
im_compressed_30 = Image.fromarray(X_compressed_30.reshape(im_arr.shape).astype('uint8'))


# 聚类个数为2
im_compressed_2.show()

# 聚类个数为6
im_compressed_6.show()

# 聚类个数为30
im_compressed_30.show()
