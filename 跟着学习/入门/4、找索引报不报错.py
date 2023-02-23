# By：仰晨
# 文件名：4、找字符串索引报不报错
# 时 间：2022/11/9 1:52

lst = '唱跳rep篮球'

try:
    print(lst.index('跳'))
    print(lst.index('飞'))
except ValueError as c:
    print('找不到就会报错', c)

print(lst.find('唱'))
print('不存在就返回', lst.find('喊'))





