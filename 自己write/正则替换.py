# By：仰晨
# 文件名：s
# 时 间：2022/12/13 3:37
import re

"""re模块（正则表达式模块）的sub函数来进行字符串替换。
第一个参数是一个正则表达式，第二个参数是要替换成的字符串，第三个参数是原始字符串。"""
print(re.sub('[自治区市省回族维吾尔壮族]', '', '广东省'))
