# By：仰晨
# 文件名：打开和关闭软件
# 时 间：2023/6/19 14:58
import subprocess
import os
import locale

# # 获取系统默认编码
# encoding = locale.getpreferredencoding()
#
# # 要退出的程序路径
# exe_path = r"D:\green\v2rayN-Core\v2rayN.exe"
#
# # 使用tasklist命令查找正在运行的程序
# tasklist_output = subprocess.check_output("tasklist", shell=True).decode(encoding)
#
# # 检查程序是否正在运行
# if os.path.basename(exe_path) in tasklist_output:
#     # 使用taskkill命令结束程序
#     subprocess.call(f"taskkill /IM {os.path.basename(exe_path)} /F", shell=True)
#     print(f"{exe_path}已退出")
# else:
#     print(f"{exe_path}未运行")




# 要退出的程序路径
exe_path = r"D:\green\v2rayN-Core\v2rayN.exe"

# 使用taskkill命令强制结束程序
os.system(f"taskkill /IM {os.path.basename(exe_path)} /F")


# 使用subprocess.Popen()启动程序，不等待其结束
subprocess.Popen(exe_path)
