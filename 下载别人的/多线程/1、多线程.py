# By：仰晨
# 文件名：多进程
# 时 间：2022/10/13 21:27

# import threading    # 多进程


# --------------------------------------------------------------
import threading
import time


def eat():
    for i in range(4):
        print("一、我吃……", i)
        time.sleep(0.5)


def drink():
    for i in range(4):
        print("二、我喝……", i)
        time.sleep(0.5)


if __name__ == '__main__':
    #                                   通过线程类创建线程对象-------------------------------
    #                                   线程对象 = threading.Thread(target=任务名)---------
    eat_thread = threading.Thread(target=eat)
    drink_thread = threading.Thread(target=drink)

    #                                   启动线程执行任务------------------
    #                                   线程对象.start() ---------------
    eat_thread.start()
    drink_thread.start()

"""
进程和线程对比
1、关系对比
线程是依附在进程里面的，没有进程就没有线程

一个进程默认提供一条线程，进程可以创建多个线程

2、区别对比
创建进程的资源开销要比创建线程的资源开销要大

进程是操作系统资源分配的基本单位，线程是CPU调度的基本单位

线程不能独立执行，必须依存在进程中

3、优缺点对比
进程优点：可以用多核；缺点：资源开销大

线程优点：资源开销小；缺点：不能使用多核（因为线程依附于进程，进程占用一个核）
————————————————
版权声明：本文为CSDN博主「帅帅气气的黑猫警长」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/Hao_ge_666/article/details/120603014"""












