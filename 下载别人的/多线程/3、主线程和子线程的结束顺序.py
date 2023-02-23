# By：仰晨
# 文件名：主线程和子线程的结束顺序
# 时 间：2022/10/13 22:47

"""
首先说进程，主进程会等待所有子进程执行结束后再结束
线程也是类似的，主线程会等待所有的子线程执行结束之后再结束

可以清楚的看到，主线程已经结束之后，子线程依旧在运行
"""
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
    eat_thread = threading.Thread(target=eat, args=("giao",))
    drink_thread = threading.Thread(target=drink, kwargs={"name": "qz", "count": 4})

    eat_thread.start()
    drink_thread.start()

    time.sleep(1)
    print("我吃不下也喝不下了！")














