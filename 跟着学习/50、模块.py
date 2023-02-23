# 仰晨
# 始时间：2022/8/12 17:15:17
# 文件名：50、模块
"""什么叫模块
·模块
    ·模块英文为Modules·函数与模块的关系
         ·一个模块中可以包含N多个函数
    ·在Python中一个扩展名为.py的文件就是一个模块
    ·使用模块的好处
        ·方便其它程序和脚本的导入并使用
        ·避免函数名和变量名冲突
        ·提高代码的可维护性
        ·提高代码的可重用性
"""
"""
·创建模块
    ·新建一个.py文件，名称尽量不要与Python自带的标准模块名称相同
    
·导入模块
    import 模块名称 [as别名]              (导入全部？。。每次使用都要加前缀 比如：math.pow(2, 4)
    from 模块名称 import 函数/变量/类      (就单个      不用加前缀        比如：pow(2, 4)   
"""

import math                                         # 导入一个关于数学的模块
print(id(math))
print(type(math))                                   # <class 'module'>
print(math)                                         # <module 'math' (built-in)>
print(math.pi)                                      # 3.141592653589793
print('--------------')
print(dir(math))                                    # 查看math所有属性
print(math.pow(2, 4), type(math.pow(2, 4)))         # 2的4次方和他的类型    //16.0 <class 'float'>
print(math.ceil(5.20))                              # 向上取整           //6
print(math.floor(3.141592653589793))                # 向下取整          //3



from math import pow                                 # 导入pow只能用pow,不能用其他的 会报错（不过上面已经导入了全部...）
print(pow(4, 2))                                     # 用from导入就不用加前缀.


'''
怎么使用自己定义的模块呢
   在pycharm中右键文件夹 找到 “将目标标记为”   再找到   “源代码根目录” 点击
                        Mark Directory as       Sources Root
'''

from 计算 import 相加
print(相加(55555, 67))        # 55622
#print(相减(55555, 67))       # 报错NameError: name '相减' is not defined

import 计算
print(计算.相减(55555, 67))     # 55488
print(计算.相乘(5, 3))          # 15





















