# 仰晨
# 始时间：2022/8/2 02:31:16
# 文件名：46、object类

"""
. object类是所有类的父类，因此所有类都有object类的属性和方法。
·内置函数dir()可以查看指定对象所有属性
Object有一个_str_()方法，用于返回一个对于“对象的描述”，对应于内置函数str()经常用于print()方法，帮我们查看对象的信息，所以我们经常会对_str__()进行重写
"""

class Student:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '{0}会Ctrl,可他才{1}岁啊'.format(self.name, self.age)


print(dir(Student))                                     # 查看指定对象所有属性

aaa = Student('鲲鲲', 24)
print('--------------------------------')
print(aaa)                                              # 原本的    <__main__.Student object at 0x00000181D048CDC8>
                                                        # 修改后     鲲鲲会Ctrl,可他才24岁啊
print(type(aaa))                                        # <class '__main__.Student'>






























