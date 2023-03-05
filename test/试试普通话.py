# By：仰晨
# 文件名：试试普通话
# 时 间：2023/2/28 22:12

import requests
import time
print(str(time.time()).split('.')[0])

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '367',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'epass.cltt.org',
    'Origin': 'http://bm.cltt.org',
    'Referer': 'http://bm.cltt.org/',
    'S-Auth-AppId': '64e43635ea9344baaac25b1059d09697',
    'S-Auth-Nonce': '08b33262-7a56-45bf-924d-a13c4b958643',                 # 变了
    'S-Auth-Signature': 'o64DIhgjnGoNJs3UJRyZBzgBpCu+Dm8+en4NEA1Jxc4=',     # 变了
    'S-Auth-Stage': 'RELEASE',
    'S-Auth-Timestamp': str(time.time()).split('.')[0],                                    # 变了
    'S-Auth-Version': '1',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.139 Safari/537.36'
}
data = {"params": {"type": "1", "appId": "bm",
                   "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiIiwiZGF0YVNvdXJjZUtleSI6IiIsInBob25lIjoiMTUxMTk0NTMxNDYiLCJhcHBOYW1lIjoiYm0iLCJ1c2VySWQiOiIxNTY3NTM1NzE0Mjg3MzUzODU4IiwiaWF0IjoxNjc3NTkyODc1LCJvcmdJZCI6IiJ9.s19rY_7XIa4bSD1s1OIfTQUJzMtY82WSXAyzQW4zJQM",
                   "provinceId": "guangdong"}}

print(
    requests.post(url="https://epass.cltt.org/prod/bm/signup/listOpeningTestStation", headers=headers, data=data).text)
