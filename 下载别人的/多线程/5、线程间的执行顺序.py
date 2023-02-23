# By：仰晨
# 文件名：5、线程间的执行顺序
# 时 间：2022/10/13 22:55
"""
线程之间的执行是无序的，是由CPU调度决定的。

我们可以用current_thread()方法获取线程对象，通过线程的名字来确定运行的顺序
"""
import threading    # 导入多进程
import time


def test():
    time.sleep(1)
    thread = threading.current_thread()
    print(thread)


if __name__ == '__main__':
    for i in range(5):
        threading.Thread(target=test).start()















