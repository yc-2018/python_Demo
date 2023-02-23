# 仰晨不牛马
# 牛马时间：2022/5/24 17:16:18

整数1 = 67
整数2 = -67
整数3 = 0
整数4 = 0b1011011  # 二进制
整数5 = 0o67  # 八进制
整数6 = 0x2b  # 十六进制

print(整数1, type(整数1), '\n', 整数2, type(整数2), '\n', 整数3, type(整数3), '\n', 整数4, type(整数4), '\n', 整数5, type(整数5), '\n', 整数6,
      type(整数6))

f浮点数1 = 1.1
f浮点数2 = 2.2
f浮点数3 = 3.3
print(f浮点数1 + f浮点数2)  # 结果=3.3000000000000003
print(f浮点数3 + f浮点数2)  # 结果=5.5
print(f浮点数3, type(f浮点数3))
from decimal import Decimal  # 调用模块让小数点后精确

print(Decimal('1.1') + Decimal('2.2'))

# 首字母必须大写
d布尔0 = False  # False表示0
d布尔1 = True  # True表示1
print(d布尔0, type(d布尔0))
print(d布尔1, type(d布尔1))
d布尔0 = d布尔0 + 1  # 运算后会变成int型=0+1=1
print(d布尔0, type(d布尔0))

str1 = '牛马又来啦1'
str2 = "牛马有来啦2"
str3 = '''牛马就没
有
跑'''
str4 = """因为牛马
跑不动"""
print(str1, type(str1))
print(str2, type(str2))
print(str3, type(str3))
print(str4, type(str4))
