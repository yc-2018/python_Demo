# By：仰晨
# 文件名：漏斗图
# 时 间：2022/12/28 20:40
import pandas as pd
from pyecharts.charts import Funnel


data = pd.read_excel("热榜合并.xlsx", sheet_name=0)  # 读取数据
counts = data['UP主'].value_counts().to_list()                       # 拿到up出现的次数
name = []
values = []
for i in range(1, counts[0]+1):                                      # 统计的第一个肯定是出现次数最多的 为3就循环3次
    count = counts.count(i)                                          # 对列表相同值进行统计
    print(i, "出现了", count, "次")
    name.append(str(i)+'个上榜视频')
    values.append(count)

wf = Funnel()                       # 创建漏斗图对象
wf.add('up主视频数量情况', [list(z) for z in zip(name, values)], is_selected=True)
wf.render(path="pic/漏斗图.HTML")  # 生成html
