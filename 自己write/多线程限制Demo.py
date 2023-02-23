# By：仰晨
# 文件名：多线程限制Demo
# 时 间：2023/2/16 15:34
import threading


def method(a):
    # 获取信号量以确保线程数不超过5
    semaphore.acquire()

    for j in range(100):
        print(j, end='-')
    print(a)

    # 线程完成时释放信号量
    semaphore.release()


# 使用最大值为5的BoundedSemaphore对象创建
semaphore = threading.BoundedSemaphore(value=1)  # 1就相当于单线程

# 创建10个线程
for i in range(10):
    t = threading.Thread(target=method, args=("ikun",))
    t.start()


