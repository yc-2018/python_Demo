# By：仰晨
# 文件名：4、设置守护主线程
# 时 间：2022/10/13 22:51
"""
如果我们想让主线程结束之后，子线程也随即结束，那么我们可以使用线程守护

我们可以使用daemon，这个单词意思

daemon
n.（古希腊神话中的）半神半人的精灵
网络：守护进程；守护程序；虚拟光驱
可以在创建线程时候，直接设置daemon
-----------------------------------------------------------
可以在创建线程时候，直接设置daemon
eat_thread = threading.Thread(target=eat,args=("giao",),daemon=True)
-----------------------------------------------------------
也可以创建进程之后，启动线程之前，设置daemon
drink_thread = threading.Thread(target=drink,kwargs={"name":"qz","count":4})
drink_thread.daemon = True
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
    eat_thread = threading.Thread(target=eat, args=("giao",), daemon=True)
    drink_thread = threading.Thread(target=drink, kwargs={"name": "qz", "count": 4})
    drink_thread.daemon = True

    eat_thread.start()
    drink_thread.start()

    time.sleep(1)
    print("我吃不下也喝不下了！")














