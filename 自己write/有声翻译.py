# By：仰晨
# 文件名：有声翻译
# 时 间：2023/2/23 22:20----真tm的够了2023.2.24 2：51明天早课----2023.2.24 15:30tm的还得是360翻译----16:31tm的多行不行就搞剪贴板
import os
import threading

import pyperclip
import requests
from playsound import playsound
# from pydub import audio_segment
# from pydub.playback import play


def sound(word):
    url = f"https://fanyi.baidu.com/gettts?lan=en&text={word}&spd=3&source=web"

    content = requests.get(url).content
    with open(getName(word), "bw") as mp3:
        mp3.write(content)
        mp3.close()
    while True:
        # time.sleep(0.5)
        threading.Thread(target=play_mp3, args=(word,)).start()
        if input("——————输入0重新播放音频，直接回车退出——————") != '0':
            break


def play_mp3(word):
    try:
        # 第三方库播放-垃j第三方库,有时读不了就调用系统的
        playsound(os.getcwd() + '\\' + getName(word))
        # play(audio_segment.AudioSegment.from_mp3(file=os.getcwd() + '\\' + getName(word)))
    except Exception as e:
        # 调用默认播放器播放
        print('报错了' + str(e))
        os.system(getName(word))


def getName(words):
    return words[:50].replace('\n', ' ') + '.mp3'  # 太长或换行都不行


def show_word():
    # 显示单词
    try:
        print(requests.post("https://fanyi.baidu.com/sug", {"kw": english}).json()["data"][0]['v'])
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
            requests.post(url=f"https://fanyi.so.com/index/search?eng=1&validate=&ignore_trans=0&query={english}"
                          .replace(' ', '+').replace('\n', '%0A'),
                          headers=headers).json()["data"]["fanyi"])


if __name__ == '__main__':

    # english = input("输入英语")     # 没办法处理多行的
    print("***运行前应该先复制要翻译的值到剪贴板，运行时会自动获取剪贴板的值进行翻译***")
    english = pyperclip.paste()  # 读取剪贴板内容
    print("剪贴板内容为：" + english)

    if not os.path.exists('sound'):
        os.mkdir('sound')  # 创建文件夹
    os.chdir('sound')  # 设置当前路径

    try:
        show_word()
    except IndexError:
        print("-----连360都失败了-----")

    # 输出音频
    sound(english)
