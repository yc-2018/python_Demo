# 仰晨
# 始时间：2022/8/7 17:27:38
# 文件名：48、特殊属性、方法

"""
特殊属性
__dict__获得类对象或实例对象所绑定的所有属性和方法的字典

"""
print(dir(object))              # 查看object类的属性和方法

class A:
    pass

class B:
    pass

class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age

class D(A):
    pass


print('-------特殊属性---------------')
# 创建C类的对象
x = C('仰晨', 20)             # x 是C类的一个实例对象
print(x.__dict__)            # 实例对象的属性字典
print(C.__dict__)            # 类对象的字典
print('---------------')
print(x.__class__)           # 输出对象所属的类//<class '__main__.C'>
print(C.__bases__)           # 查看C的所有父类的元素
print(C.__base__)            # 查看C的第一个父类
print(C.__mro__)             # 查看类的层次结构
print(A.__subclasses__())    # 查看A的子类(列表


"""
特殊方法
__len__()通过重写__len___()方法，让内置函数len()的参数可以是自定义类型
__add__()通过重写__add__()方法，可使用自定义对象具有“+”功能
__new__()用于创建对象
__init__()对创建的对象讲行初始化
"""
print('------特殊方法--------------------')

a = 12
b = 24
c = a + b
print(c)                 # 36
d = a.__add__(b)
print(d)                # 36


class Student:
    def __init__(self, name):
        self.name = name
    def __add__(self, other):
        return self.name + other.name
    def __len__(self):
        return len(self.name)

stu1 = Student('小黑子')
stu2 = Student('苏珊')

s = stu1 + stu2                     # 实现了2个对象的加法运算（因为在Student中编写了__add__()的特殊方法）
print(s)                            # 小黑子苏珊
s= stu1.__add__(stu2)               # 相当+号
print(s)                            # 小黑子苏珊

print('---------------')
列表 = [11, 22, 33, 44]
print(len(列表))                      # 4
print(列表.__len__())                 # 4

# print(len(stu1))                  # 未在类 Student中修改————len———时会报错
print(len(stu1))                    # 3
print(stu1.__len__())               # 3


# ---------难以理解的__new__()和__init__()-----------------------------
print('--难以理解的__new__()和__init__()--')

class Abc(object):
    def __new__(cls, *args, **kwargs):
        print('__new__被调用,cls的值为：{0}'.format(id(cls)))          # 2184
        obj = super().__new__(cls)
        print('创建的对象的ID为：{0}'.format(id(obj)))                          # 0584
        return obj

    def __init__(self, name, age):
        print('__init__被调用，self的ID为：{0}'.format(id(self)))              # 0584
        self.name = name
        self.age = age

print('object这个类对象的ID为：{0}'.format(id(object)))                                 # 0880
print('Abc这个类对象的ID为：{0}'.format(id(Abc)))                       # 2184

# 创建实例对象
ikun = Abc('篮球', 20)
print('ikun这个Abc类的实例对象的ID为：{0}'.format(id(ikun)))                    # 0584












