# 仰晨
# 始时间：2022/8/1 22:06:49
# 文件名：45、面向对象的3大特征

"""面向对象的三大特征
·封装:提高程序的安全性
    ·将数据（属性）和行为(方法)包装到类对象中。在方法内部对属性进行操作，在类对象的外部调用方法。这样，无需关心方法内部的具体实现细节，从而隔离了复杂度。
    ·在Python中没有专门的修饰符用于属性的私有，如果该属性不希望在类对象外部被访问，前边使用两个“_”。
·继承:提高代码的复用性
·多态:提高程序的可扩展性和可维护性

"""
print('---------------111111111111封装---------------------')

class Students:
    def __init__(self, name, age):
        self.name = name
        self.__age = age                                    # 年龄不希望在类的外部被使用，所以加了两个_

    def aaa(self):
        print('他是', self.name, "今年", self.__age)        # ↑但是可以在类里面使用

stu = Students('ikun', 22)

stu.aaa()                                                   # 他是 ikun 今年 22

# ----在类外使用name, age----

print(stu.name)                 # ikun
# print(stu.__age)              # 报错 AttributeError: 'Student' object has no attribute '__age'
print(dir(stu))
print(stu._Students__age)     # 不希望被使用但可以被使用_Student__age访问  #22


print('--------------------------22222222继承-------------------------')
"""
如果一个类没有继承任何类，则默认继承object
 Python支持多继承
·定义子类时，必须在其构造函数中调用父类的构造函数
"""
class A(object):
    pass

class B(object):
    pass

class C(A, B):
    pass
# --------------------python支持多继承

# -------------------父子

class Person(object):               # Person(人）继承object类
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def 打印(self):
        print(self.name, '它今年', self.age)

class Student(Person):                      # Student(学生）继承Person（人）
    def __init__(self, name, age, No_):
        super().__init__(name, age)           # 继承Person(人）的name, age
        self.No_ = No_

class Teacher(Person):                      # Teacher（老师）也继承Person（人）
    def __init__(self, name, age, cm):
        super().__init__(name, age)           # 用super().继承Person(人）的name, age
        self.cm = cm

学生 = Student('苏珊', 22, '067')
老师 = Teacher('坤坤', 25, '008')

学生.打印()                                 # 苏珊 它今年 22
老师.打印()                                 # 坤坤 它今年 25


print('-------------------3333333333方法重写-------------------------')
"""
方法重写
如果子类对继承自父类的某个属性或方法不满意，可以在子类中对其(方法体)进行重新编写
·子类重写后的方法中可以通过super().xxx()调用父类中被重写的方法
"""

class F父(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def 输出(self):
        print(self.name, 'TA今年', self.age, '岁')

class Z子(F父):
    def __init__(self, name, age, 身高):
        super().__init__(name, age)
        self.身高 = 身高
    def 输出(self):                               # 把父类的def 输出(self):重写
        super().输出()                            # 把父类的def 输出(self):引进（可选）
        print('他身高', self.身高)                 # 加上其他的内容


重写 = Z子('KUN', 25, 182)
重写.输出()                     # KUN TA今年 25 岁
                              # 他身高 182