# 仰晨不牛马
# 牛马时间：2022/6/10 02:06:14

print('可迭代对象有，字符串和裂表')

for 自定义变量 in '可迭代对象':  # 第一次把可赋值给自定义变量，以此类推
    print(自定义变量)

# range() 产生的序列 也是可迭代对象

for i in range(11):
    print(i, end='-')

print('\n')
# 如果不用自定义变量 可以写为 _
for _ in range(3):
    print('重要的事情说3遍')

#############################################
# ##求1到100之间的偶数和
和 = 0
for z in range(1, 100):
    if z % 2 == 0:
        和 += z
print('1到100之间的偶数和为', 和)

print('''求100到999的水仙花数
比如:153=1*1*1+5*5*5+3*3*3''')

for hh in range(100, 1000):
    个位 = hh % 10
    十位 = hh // 10 % 10
    百位 = hh // 100
    if hh == 个位 ** 3 + 十位 ** 3 + 百位 ** 3:
        print(hh)
