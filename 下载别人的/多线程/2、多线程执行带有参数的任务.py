# By：仰晨
# 文件名：多线程执行带有参数的任务
# 时 间：2022/10/13 22:38

import threading
import time


def eat(name):
    for i in range(4):
        print(name + "我吃……")
        time.sleep(0.5)


def drink(name, count):
    for i in range(count):
        print(name + "我喝……")
        time.sleep(0.5)


if __name__ == '__main__':
    #                                         args使用方式
    eat_thread = threading.Thread(target=eat, args=("giao",))        # 此处要注意的是，args如果只有一个元素，后面的逗号不能省略
    #                                           kwargs使用方式
    drink_thread = threading.Thread(target=drink, kwargs={"name": "qz", "count": 5})

    eat_thread.start()
    drink_thread.start()















