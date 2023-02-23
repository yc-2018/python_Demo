# 欲仰清晨却已星辰（懒）
# 始时间：2022/7/20 01:46:33
# 文件名：36、函数def

"""
函数的创建和调用
·什么是函数
·函数就是执行特定任和以完成特定功能的一段代码·为什么需要函数
·复用代码·隐藏实现细节·提高可维护性
·提高可读性便于调试·函数的创建
                            def 函数名（[输入参数]) :
                                函数体
                                [return xxx]
"""

def 求和函数 (牛, 马):            # 牛和马是形参，形参的位置是在函数的定义处
    和 = 牛 + 马
    return 和



得到数 = 求和函数(665,245)         # 556和245是实参，实参的位置是函数的调用处。。。。。这样写就是按位置传给形参
print(得到数)              # 910

# ------------------------------------2022.7.20--01:57-----------原来就是C语言的有参函数↑-------

得到数 = 求和函数(马=665, 牛=245)                       # 等号左侧的为关键字参数 这样写就是按照关键字传给形参
print(得到数)              # 910


# -------------------------------------------------内存分析-----------------------
def jjj(aaa, bbb):
    print('aaa', aaa)                # aaa 222
    print('bbb', bbb)                # bbb ['加油', '努力', 'gh要用力']
    aaa = 6767
    bbb.append(167167)
    print('aaa', aaa)               # aaa 6767
    print('bbb', bbb)               # bbb ['加油', '努力', 'gh要用力', 167167]
    # return

荔枝 = 222
树枝 = ['加油', '努力', 'gh要用力']
jjj(荔枝, 树枝)
print(荔枝)                           # 222
print(树枝)                           # ['加油', '努力', 'gh要用力', 167167]
'''
在函数调用过程中，进行参数的传递
如果是不可变对象，在函数体的修改不会影响实参的值
如果是可变对象，在函数体的的修改会影响到实参的值
'''


# ----------------------函数的返回值有多个时，结果为元组-----------------------
def 分开(一个列表):
    奇数 = []
    偶数 = []
    for i in 一个列表:
        if i % 2:
            奇数.append(i)
        else:
            偶数.append(i)
    return 奇数, 偶数

lB = [53,2,46 ,81,39,22,56,24]
接收值 = 分开(lB)
print(接收值)                          # ([53, 81, 39], [2, 46, 22, 56, 24])

"""
函数的返回值-return写不写看情况而定
(1)如果函数没有返回值【函数执行完毕之后，不需要给调用处提供数据】return可以省略不写
(2)函数的返回值，如果是1个，直接返回类型
(3)函数的返回值，如果是多个，返回的结果为元组
"""
# ----------------------------------------睡觉2022.7.20--02：47-------------


# ----------------------------------------默认值参数-----------2022.7.20--22:27--
def ii(a, b=1111):           # b为默认值
    print(a, b)

# 开始调用
ii(60)                      # 60 1111      有不写且有默认值就自动默认值
ii(67, 22)                  # 67 22


# ------------------------------参数的定义-----------------2022.7.21  02：13----
"""
·个数可变的位置参数
·定义函数时，可能无法事先确定传递的位置实参的个数时，使用可变的位置参数
·使用*定义个数可变的位置形参
·........结果为一个元组

·个数可变的关键字形参
·定义函数时，无法事先确定传递的关键字实参的个数时，使用可变的关键字形参
·使用**定义个数可变的关键字形参
·........结果为一个字典
"""

def 牛马(*害):                         # 结果为一个元组
    print(害)
    print(害[0])
    print('------------------------')

牛马(20, '荔枝', '苏珊', 666)        # (20, '荔枝', '苏珊', 666)  # 20 # -----------------------
牛马('001', '小镇做题家')            # ('001', '小镇做题家')  # 001  # ------------------------
牛马('虾头')                        # ('虾头',)  # 虾头  # ------------------------

# -------------------------------
def abc(**yc):
    print(yc)
    print(yc['x'])

abc(x=123, y=456, z=789)        # {'x': 123, 'y': 456, 'z': 789}


"""
在一个函数的定义过程中，既有个数可变的关键字形参，也有个数可变的位置形参，要求，个数可变的位置形参，放在个数可变的关键字形参之前
"""
### def aa(*bb,*cc):                    #报错
###     pass

### def aa(**bb,**cc):                    #报错
###     pass

### def aa(**bb,*cc):                    #报错
###     pass

def aa(*bb, **cc):
    pass

print('-----------参数总结-------------')
# -----------------------↓参数总结2022.7.21  22：57--------------

def ppp(a, b, c):
    print(a+b+c)


列表 = [20, 30, 40]
# ppp(列表)              报错
ppp(*列表)                # 在函数调用时，将列表中的每个元素都转换为位置实参传入

ppp(b=47, c=1, a=4)      # 函数的调用之关键字调用

字典 = {'a': 18, 'b': 23, 'c': 11}
ppp(**字典)               # 在函数调用时,将字典中的键值对都转换为关键字实参传入

# -----------------------

def fun(a, b, *, c, d):                         # 从*之后的参数,在函数调用时,只能采用关键字参数传递
    print('a=', a, 'b=', b,'c=', c, 'd=', d)

fun(1, 2, c=3, d=4)                             # a= 1 b= 2 c= 3 d= 4

# ---------定义形参的顺序问题-----------=
def fun1(a, b, *, c, **d):
    pass

def fun2(*a,b,c,**d):
    pass

def fun3(a,b=2,*c,**d):
    pass

# ------结束吧2022.7.21 23：41---------------