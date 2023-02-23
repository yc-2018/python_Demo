# 仰晨
# 始时间：2022/8/20 01:29:36
# 文件名：自己琢磨pic
# 网站/robots.txt  看网址给你爬什么（人道主义）

import requests
from lxml import etree
import os

url = 'https://pngimg.com/images/animals/anaconda'       # 网络请求包
浏览器标识 = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.139 Safari/537.36'}


网络请求 = requests.get(url).text                    # 获取网络响应,tmd这个网站加了浏览器标识反而会出现问题，浪费这么久时间
# print(网络请求)                                             # <Response [200]>


html = etree.HTML(网络请求)
# print(html)

网址列表 = html.xpath('//@src')

a = 1
for i in 网址列表:
    if i.find('small') != -1:
        print('开始第{}次'.format(a))
        if a == 1:
            try:
                当前的工作目录 = os.getcwd()  # 返回当前的工作目录
                创建目录 = os.mkdir(i.split('/')[2])

            except FileExistsError:
                pass
            os.chdir('{0}\\{1}'.format(当前的工作目录, i.split('/')[2]))  # 将设置为当前工作目录

        with open(i.split('/')[-1], 'wb') as png:
            png.write(requests.get('https://pngimg.com'+i.replace('/small', '')).content)
            a = a + 1
print('---------------------运行结束---------------')