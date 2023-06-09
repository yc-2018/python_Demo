# 仰晨
# 始时间：2022/8/12 22:48:36
# 文件名：52、包

"""Python中的包
·包是一个分层次的目录结构，它将一组功能相近的模块组织在一个目录下
·作用:
    ·代码规范
    ·避免模块名称冲突
·包与目录的区别
    ·包含_init__.py文件的目录称为包
    ·目录里通常不包含_init__.py文件
·包的导入
    import 包名.模块名
"""

import 试试包.模块1 as bao       # bao是 《试试包.模块1 》的别名，也可以说是简写
print(bao.a)

print('----用import方法导入时，只能跟包名或者模块名----')

from 试试包 import 模块2
print(模块2.b)

print('----用from * import方法可以导入 包、模块、函数、变量----')

from 试试包.模块3 import c

print(c)

































