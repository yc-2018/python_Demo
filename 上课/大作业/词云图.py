# By：仰晨
# 文件名：词云图
# 时 间：2022/11/22 2:58

from wordcloud import WordCloud as 词云图
# 添加形状 要这2包
import numpy as np
from PIL import Image
# 读取数据用
import pandas as pd


形状 = np.array(Image.open("pic/bili.png"))

path = r"C:\Windows\Fonts\simhei.ttf"

词云 = 词云图(background_color="white", max_words=100, font_path=path, colormap="Blues", mask=形状, contour_width=8,
         contour_color="#6DD5ED", max_font_size=50, stopwords="区")  # 不加禁用词会有bug
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

data = pd.read_excel("热榜合并.xlsx", sheet_name=0)  # 读取数据
text = data.loc[:, '分区'].tolist()
text = "+区+".join(text)
词云.generate(text)
词云.to_file("pic/B站热榜词云图.png")
print(text)
