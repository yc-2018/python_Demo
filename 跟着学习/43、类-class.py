# 仰晨
# 始时间：2022/7/28 23:56:42
# 文件名：43、类-class

class Yc:               # #Student为类的名称（类名）由一个或多个单词组成，每个单词的首字母大写，其余小写(规范不这样也不报错
    pass

# Python中一切皆对象Yc是对象吗?内存有开空间吗?

print(id(Yc))       # 2698097203896
print(type(Yc))     # class 'type'>
print(Yc)           # <class '__main__.Yc'>

# --------------------------------------------------------------

class L类:

    # 类属性
    地方 = '广东'  # 直接写在类里的变量,称为类属性

    # 实体属性
    def __init__(self, 名字, 年龄):         # 名字，年龄 为实体属性
        self.名字 = 名字                    # self.名字 称为实体属性，进行了 一个赋值的操作，将局部变量的name的值赋给实体属性
        self.年龄 = 年龄

    # 实例方法
    def 吃(self):
        print('我叫', self.名字, 'in eat凉拌加鸡蛋ing')
    # 在类之外定义的称为函数,在类之内定义的称为方法

    @classmethod
    def cm(cls):
        print('I‘m类方法，因为用了@classmethod修饰')

    @staticmethod
    def sm():
        print('我是静态方法，因为用了@staticmethod修饰')


print('-------------那么类怎么用呢-------------------------')

学 = L类('仰晨', 22)

print(id(学))            # 1906615093640            他16进制为↓
print(type(学))          # <class '__main__.L类'>
print(学)                # <__main__.L类 object at 0x000001BBEB1D8988>

# ------引用类的2种方法=49行=54行---------
学.吃()                  # 我叫 仰晨 in eat凉拌加鸡蛋ing
                        # 对象名.方法名()
print(学.名字)           # 仰晨
print(学.年龄)           # 22

L类.吃(学)               # 我叫 仰晨 in eat凉拌加鸡蛋ing
                        # 49行代码和54行带码功能是一样的
                        # 类名.方法名（类的对象）--》实际上就是方法定义处的self


学.sm()                  # 我是静态方法，因为用了@staticmethod修饰
L类.sm()                 # 我是静态方法，因为用了@staticmethod修饰

# ----------------------
学.cm()                  # I‘m类方法，因为用了@classmethod修饰
L类.cm()                 # I‘m类方法，因为用了@classmethod修饰

# -------------------------------类属性的使用方法
print(学.地方)         # 广东
L类.地方 = '蔡徐村'

print(学.地方)         # 蔡徐村
print(L类.地方)        # 蔡徐村

