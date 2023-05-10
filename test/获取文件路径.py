# By：仰晨
# 文件名：获取文件路径
# 时 间：2023/5/10 19:11
import os

folder_path = r'E:\Users\Dell\Desktop\新建文件夹'
jpg_files = [(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.jpg')]
print(jpg_files)    # os.path.join(folder_path, f)

print(os.path.dirname("他的父级路径"+r'E:\Users\Dell\Desktop\新建文件夹\IMG_20230413_152221.jpg'))
print(os.path.join('folder_path', 'f','666.py'))
