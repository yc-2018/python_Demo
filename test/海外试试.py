# By：仰晨
# 文件名：海外试试
# 时 间：2023/7/13 15:04

import requests

# 使用网络出海会报错所以要明确代理用不用，如果不用就写None
proxies = {
    'http': "127.0.0.1:2334",
    'https': "127.0.0.1:2334",
}

url = 'https://ss.weiwei.in/2020.html'

print(requests.get(url, proxies=proxies).text)