# By：仰晨
# 文件名：1、守护进程试试
# 时 间：2023/7/21 10:16
"""《为翻译程序测试》
帮我写个py，主进程阻塞监控esc键，按了esc键就结束，然后守护进程一直循环打印hello world
----------------------------------------------------------------------------------
守护进程中使用 input() 会导致问题。这是由于守护进程的生命周期是由主（父）进程控制的。
当主进程结束时，所有的守护进程都会被立即终止。
因此，当你尝试在守护进程中使用 input() 来获取用户输入时，如果主进程已经结束，守护进程将无法正常工作，因此会抛出错误。
"""

import multiprocessing
import time
from pynput import keyboard


# 定义一个在子进程中运行的函数，这个函数会一直打印"Hello World"
def print_hello_world():
    while True:
        s = input("ddddddd")
        print(s)
        print("Hello World")

        time.sleep(1)


# 定义一个用于监控ESC键的回调函数
def on_press(key):
    if key == keyboard.Key.esc:
        print("ESC key pressed. Exiting...")
        # 如果监测到ESC键被按下，结束程序
        return False


def main():
    # 创建一个守护进程
    p = multiprocessing.Process(target=print_hello_world)
    # 设置为守护进程，这样主进程结束时，守护进程也会结束
    p.daemon = True
    # 启动守护进程
    p.start()

    # 创建一个键盘监听器
    listener = keyboard.Listener(on_press=on_press)
    # 启动键盘监听器
    listener.start()
    # 等待监听器结束
    listener.join()

    # 程序结束，守护进程也会结束


if __name__ == '__main__':
    main()

# -----------------------------------------------
# if key == keyboard.Key.esc:如果我想按alt+c结束怎么改
"""
# 创建变量，用于检测Alt键是否被按下
is_alt_pressed = False

def on_press(key):
    global is_alt_pressed
    # 检测Alt键是否被按下
    if key == keyboard.Key.alt:
        is_alt_pressed = True
    # 检测C键是否被按下，且Alt键也被按下
    elif key == keyboard.KeyCode(char='c') and is_alt_pressed:
        print("Alt+C pressed. Exiting...")
        return False

def on_release(key):
    global is_alt_pressed
    # 如果Alt键被释放，更新状态
    if key == keyboard.Key.alt:
        is_alt_pressed = False
"""
