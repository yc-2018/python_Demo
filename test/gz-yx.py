# By：仰晨
# 文件名：gz-yx
# 时 间：2023/6/29 10:17
import requests

url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2023-06-29&leftTicketDTO.from_station=WMQ&leftTicketDTO.to_station=GZQ&purpose_codes=0X00"


headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.139 Safari/537.36',
   'Accept': '*/*',
   'Host': 'kyfw.12306.cn',
   'Connection': 'keep-alive',
    'Referer': 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E9%98%B3%E8%A5%BF,WMQ&ts=%E5%B9%BF%E5%B7%9E,GZQ&flag=Y,N,Y',
    'X-Requested-With': 'XMLHttpRequest'

}

response = requests.get(url, headers=headers)

print(response.text)
