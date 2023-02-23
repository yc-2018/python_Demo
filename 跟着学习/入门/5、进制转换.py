# By：仰晨
# 文件名：5、进制转换
# 时 间：2022/11/9 2:07


a = int(input('输入一个整数'))

print(f'{a}的二进制数为{bin(a)}')
print(f'{a}的八进制数为{oct(a)}')
print(f'{a}的16进制数为{hex(a)}')

# 转回10进制
print(int(hex(a), 16))
print('二进制转换为十进制 ：', int("00011000", 2))
print(int(oct(a), 8))






