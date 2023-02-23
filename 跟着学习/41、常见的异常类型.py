# 仰晨
# 始时间：2022/7/28 02:43:37
# 文件名：41、常见的异常类型

"""
ZeroDivisionError     除(或取模)零(所有数据类型)
IndexError            序列中没有此索引(index)
KeyError              映射中没有这个键
NameError             未声明/初始化对象(没有属性)
SyntaxError           Python语法错误
ValueError            传入无效的参数
"""

# print(52/0)             # ZeroDivisionError: division by zero

列表 = [0, 1, 2, 4, '牛马']
# print(列表[6])          # IndexError: list index out of range

字典 = {'张三': 76, '李四': 77}
# print(字典['王五'])     # KeyError: '王五'

# print(仰晨)              # NameError: name '仰晨' is not defined

# int a = 20              # SyntaxError: invalid syntax

# print(int('二十'))        # ValueError: invalid literal for int() with base 10: '二十'



























