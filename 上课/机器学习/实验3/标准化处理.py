# By：仰晨
# 文件名：标准化处理
# 时 间：2023/4/17 20:02
from sklearn import preprocessing
import numpy as np

from sklearn.metrics import precision_score, recall_score, f1_score

"""
1.假设某地某天的时段温度分别为[20,23,24,25,26,27,28,25,24,22,21,20]，编程使用preprocessing.scale()函数对此数列进行标准化处理。
2、使用某模型对水果进行预测，真值为[1,0,0,1,1,0,0,1]，预测结果为[0,1,1,1,1,1,0,1]，编程计算该模型的精确率、召回率和f1均值。
"""

# 标准化处理
temp = [20, 23, 24, 25, 26, 27, 28, 25, 24, 22, 21, 20]
temp = np.array(temp).reshape(-1, 1)  # 转换为列向量
scaled_temp = preprocessing.scale(temp, axis=0)
print(scaled_temp)


print("---------------------------------------------")

# 精确率、召回率和 F1 均值计算

true_y = [1, 0, 0, 1, 1, 0, 0, 1]
pred_y = [0, 1, 1, 1, 1, 1, 0, 1]

precision = precision_score(true_y, pred_y)
recall = recall_score(true_y, pred_y)
f1 = f1_score(true_y, pred_y)

print("精确率：", precision)
print("召回率：", recall)
print("F1 值：", f1)
