# 仰晨不牛马
# 牛马时间：2022/6/10 01:49:42

"""求100以内的偶数和"""
和 = 0
增量 = 0
while 增量 <= 100:
    if not bool(增量 % 2):  # 增量%2==0:
        和 = 和 + 增量

    增量 += 1
print('100以内的偶数和为', 和)
