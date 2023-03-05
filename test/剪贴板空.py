# By：仰晨
# 文件名：剪贴板空
# 时 间：2023/3/5 22:31
import pyperclip

paste = pyperclip.paste()
print(paste)

if paste is None:
    print(666)

if paste == "":
    print(777)      # 剪贴板为图片等   就是“”
