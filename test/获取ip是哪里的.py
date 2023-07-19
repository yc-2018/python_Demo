# By：仰晨
# 文件名：获取ip是哪里的
# 时 间：2023/7/15 15:24


import requests
from datetime import datetime

# 获取当前的日期和时间
now = datetime.today()

# 打印今天是几号
print(now.day)


url = "https://www.bejson.com/Bejson/Api/Ip/getIp?ip=119.8.98.117"

headers = {
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
   'Accept': '*/*',
   'Host': 'www.bejson.com',
   'Connection': 'keep-alive'
}

response = requests.request("POST", url, headers=headers)

print(response.json())
