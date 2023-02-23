# 仰晨
# 始时间：2022/8/14 03:01:20
# 文件名：53、常用的内置模块

"""
sys         与Python解释器及其环境操作相关的标准库
time        提供与时间相关的各种函数的标准库
os          提供了访问操作系统服务功能的标准库
calendar    提供与日期相关的各种函数的标准库
urllib      用于读取来自网上（服务器）的数据标准库
json        用于使用JSON序列化和反序列化对象
re          用于在字符串中执行正则表达式匹配和替换
math        提供标准算术运算函数的标准库
decimal     用于进行精确控制运算精度、有效数位和四舍五入操作的十进制运算
logging     提供了灵活的记录事件、错误、警告和调试信息等目志信息的功能
"""

import sys
import time
import urllib.request
import math

print(sys.getsizeof('获取对象所占的内存大小'))             # 96
print(sys.getsizeof(127))                               # 28
print(sys.getsizeof(1))                                  # 28
print(sys.getsizeof(0))                                   # 24
print(sys.getsizeof(False))                                # 24
print(sys.getsizeof(True))                                  # 28

print(time.time())                      # 未转化的时间          # 1660418012.5328677
print(time.localtime(time.time()))      # 转化时间               # time.struct_time(tm_year=2022, tm_mon=8, tm_mday=14, tm_hour=3, tm_min=16, tm_sec=4, tm_wday=6, tm_yday=226, tm_isdst=0)

print(urllib.request.urlopen('http://www.baidu.com').read())     # 读取百度网页

print(math.e)                                                       # 2.718281828459045





























