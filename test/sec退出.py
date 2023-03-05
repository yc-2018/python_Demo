# By：仰晨
# 文件名：sec退出
# 时 间：2023/3/5 21:00

import keyboard
import ctypes       # Python 标准库中自带的模块,它提供了一种与 C 语言兼容的外部函数库的接口

"""py 程序监听 如果esc键就关闭当前窗口"""


def on_key_event(event):
    if event.name == "esc":
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        ctypes.windll.user32.SendMessageW(hwnd, 0x0010, 0, 0)


keyboard.on_press(on_key_event)
keyboard.wait()

print(input(666))
