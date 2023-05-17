# By：仰晨
# 文件名：回归算法
# 时 间：2023/5/18 2:11
import numpy as np

# 数据预处理
data = np.array([[20, 7000, 800, 1],
                 [35, 2000, 2500, 0],
                 [27, 5000, 3000, 1],
                 [32, 4000, 4000, 0],
                 [45, 2000, 3800, 0]])

X = data[:, :3]
y = data[:, 3]

X = (X - X.mean(axis=0)) / X.std(axis=0)  # 特征缩放


# 梯度下降法求解逻辑回归参数
def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def gradient_descent(X, y, alpha, iterations):
    m, n = X.shape
    X = np.hstack((np.ones((m, 1)), X))  # 添加一列全1向量表示偏置项
    theta = np.zeros(n + 1)  # 初始化参数为0

    for _ in range(iterations):
        z = np.dot(X, theta)
        h = sigmoid(z)
        gradient = np.dot(X.T, (h - y)) / m
        theta -= alpha * gradient

    return theta


alpha = 0.01
iterations = 10000
theta = gradient_descent(X, y, alpha, iterations)

# 预测用户6的贷款是否会逾期
user_6 = np.array([30, 3500, 3500])
user_6 = (user_6 - X.mean(axis=0)) / X.std(axis=0)  # 特征缩放
user_6 = np.hstack((np.ones(1), user_6))

probability = sigmoid(np.dot(user_6, theta))
prediction = probability >= 0.5  # True表示逾期，False表示不逾期

print(f"用户6的贷款逾期概率: {probability}")
print(f"预测用户6的贷款是否逾期: {'Yes' if prediction else 'No'}")
