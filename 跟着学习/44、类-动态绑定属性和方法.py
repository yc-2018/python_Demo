# 仰晨
# 始时间：2022/7/30 02:00:42
# 文件名：44、类-动态绑定属性和方法

class Student:
    def __init__(self, name, age=20):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + str(self.age) + '多岁了，居然还在吃吃饭')

s111 = Student('张三', 30)
s222 = Student('李四')

s111.eat()                                                                      # 张三30多岁了，居然还在吃吃饭
s222.eat()                                                                      # 李四20多岁了，居然还在吃吃饭

# -------------为s111 单独添加一个 属性《直接写就行》

s111.gender = '男'

print(s111.name, s111.age, s111.gender)                                         # 张三 30 男


# -----------为上222 单独绑定一个 方法
print('----------先定义一个函数------------')

def xyz():
    print('在类之外定义的叫做函数')

s222.i = xyz                                    # 直接关联上，不用加括号

s222.i()                                                                    # 在类之外定义的叫做函数










