# By：仰晨
# 文件名：win哔哔声试试
# 时 间：2023/2/28 2:10
import winsound
import os
os.chdir(r'E:\Pycharm\python_Demo\自己write\sound')  # 设置当前路径
winsound.PlaySound("play.mp3", winsound.SND_NODEFAULT)

# 失败---------------不行

# 第二个参数是winsound.SND_FILENAME，它指示PlaySound函数使用文件名作为音频文件的来源。
