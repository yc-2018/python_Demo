# 仰晨不牛马
# 牛马时间：2022/5/26 23:05:29
print('--------------str()将其他类型转换成str类型--------------------')
名字 = '仰晨'
年龄 = 22

print('我叫' + 名字 + '，今年' + str(年龄) + '岁')  # 不同类型连接（+是连接符）不可以直接打印   这里要加str()转换

a = 1
b = 2.0
c = False
print(type(a), type(b), type(c))  # 看原本数据类型
print(str(a), str(b), str(c))
print(type(str(a)), type(str(b)), type(str(c)))

# 这样没用，瞬时性的
str(a), str(b), str(c)
print(type(a), type(b), type(c))

print('---------------int()，其他转换成int类型------------------')
str1 = '556'
str2 = '55.6'
str3 = 'lm'
print(type(int(str1)), int(str1))
# print(type(int(str2)),int(str2))   #字符串只有整数字符串才可以转
# print(type(int(str3)),int(str3))    #字符串只有整数字符串才可以正常转

# 布尔型可以正常转
bool1 = True
bool2 = False
print(type(int(bool1)), int(bool1))
print(type(int(bool2)), int(bool2))

# float类型转int会直接舍弃小数
float1 = 13.14
print(type(int(float1)), int(float1))

print('---------------float()，其他转换成float类型------------------')
str1 = '6767'
str2 = '67.67'
str3 = 'a.67'

int1 = 67

bool1 = True

print(type(float(str1)), float(str1))
print(type(float(str2)), float(str2))
# print(type(float(str3)),float(str3))#只有小数点和数字组成的才可以正常转换

print(type(float(bool1)), float(bool1))
print(type(float(bool2)), float(bool2))

print(type(float(int1)), float(int1))
