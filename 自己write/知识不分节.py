#下面是申明 #coding:gbk
#coding:utf-8
#在 Python 3 中，可以用中文作为变量名，非 ASCII 标识符也是允许的了。
print('打印')

牛马='字符串，又长又臭'
大牛马="一条句子，超级长和臭"
超级牛马="""三个双引号的，还可以换行的巨长臭的东西"""

print('hello\n牛马')      # 使用反斜杠(\)+n转义特殊字符
print(R'hello\n牛马')     # 在字符串前面添加一个 r或R，表示原始字符串，不会发生转义

#########################################
'''保留字即关键字
'False', 'None', 'True', 'and', 'as', 
'assert', 'break', 'class', 'continue', 
'def', 'del', 'elif', 'else', 'except', 
'finally', 'for', 'from', 'global', 'if', 
'import', 'in', 'is', 'lambda', 'nonlocal', 
'not', 'or', 'pass', 'raise', 'return', 'try', 
'while', 'with', 'yield']
'''
########################################

#########################################
"""
多行语句
Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠 \ 来实现多行语句，例如：
"""
无敌牛马 = 牛马 + \
        大牛马 + \
        超级牛马
print('\n',无敌牛马)
'''
在 [], {}, 或 () 中的多行语句，不需要使用反斜杠 \，例如：
total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
'''
#字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
str = '123456789'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始后的所有字符
print(str[1:5:2])  # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str * 2)  # 输出字符串两次
print(str + '你好'+牛马)  # 连接字符串



'''Python 可以在同一行中使用多条语句，语句之间使用分号 ; 分割，以下是一个简单的实例：
import sys; x = 'runoob'; sys.stdout.write(x + '\n')


print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：
'''
print(牛马+'不换行',end="00000000");print(大牛马)


import sys
print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)

from sys import argv, path  # 导入特定的成员

print('================python from import===================================')
print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path


'''
多个变量赋值
Python允许你同时为多个变量赋值。例如：

a = b = c = 1
以上实例，创建一个整型对象，值为 1，从后向前赋值，三个变量被赋予相同的数值。

您也可以为多个对象指定多个变量。例如：

a, b, c = 1, 2, "runoob"
以上实例，两个整型对象 1 和 2 的分配给变量 a 和 b，字符串对象 "runoob" 分配给变量 c。'''