# 仰晨
# 始时间：2022/7/28 02:56:57
# 文件名：42、traceback模块的使用


import traceback

try:
    print('----------------')
    print(1 / 0)
except:
    traceback.print_exc()


# 有时报错在前，有时报错在后，这是因为这是线程进行?（同时进行？）
# 了解这个模块是为了以后看（出错）日志

"""
ZeroDivisionError: division by zero
----------------
"""

"""
----------------
ZeroDivisionError: division by zero
"""