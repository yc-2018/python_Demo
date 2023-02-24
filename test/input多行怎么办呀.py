# By：仰晨
# 文件名：input多行怎么办呀
# 时 间：2023/2/24 16:11
# data = """
# line1
# line2
# line3
# """
#
# input_data = input(data)
#
# print(input_data)

"""pyperclip是一个第三方库，可以让你在Python程序中复制和粘贴文本。"""
import pyperclip

# 读取剪贴板内容
text = pyperclip.paste()

print(text)
