# By：仰晨
# 文件名：试试post请求
# 时 间：2022/10/31 12:59
import requests
url = 'http://192.168.150.88/'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/62.0"}

dit = {
    'username': '202210001182',
    'pwd': '01120012'
}

ss = requests.post(url, params=dit, headers=headers)
ssbm = ss.encoding
ss.encoding = ssbm
print(ss.text)

print(requests.get(' http://baidu.com').text)










