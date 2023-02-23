# 仰晨
# 始时间：2022/8/15 18:41:33
# 文件名：59、os模块的常用函数

"""
目录操作
    1、os模块是Python内置的与操作系统功能和文件系统相关的模块,该模块中的语句的执行结果通常与操作系统有关,
       在不同的操作系统上运行，得到的结果可能不一样。
    2、os模块与os.path模块用于对目录或文件进行操作
"""

import os
# os.system('notepad.exe')                    # 打开电脑记事本
# os.system('calc.exe')                       # 打开计算机

# 直接调用可执行文件
# os.startfile(r'F:\R软件\WeChat\WeChat.exe')    # 打开微信     # 如果前面不写r,后面的\都要写写成\\（转义字符）

# os.startfile('E:\\Users\\Dell\\Desktop\\最伟大的作品.mp3')      # 听歌....


#  ------------------os模块操作目录相关函数------------------------------ #
#       函数                                      说明                  #
#   getcwd()                                返回当前的工作目录            #
#   listdir(path)                           返回指定路径下的文件和目录信息  #
#   mkdir(path[, mode])                     创建目录                    #
#   makedirs(path1/path2.. . [, mode])      创建多级目录                 #
#   rmdir(path)                             删除目录                    #
#   removedirs(path1/path2.. . . . .)       删除多级目录                 #
#   chdir(path)                             将path设置为当前工作目录       #
# ------------------------------------------------------------------  #

print(os.getcwd())                          # 返回当前的工作目录

lst = os.listdir('../跟着学习')             # 返回指定路径下的文件和目录信息     写全也是可以的

print(lst)

# os.mkdir('59、创建的文件夹')                   # 创建目录
# os.mkdir(r'E:\Users\Dell\Desktop\试试水')    # 创建目录

# os.makedirs('59、创建的多级文件夹/空白/是空白/都是空白')              # 创建多级目录
# os.makedirs(r'E:\Users\Dell\Desktop\试试水\1223\sdl')          # 创建多级目录

# os.rmdir('59、创建的文件夹')                                 # 只能删除空白文件夹
# os.removedirs('59、创建的多级文件夹/空白/还是空白/都是空白')       # 删除多级目录
# os.removedirs(r'E:\Users\Dell\Desktop\试试水\1223\sdl')        # # 删除多级目录

os.chdir(r'E:\Pycharm\跟着学习')                            # 将这个目录设置为当前工作目录
















