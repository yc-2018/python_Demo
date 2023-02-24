# By：仰晨
# 文件名：有声翻译
# 时 间：2023/2/23 22:20----真他妈的够了2023.2.24 2：51明天早课----2023.2.24 15:30他妈的还得是360翻译
import os
import time
import requests
from playsound import playsound


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
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.139 Safari/537.36",
        }
        print(
            requests.post(url=f"https://fanyi.so.com/index/search?eng=1&validate=&ignore_trans=0&query={english}",
                          headers=headers).json()["data"]["fanyi"])
        # 因为百度的查询限制在38个汉字以内。
        # from lxml import etree
        # headers = {"User-Agent": "Mozilla/5.1 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
        # try:
        #     html = requests.get(f"https://www.sogou.com/web?query=翻译{english}", headers=headers).text
        #     print(etree.HTML(html).xpath("//dd[@id]//span")[0].text)
        # except Exception:
        #     html = requests.get(f"https://www.baidu.com/s?ie=utf-8&wd=翻译{english}", headers=headers).text
        #     print(etree.HTML(html).xpath("//div[@class='op_sp_fanyi']//p[class='op_sp_fanyi_line_two']")[0].text)


if __name__ == '__main__':

    english = input("输入英语")

    try:
        os.mkdir('sound')  # 创建文件夹
    except FileExistsError:
        pass
    finally:
        os.chdir('sound')  # 设置当前路径

    try:
        show_word()
    except IndexError:
        print("-----连360翻译都失败了-----")

    # 输出音频
    sound(english)


input()
