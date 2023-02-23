import requests
import re
import os
from urllib import parse

reg = r"(?<=href=\")(/video.+?)(?=\")"
re_mp4 = r"v26-web.+?(?=\")"
headers = {"User-Agent": "Mozilla/5.1 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}


# 自己把网页的数据复制到文本文件
def get_txt():
    with open('douyin.txt', 'r', encoding='utf-8') as f:
        txt = f.read()
        url_lst = re.findall(reg, str(txt))
    return url_lst


# 从网页中搞到数据
def get_HTML():
    txt = requests.post("https://www.douyin.com/user/MS4wLjABAAAAEJQhsV2XehwvEi62fy1JEqMiFQ3P6lMXbaSyZc-rUYA",
                        headers=headers).text  # 辛吉飞抖音主页
    url_lst = re.findall(reg, txt)

    print(url_lst)
    print('------------------------')
    return url_lst


url_lst = get_txt()  # 2选一

try:
    os.mkdir('douyin')  # 创建文件夹
except:
    pass

os.chdir('douyin')  # 设置当前路径
i = 0
lose = ''
for u in url_lst:
    mp4 = requests.post(r'https://www.douyin.com' + u, headers).text
    new_txt = parse.unquote(mp4)  # URL解码

    new_mp4 = re.findall(re_mp4, new_txt)
    i += 1
    try:
        print(new_mp4[1])
        with open(str(i) + '.mp4', 'wb') as video:
            video.write(requests.get(r'https://' + new_mp4[1]).content)
            print(i)

    except:
        lose = lose + str(i) + ','
        continue

print('失败有：', lose)
