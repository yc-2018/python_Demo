# 仰晨不牛马
# 牛马时间：2022/6/8 21:38:31

z数1 = int(input('请输入第一个整数'))
z数2 = int(input('请输入第二个整数'))

# 正常写法
if z数1 > z数2:
    print(z数1, '大于', z数2)
elif z数1 < z数2:
    print(z数1, '小于', z数2)
else:
    print(z数1, '等于', z数2)

# 条件表达式（好像只能2个值）
print(str(z数1) + '大于' + str(z数2) if z数1 > z数2 else str(z数1) + '小于等于' + str(z数2))
# 或者用括号
print((z数1, '大于', z数2) if z数1 > z数2 else (z数1, '小于等于', z数2))
