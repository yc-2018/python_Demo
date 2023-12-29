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
#           12.30 01:02----添加百度翻译api 和 网上找的一个，把每个翻译抽取为方法，去掉百度发声，统一本地发声。优化360接口中文也能翻译了 优化方法排序
#                 01:20----优化第一次不会自动播放纯中文的声音了
import os
import re

import pyperclip  # 读取剪贴板
import requests

# 读文字出声音模块
import pyttsx3

# 监控esc键按了就结束
import threading
from pynput import keyboard
import time

# 百度api要用的
import random
from hashlib import md5

from urllib.parse import quote_plus  # URL编码
from colorama import Fore, Style, init, Back  # 输出颜色

# 初始化colorama，使其在所有支持的平台上都能使用彩色输出
init()  # pycharm不需要，cmd才要

# 使用网络出海会报错所以要明确不要代理
proxies = {'http': None, 'https': None}


def start_transl(translation_text=""):
    """翻译入口"""
    # 显示翻译内容  # threading.Thread(target=show_word, args=(translation_text,)).start()  # 多线程但不喜欢排序混乱
    show_word(translation_text)

    # 输出音频 并返回看看是否继续翻译
    translation_text = sound(translation_text)

    if translation_text != "":
        start_transl(translation_text)


# 显示翻译内容
def show_word(word):
    """显示翻译内容"""
    print("翻译结果为:" + "——" * 18)
    print(Fore.GREEN + Style.BRIGHT, end='')

    # 调用翻译api接口，并直接打印出来
    free_88_word_translation(word)


def free_88_word_translation(word):
    """88邮箱单词翻译: 连句子来了也只会翻译第一个单词"""
    try:
        if not bool(re.match(r'^[a-zA-Z]+$', word)):  # 判断字符串只有大小写字母
            raise "88翻译不了句子"
        url = "https://mail.88.com/api/x/wcw/wordMean"
        _json = requests.get(url, {"word": word}, proxies=proxies, timeout=2).json()['var']['means']
        print("\n".join(f"{c}=>{v}" for c, v in ((item.get('c', ''), item.get('v', '')) for item in _json)))
    except:
        baidu_api_translation(word)


def baidu_api_translation(query):
    """百度翻译api 要申请的哇 有次数的哇"""
    try:
        # 设置您自己的appid/appkey。直接放环境变量（安全)
        appid = os.getenv('BDid')
        appkey = os.getenv('BDkey')
        if appid is None:
            raise "没key翻译不了句子"

        # 有关语言代码的列表，请参阅`https://api.fanyi.baidu.com/doc/21`
        from_lang = 'en'
        to_lang = 'zh'

        if not bool(re.search(r'[a-zA-Z]', query)):  # 判断字符串是否包涵大小写字母
            from_lang = 'zh'
            to_lang = 'en'

        url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'

        # 生成盐并签名
        salt = random.randint(32768, 65536)
        sign = md5((appid + query + str(salt) + appkey).encode('utf-8')).hexdigest()

        # 生成请求
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

        # 发送请求
        r = requests.post(url, params=payload, headers=headers)
        result = r.json()['trans_result']

        # 显示响应
        print("\n".join(item['dst'] for item in result))

    except:
        baidu_word_translation(query)


def baidu_word_translation(word):
    """百度单词翻译"""
    try:
        url = "https://fanyi.baidu.com/sug"
        print(requests.post(url, {"kw": word}, proxies=proxies, timeout=2).json()["data"][0]['v'])
    except IndexError:
        free_360_translation(word)


def free_360_translation(word):
    """360免费翻译"""
    try:
        headers = {
            "accept-language": "zh-CN,zh;q=0.9", "accept-encoding": "gzip, deflate, br",
            "pro": "fanyi", "sec-ch-ua-platform": "Windows", "sec-fetch-dest": "empty",
            "ec-fetch-mode": "cors", "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)",
        }
        eng = 1 if bool(re.search(r'[a-zA-Z]', word)) else 0  # 1就是英译中  0就是中译英
        url = f"https://fanyi.so.com/index/search?eng={eng}&validate=&ignore_trans=0&query={quote_plus(word)}"
        print(requests.post(url=url, headers=headers, proxies=proxies, timeout=3).json()["data"]["fanyi"])
    except:
        free_api_translation(word)


def free_api_translation(word):
    """网上免费翻译api,不知道什么时候会失效而已"""
    try:
        url = f"https://findmyip.net/api/translate.php?text={quote_plus(word)}"
        print(requests.get(url, proxies=proxies, timeout=4).json()['data']['translate_result'])
    except:
        print("-----全部翻译接口都失败了-----")


# 播放声音
def sound(word):
    """把文本声音拿到内存 并调用播放   如果太长了刚开始就不读了按0再读"""
    play_one = False  # 超长第一次？
    engine = pyttsx3.init()  # 初始化语音引擎

    while True:
        printf = "——————输入0重新播放音频，直接回车或esc退出，输入其他英语继续翻译——————\n"

        # 朗读条件: 文本少于3个空格 且 文本带有英文字母 或者不是第一次播放
        if (play_one or word.count(" ") < 3) and (bool(re.search(r'[a-zA-Z]', word)) or play_one):
            # 使用语音引擎朗读文本
            engine.say(word)
            # 运行语音引擎，等待文本朗读完成
            engine.runAndWait()
        else:
            play_one = True
            printf = "——————该句太长 想播放请按0，直接回车或esc退出，输入其他英语继续翻译——————\n"

        print(Back.BLUE + Fore.WHITE + Style.BRIGHT)
        input_why = input(printf)
        print(Style.RESET_ALL)

        if input_why != '0':
            return input_why


# 监控esc键，按下就报错（退出程序)
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
        0 / 0


if __name__ == '__main__':
    print("""
    剪贴板内容包含驼峰命名就会拆分成多个单词 包涵_就变成空格 
    《优点：单个单词能有多个结果,短句自动播放音频，长句按0再播放 
    《缺点：短的单词声音也必定播放 
    ***运行前先复制英文要翻译的值到剪贴板，运行时会自动获取剪贴板的值进行翻译*** """)

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
    input_thread = threading.Thread(target=start_transl, daemon=True, args={english})
    input_thread.start()

    # 创建键盘监听器--直到按esc结束
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
