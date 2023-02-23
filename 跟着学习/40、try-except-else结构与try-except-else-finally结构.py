# 仰晨
# 始时间：2022/7/28 02:24:42
# 文件名：40、try-except-else结构与try-except-else-finally结构


# try-except-else结构     如果try报错就执行except否则执行else（分支结构）
try:
    a = int(input('请输入被除数'))
    b = int(input('请输入除数'))

    c = a / b

except BaseException as 错:         # 出错又不知道是什么错误就用 BaseException as 名字:
    print('出错了', 错)              # 出错了 division by zero

else:
    print('结果为:', c)


# -----------------------------------------------------
"""
· try...except...else...finally结构
. finally块无论是否发生异常都会被执行，能常用来释放try块中申请的资源
"""


try:
    x = int(input('请输入被乘数'))
    y = int(input('请输入乘数'))

    z = x * y

except BaseException as 错了:         # 出错又不知道是什么错误就用 BaseException as 名字:
    print('出错了', 错了)              # 出错了 invalid literal for int() with base 10: ''

else:
    print('结果为:', z)

finally:
    print('欢迎下次光临')             # 欢迎下次光临  finally块无论是否发生异常都会被执行

print('程序运行结束')



























