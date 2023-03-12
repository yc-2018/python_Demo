# By：仰晨
# 文件名：有声翻译
# 时 间：2023/2/23 22:20----真tm的够了2.24 2：51明天早课----
#            2.24 15:30----tm的还得是360翻译----16:31tm的多行不行就搞剪贴板---
#            3.5 22:24-----大优化cmd窗口+esc关闭&输入其他英语继续翻译&判断如果剪贴板文字为空就让自行输入&其他小优化
#            3.12 16:04----剪贴板内容if包含驼峰命名then拆分成多个单词
#                 16:23----音频文件不缓存了，删掉了1️⃣文件名字方法2️⃣专门多线程播放声音的方法3️⃣去除为缓存文件创建一个文件夹设置为工作路径

import re

import pyperclip    # 读取剪贴板
import requests
# 播放声音
from io import BytesIO
import sounddevice as sd
import soundfile as sf
# 关闭当前窗口 只对cmd窗口有效
import keyboard
import ctypes       # Python 标准库中自带的模块,它提供了一种与 C 语言兼容的外部函数库的接口


# 关闭当前窗口 只对cmd窗口有效
def on_key_event(event):
    if event.name == "esc":
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        ctypes.windll.user32.SendMessageW(hwnd, 0x0010, 0, 0)


# 下载英语声音 并调用播放
def sound(word):
    mp3 = BytesIO(requests.get(f"https://fanyi.baidu.com/gettts?lan=en&text={word}&spd=3&source=web").content)
    while True:
        mp3.seek(0)  # 将指针重置为数据的开头
        samples, fs = sf.read(mp3, dtype='float32')
        sd.play(samples, fs)
        input_why = input("——————输入0重新播放音频，直接回车或esc退出，输入其他英语继续翻译——————\n")
        if input_why != '0':
            return input_why


# 显示翻译内容
def show_word(e):
    # 显示单词
    print("翻译结果为:"+"——"*18)
    try:
        print(requests.post("https://fanyi.baidu.com/sug", {"kw": e}).json()["data"][0]['v'])
    # 显示句子
    except IndexError:
        headers = {
            "accept-language": "zh-CN,zh;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "pro": "fanyi",
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": "empty",
            "ec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/98.0.4758.139 Safari/537.36",
        }
        print(
            requests.post(url=f"https://fanyi.so.com/index/search?eng=1&validate=&ignore_trans=0&query={e}"
                          .replace(' ', '+').replace('\n', '%0A'),
                          headers=headers).json()["data"]["fanyi"])


def main(english1=""):

    try:
        show_word(english1)
        # threading.Thread(target=show_word, args=(english1,)).start()  # 多线程但不喜欢排序混乱
    except IndexError:
        print("-----连360都失败了-----")

    # 输出音频 并返回看看是否继续翻译
    english1 = sound(english1)
    if not english1 == "":
        main(english1)


if __name__ == '__main__':
    keyboard.on_press(on_key_event)  # 键盘监听esc就退出 关闭当前窗口 只对cmd窗口有效
    print("（程序要网，如果尝试几次都没输出翻译 那就是翻译api出现问题）剪贴板内容if包含驼峰命名then拆分成多个单词")
    print("《优点：单个单词能有多个结果 《缺点：本程序只有英文翻译为中文，声音也必定播放")
    print("***运行前先复制要翻译的值到剪贴板，运行时会自动获取剪贴板的值进行翻译***")
    english = re.sub(r'(?<=[^A-Z\s])([A-Z])', r' \1', pyperclip.paste())  # 读取剪贴板内容  包含驼峰命名的就拆分成多个单词，如果输入没有驼峰命名就按原来的输出
    print("——" * 20)
    if english == "":
        english = input("剪贴板文字为空，请先输入英文吧~")     # 没办法处理多行的
    else:
        print("剪贴板内容为：" + english)

    main(english)
