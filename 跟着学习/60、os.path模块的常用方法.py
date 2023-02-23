# 仰晨
# 始时间：2022/8/16 01:45:27
# 文件名：60、os.path模块的常用方法

# 函数-----------------------------说明--------------------------------------------
# abspath(path)           用于获取文件或目录的绝对路径
# exists(path)            用于判断文件或目录是否存在，如果存在返回True.否则返回False
# join(path, name)        将目录与目录或者文件名拼接起来
# splitext()              分离文件名和扩展名
# basename(path)          从一个目录中提取文件名
# dirname(path)           从一个路径中提取文件路径，不包括文件名
# isdir(path)             用于判断是否为路径
# --------------------------------------------------------------------------------
import os.path
print(os.path.abspath('58、文本.txt'))                                     # 获取文件或目录的绝对路径
print(os.path.exists('58、文本.txt'), os.path.exists('60、文本.txt'))       # 判断文件或目录是否存在，如果存在返回True.否则返回False
print(os.path.join(r'E:\Pycharm\跟着学习', '牛马.abc'))       # 拼接         # E:\Pycharm\跟着学习\牛马.abc
print(os.path.split(r'E:\Pycharm\跟着学习\58、文本.txt'))     # 路径和文件分开  # ('E:\\Pycharm\\跟着学习', '58、文本.txt')
print(os.path.splitext('拆分.txt'))                                        # ('拆分', '.txt')
print(os.path.basename(r'E:\Pycharm\跟着学习\58、文本.txt'))  # 提取文件名     # 58、文本.txt
print(os.path.dirname(r'E:\Pycharm\跟着学习\58、文本.txt'))   # 提取目录       # E:\Pycharm\跟着学习
print(os.path.isdir(r'E:\Pycharm\跟着学习\58、文本.txt'))    # 判断是否为路径,文件不是路径，会在系统找 找不到也是False         # False

print('--------------------------------------------------------------------------------------------------------------------')
# 案例：输出指定目录下的所有.py文件

import os
当前目录 = os.getcwd()
列表 = os.listdir(当前目录)
for 文件名 in 列表:
    if 文件名.endswith('.py'):                 # .endwith('是以什么结尾的意思')
        print(文件名)

# 案例：os里面有一个函数walk（‘路径’）  可以遍历路径的所有文件和目录和子目录    这个函数返回的值是一个元组?
遍历目录 = os.walk(r'E:\Pycharm')
print(type(遍历目录))
for 路径, 目录名, 文件名 in 遍历目录:
    '''print('########################################')
    print(路径)
    print(目录名)
    print(文件名)'''
    print('@@@@@@@@@@@@@@@@@@@@@@')
    for dir in 目录名:
        print(os.path.join(路径, dir))
    print('$$$$$$$$$$$$$$$$$$$$$')
    for file in 文件名:
        print(os.path.join(路径, file))

























