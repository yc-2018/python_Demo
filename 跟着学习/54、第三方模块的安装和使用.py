# 仰晨
# 始时间：2022/8/14 17:12:20
# 文件名：54、第三方模块的安装和使用
# 在线安装第三方模块--先打开管理员（cmd）
# C:\Users\Dell>pip install schedule          # 安装第三方模块schedule--------------pip install 模块名-------------------------
# 一堆东西
# C:\Users\Dell>python                        # 进入python-------------------------------------------------
# 一个提示
# import schedule                         # 使用第三方模块，如果不报错就是导入成功了---------------------------

import schedule
import time


def job():
    print('嗨--')


schedule.every(3).seconds.do(job)  # 安排。每3。秒。做（工作）
while True:
    schedule.run_pending()  # 运行
    time.sleep(1)  # 延迟一秒
