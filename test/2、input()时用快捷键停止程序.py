# By：仰晨
# 文件名：2、input()时用快捷键停止程序
# 时 间：2023/7/21 10:42
import threading
from pynput import keyboard
"""《为翻译程序测试》"""


def monitor_input():
    while True:
        try:
            input_str = input("Please enter something: ")
            print(f"You entered: {input_str}")
        except EOFError:
            break


def on_press(key):
    # 检测ESC键是否被按下
    if key == keyboard.Key.esc:
        print("ESC key pressed. Exiting...")
        # 触发系统退出
        # raise SystemExit(0)
        raise "你干嘛哎呦"
        # 1/0

    print(f"线程数量:{threading.active_count()}")


def main():
    # 创建用户输入的线程
    input_thread = threading.Thread(target=monitor_input, daemon=True)
    input_thread.start()

    # 创建键盘监听器
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == '__main__':
    main()
