# By：仰晨
# 文件名：列表循环判断语法糖
# 时 间：2023/4/8 1:12

png_ = ['1000.0、ASCII转字符.py', '1000.1、文字转字符码.py', '1001.0、个性字母and数字.png']
print([p + ".png" for p in png_ if p.endswith(".png")])  # ['1001.0、个性字母and数字.png.png']

# 结论：先判断再放进列表前再多加一个.png

# s = input(1)
# if s ==None:
#     print(666)
# if s =="":
#     print(777)
# # 直接回车为777

import os
print(type(os.path.getsize('图片转Base64.py')))

# print(1024**2*20)
# print((1024**2)*20)


# import os
# def file_extension(path):
#     return os.path.splitext(path)[1]
# # 调用函数并传入文件路径，返回文件的扩展名
# print(file_extension('C:/Users/Administrator/Desktop/sam.ple.jpg'))


print("".join("sd.dsd.sddf.qqq".split(".")[:-1]))
print(os.path.splitext("sd.dsd.sddf.qqq")[0])