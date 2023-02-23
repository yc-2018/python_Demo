# 仰晨不牛马
# 牛马时间：2022/6/9 02:16:25

# range()的三种方式.列表

# 1、一个值      #list是列表的意思
n牛马 = range(12)  # 会生成比12小的整数（0-11）
print(n牛马)
print(type(n牛马))  # <class 'range'>
print(list(n牛马))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# 2、2个值
n牛马 = range(3, 12)  # 会生成3到比12小的整数（3-11）
print(n牛马)
print(list(n牛马))  # [3, 4, 5, 6, 7, 8, 9, 10, 11]

# 3、3个值
n列表 = range(3, 12, 2)  # 会生成3到比12小间隔2的整数[3, 5, 7, 9, 11]
print(n列表)
print(list(n列表))  # [3, 5, 7, 9, 11]

# 判断一个数是否在列表中，用in  或not in
print(6 in n列表)  # False
print(5 in n列表)  # True
print(6 not in n列表)  # True
print(5 not in n列表)  # False
