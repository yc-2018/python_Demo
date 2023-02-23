# By：仰晨
# 文件名：有声翻译
# 时 间：2023/2/23 22:20----真他妈的够了2023.2.24 2：51明天早课
import os
import time
import requests
from playsound import playsound
from lxml import etree


def sound(word):
    url = f"https://fanyi.baidu.com/gettts?lan=en&text={word}&spd=3&source=web"

    content = requests.get(url).content
    with open(f"{word}.mp3", "bw") as mp3:
        mp3.write(content)

    # 第三方库播放-写完还马上读不了，垃圾第三方库
    time.sleep(0.5)
    playsound(f"{word}.mp3")
    # 调用默认播放器播放
    # os.system(f"{english}.mp3")


if __name__ == '__main__':

    english = input("输入英语")

    try:
        os.mkdir('sound')  # 创建文件夹
    except FileExistsError:
        pass
    finally:
        os.chdir('sound')  # 设置当前路径

    # 输出音频
    sound(english)

    # 显示单词
    try:
        print(requests.post("https://fanyi.baidu.com/sug", {"kw": english}).json()["data"][0]['v'])
    except IndexError:
        headers = {"User-Agent": "Mozilla/5.1 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
        html = requests.get(f"https://www.sogou.com/web?query=翻译{english}", headers=headers).text

        print(etree.HTML(html).xpath("//dd[@id]//span")[0].text)

input()
