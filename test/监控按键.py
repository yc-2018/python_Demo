# By：仰晨
# 文件名：监控按键
# 时 间：2023/3/5 19:21
import threading
import keyboard
import sys

should_exit = False


def on_key_event(event):
    global should_exit
    # print(event.name)
    if event.name == "esc":
        print("主线程退出")
        should_exit = True
        print(should_exit)
        sys.exit()


keyboard.on_press(on_key_event)


def program_logic():
    while True:
        if input("input:...") == "0":
            break
    print("666666666666666")
    global should_exit
    should_exit = True


program_thread = threading.Thread(target=program_logic)
program_thread.setDaemon(True)
program_thread.start()
i = 1
while not should_exit:
    i += 1
# program_thread.join()
