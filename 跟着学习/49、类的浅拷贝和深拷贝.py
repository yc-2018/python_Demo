# 仰晨
# 始时间：2022/8/12 15:19:42
# 文件名：49、类的浅拷贝和深拷贝

"""
·变量的赋值操作
        ·只是形成两个变量，实际上还是指向同一个对象
·浅拷贝
        .Python拷贝一般都是浅拷贝，拷贝时，对象包含的子对象内容不拷贝，因此，源对象与拷贝对象会引用同一个子对象
·深拷贝
        ·使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象，源对象和拷贝对象所有的子对象也不相同
"""

class CPU:
    pass

class Disk:
    pass

class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk

# 变量的赋值操作------------------------------
cpu1 = CPU()
cpu2 = cpu1
print(cpu1, id(cpu1))       # <__main__.CPU object at 0x000001CB6F459F88> 1973256822664
print(cpu2, id(cpu2))       # <__main__.CPU object at 0x000001CB6F459F88> 1973256822664

print('----------------------')
# 类的浅拷贝
disk = Disk()                       # 创建一个硬盘类的对象
computer = Computer(cpu1, disk)     # 创建一个计算机类的对象

# 浅拷贝
import copy
computer1 = copy.copy(computer)
print(computer, computer.cpu, computer.disk)        # <__main__.Computer object at 0x000001FB2C03F108> <__main__.CPU object at 0x000001FB2C030548> <__main__.Disk object at 0x000001FB2C03F288>
print(computer1, computer1.cpu, computer1.disk)     # <__main__.Computer object at 0x000001FB2C03F988> <__main__.CPU object at 0x000001FB2C030548> <__main__.Disk object at 0x000001FB2C03F288>
                                                    # 可以看出computer和computer1是不同的对象但是里面包涵的cpu和disk却是相同的
print('---------------------')

# 深拷贝
computer2 = copy.deepcopy(computer)
print(computer, computer.cpu, computer.disk)        # <__main__.Computer object at 0x000001C7AE8C32C8> <__main__.CPU object at 0x000001C7AE8B0548> <__main__.Disk object at 0x000001C7AE8BFA08>
print(computer2, computer2.cpu, computer2.disk)     # <__main__.Computer object at 0x000001C7AEB23D08> <__main__.CPU object at 0x000001C7AEB28CC8> <__main__.Disk object at 0x000001C7AEB28E88>
                                                    # 可以看出computer和computer2是不同的对象而且里面包涵的cpu和disk也不同
print(dir(copy))                                    # 查看copy所有属性


























