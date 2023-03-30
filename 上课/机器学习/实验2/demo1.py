import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("avgHgt.csv")
df = pd.DataFrame(data)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.title("中国和日本7~18岁男孩升高图")
plt.xlabel("年龄/岁")
plt.ylabel("身高/厘米")
plt.plot(df["age"], df["CHeight"], df["age"], df["JHeight"])
plt.legend(['中国男孩身高', '日本男孩身高'])
plt.show()
