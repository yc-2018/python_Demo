# By：仰晨
# 文件名：有声翻译
# 时 间：2023/2/23 22:20----真tm的够了2.24 2：51明天早课----
#            2.24 15:30----tm的还得是360翻译----16:31tm的多行不行就搞剪贴板---
#            3.05 22:24----大优化cmd窗口+esc关闭&输入其他英语继续翻译&判断如果剪贴板文字为空就让自行输入&其他小优化
#            3.12 16:04----剪贴板内容if包含驼峰命名then拆分成多个单词
#                 16:23----音频文件不缓存了，删掉了1️⃣文件名字方法2️⃣专门多线程播放声音的方法3️⃣去除为缓存文件创建一个文件夹设置为工作路径
#            3.19 04:06----有时候翻译很长的自动播放音频好吵，如果太长了刚开始就不读了按0再读,短的还是自动播放
#                 23:57----判断剪贴板字符串是否包涵英文字母，不存在就重新输入（之前是为空才重新输入，（为空也是不包含英文））
#            3.20 00:12----剪贴板内容if包涵下划线就替换为空格
#            3.22 18:29----引入读文本库读句子，单词声音还是百度取 18:36 剪贴板的.也换为空格
#            6.19 03:22----解决用网络代理就闪退问题
#            6.19 09:37----明确不用代理
#            7.15 14:13----优化：把多个连续的空格变成一个   .后面不为空白字符的.变成空格   导入URL编码（之前剪贴板多行有bug)
#                 15:10----优化：加颜色
#            8.14 21:55----优化：cmd窗口按esc秒关，在pycharm也能秒关，但是没输入回车关闭响应慢了0.几秒


import re

import pyperclip  # 读取剪贴板
import requests

# 播放声音
from io import BytesIO
import sounddevice as sd
import soundfile as sf

# 读文字出声音模块
import pyttsx3

# 监控esc键按了就结束
import threading
from pynput import keyboard
import time

from urllib.parse import quote_plus  # URL编码
from colorama import Fore, Style, init, Back  # 输出颜色

# 初始化colorama，使其在所有支持的平台上都能使用彩色输出
init()  # pycharm不需要，cmd才要

# 使用网络出海会报错所以要明确不要代理
proxies = {
    'http': None,
    'https': None,
}


# 监控esc键，按下就报错
def on_press(key):
    # 检测ESC键是否被按下
    if key == keyboard.Key.esc:
        print("检测ESC键是否被按下 或者 翻译线程结束了...触发系统退出")
        # 触发系统退出
        # raise SystemExit(0)
        raise "你干嘛哎呦"

    # 线程数=2（主线程 翻译线程 监控线程 少了就是不行了，不然按回车监控线程还一直运行)
    time.sleep(0.5)
    if threading.active_count() == 2:
        0/0


# 把英语声音拿到内存 并调用播放   如果太长了刚开始就不读了按0再读
def sound(word):
    mp3 = None  # 单个单词
    say = True  # 读句子
    play_one = False  # 超长第一次？
    engine = pyttsx3.init()  # 初始化语音引擎
    if re.match(r'^[a-zA-Z]+$', word):
        try:
            mp3 = BytesIO(requests.get(f"https://fanyi.baidu.com/gettts?lan=en&text={word}&spd=3&source=web").content)
            say = False  # （非全字母）
        except Exception:
            pass

    while True:
        printf = "——————输入0重新播放音频，直接回车或esc退出，输入其他英语继续翻译——————\n"
        if say:  # 是否是句子
            # print("是句子 启动本地引擎")
            if play_one or word.count(" ") < 6:  # 包涵6个空格表示很长就第一次不读
                # 使用语音引擎朗读文本
                engine.say(word)
                # 运行语音引擎，等待文本朗读完成
                engine.runAndWait()
            else:
                play_one = True
                printf = "——————该句太长 想播放请按0，直接回车或esc退出，输入其他英语继续翻译——————\n"
        else:
            try:
                # print("是单词 启动百度引擎")
                mp3.seek(0)  # 将指针重置为数据的开头
                samples, fs = sf.read(mp3, dtype='float32')
                sd.play(samples, fs)
            except:
                print("********获取不到网络声音，读本地的********")
                # 使用语音引擎朗读文本
                engine.say(word)
                # 运行语音引擎，等待文本朗读完成
                engine.runAndWait()

        print(Back.BLUE + Fore.WHITE + Style.BRIGHT)
        input_why = input(printf)
        print(Style.RESET_ALL)

        if input_why != '0':
            return input_why


# 显示翻译内容
def show_word(e):
    # 显示单词
    print("翻译结果为:" + "——" * 18)
    print(Fore.GREEN + Style.BRIGHT, end='')
    # print(f"@@@@@@@@@@@@@看看打印出来的是什么?----------------------------------{quote_plus(e)}")

    try:
        print(requests.post("https://fanyi.baidu.com/sug", {"kw": e}, proxies=proxies).json()["data"][0]['v'])
    # 显示句子
    except IndexError:
        try:
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

            print(requests.post(
                url=f"https://fanyi.so.com/index/search?eng=1&validate=&ignore_trans=0&query={quote_plus(e)}",
                headers=headers, proxies=proxies).json()["data"]["fanyi"])

        except IndexError:
            print("-----备用翻译也失败了-----")


def main(english1=""):
    # 显示翻译内容
    show_word(english1)
    # threading.Thread(target=show_word, args=(english1,)).start()  # 多线程但不喜欢排序混乱

    # 输出音频 并返回看看是否继续翻译
    english1 = sound(english1)
    if english1 != "":
        main(english1)


if __name__ == '__main__':
    print("（程序要网，如果尝试几次都没输出翻译 那就是翻译api出现问题）剪贴板内容if包含驼峰命名then拆分成多个单词 包涵_就变成空格\n所以想翻译驼峰命名的或者下划线的要重新贴")
    print("《优点：单个单词能有多个结果,短句自动播放音频，长句按0再播放 \n《缺点：本程序只有英文翻译为中文（中文翻译英文只有词可以），短的单词声音也必定播放")
    print("***运行前先复制要翻译的值到剪贴板，运行时会自动获取剪贴板的值进行翻译***")
    # 读取剪贴板内容  包含驼峰命名的就拆分成多个单词，包涵下划线就替换为空格 否则就按原来的输出
    english = re.sub(r'(?<=[^A-Z\s])([A-Z])', r' \1', pyperclip.paste()).replace('_', ' ')
    # 把多个连续的空格变成一个
    english = re.sub(r' +', ' ', english)
    # .后面不为空白字符的.变成空格
    english = re.sub(r'\.(?!\s)', ' ', english)
    print("——" * 20)
    if not bool(re.search(r'[a-zA-Z]', english)):
        english = input("剪贴板内容不包含english，请先输入英文吧~")  # 没办法处理多行的，因为回车就向下执行了
    else:
        print("剪贴板内容为：" + Fore.YELLOW + english)
        print(Style.RESET_ALL, end="")

    # 创建用户输入的线程
    input_thread = threading.Thread(target=main, daemon=True, args={english})
    input_thread.start()

    # 创建键盘监听器--直到按esc结束
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
