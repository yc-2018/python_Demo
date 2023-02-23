# 欲仰清晨却已星辰（懒）
# 始时间：2022/7/23 19:09:01
# 文件名：39、报错之用try-except

"""
程序报错之try
比如下面这个程序，我就不输入数，或者输入除数为0就会报错那怎么办
除数为0  报错  ZeroDivisionError: division by zero
不输入数 报错  ValueError: invalid literal for int() with base 10: 'a'

"""

try:
    a = int(input('请输入被除数'))
    b = int(input('请输入除数'))

    c = a/b

    print('结果为:', c)
except ZeroDivisionError:               # 当try中代码报错且报错类型为ZeroDivisionError:时，执行该函数中的代码
    print('！！！除数不能为0！！！')
except ValueError:
    print('！！！请输入数字!!!')           # 当try中代码报错且报错类型为ValueError:时，执行该函数中的代码
































