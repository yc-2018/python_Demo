# By：仰晨
# 文件名：读取环境变量
# 时 间：2023/12/29 23:27


import os

# 读取环境变量
appid = os.getenv('BDid')

# 使用 appid
# ... 您的代码逻辑 ...

print(f"使用的APPID: {appid}")
