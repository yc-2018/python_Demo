# By：仰晨
# 文件名：获取文件路径
# 时 间：2023/5/10 19:11
import os

folder_path = r'E:\Users\Dell\Desktop'
jpg_files = [(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.jpg')]
print(jpg_files)    # os.path.join(folder_path, f)

print(os.path.dirname("他的父级路径"+r'E:\Users\Dell\Desktop\yc.png'))
print(os.path.join('folder_path', 'f','666.py'))


print(os.path.dirname(r'E:\Users\Dell\Desktop\yc.png'))
print(os.path.basename(r'E:\Users\Dell\Desktop\yc.png'))

print(os.path.isfile(r'E:\Users\Dell\Desktop\7218653142534062653.jpg'))
