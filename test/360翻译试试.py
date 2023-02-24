# By：仰晨
# 文件名：360翻译试试
# 时 间：2023/2/24 15:14
import requests


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
print(requests.post(url=f"https://fanyi.so.com/index/search?eng=1&validate=&ignore_trans=0&query={input('请输入')}",
                    headers=headers).json()["data"]["fanyi"])
