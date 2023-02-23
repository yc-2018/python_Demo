# By：仰晨
# 文件名：词云图
# 时 间：2022/11/22 2:58

from wordcloud import WordCloud as 词云图
# 添加形状 要这2包
import numpy as np
from PIL import Image
# 处理一坨的字符串要用   j=jieba.lcut("字符串")#返回数组列表  s=" ".join(j)就会变成每一个词 之间有一个空格
import jieba

形状 = np.array(Image.open("pic/bili.png"))

path = "C:\Windows\Fonts\simhei.ttf"
stop = ['的', '和', '了', '我', "在"]
词云 = 词云图(background_color="white", repeat=False, max_words=84, width=500, height=500,
         max_font_size=200, font_path=path, colormap="Blues", mask=形状, contour_width=10, contour_color="#6DD5ED",
         stopwords=stop)
"""
background_color    背景颜色
repeat              词 重复用
max_words           整个图片最多有个词
width               图片宽
height              图片高
max_font_size       字体最大多少像素
font_path           字体路径，没有的话就只能是英文的
colormap            字体整体色调，颜色值要百度（Reds红）
stopwords           过滤没用词=列表
mode                颜色通道默认RGB  改成RGBA背景就可以透明  但背景值要先改成None  轮廓用了会报错
--------------------
mask                导入图片形状（比较麻烦）
contour_width       图片形状--外轮廓
contour_color       图片形状--外轮廓颜色
"""
text = "黑子得到了乐趣，哥哥得到了热度，只有真爱粉破防了\
        我先声明我是ikun，这辈子只粉坤坤一人！为了坤坤我还专门建了个鸡舍养鸡，就在前几天发生了一件让我决定一辈子粉坤坤的事情。\
        前天晚上一点我家鸡舍突然传出一阵鸡叫，我以为有人偷鸡，赶忙拿着铁锹就去鸡舍。我寻着鸡叫声慢慢地摸了进去，走进以后我立马打开手电筒，\
        举起铁锹大声喊道:“谁在偷鸡！”，定睛一看我哭了啊！原来是我家坤坤蹲在鸡舍里给我下蛋，试问还有哪个偶像能做到！你们这群黑子，就是嫉妒，就是见不得我家坤坤会下蛋！"
j = jieba.lcut(text)
text = " ".join(j)
print(text)

词云.generate(text)
词云.recolor()  # 换色调，其实没啥必要重新生成也一样
词云.to_file("pic/p.png")

import pandas as pd

data = pd.read_excel("热榜合并.xlsx", sheet_name=0)  # 读取数据
text = data.loc[:, '分区'].tolist()
text = " ".join(text)
词云.generate(text)
词云.to_file("pic/B站热榜词云图.png")
