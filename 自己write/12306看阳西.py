# By：仰晨
# 文件名：12306看阳西
# 时 间：2022/12/6 20:18
import requests

# date = input('请输入一个日期 如 2022-12-08 ')
url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2022-12-20&leftTicketDTO.from_station=GZQ&leftTicketDTO.to_station=WRQ&purpose_codes=ADULT"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.139 Safari/537.36",
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Content-Type': 'application/json;charset=UTF-8',
            'Referer': 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E5%B9%BF%E5%B7%9E,GZQ&ts=%E9%98%B3%E6%B1%9F,WRQ&date=2022-12-06&flag=N,N,Y'
           }
d = requests.post(url=url, headers=headers).text#.json()['data']['result']
print(d)
#
# for i in d:
#     d[i] = d[i].replace('||', '|*|').replace('||', '|*|').split('|')[3:]
#     d[i][9] = "加密乱码"
#     d[i][36] = "某序号"
#     d[i][29] = "商务：" + d[i][29]
#     d[i][28] = "一等座：" + d[i][28]
#     d[i][27] = "二等座：" + d[i][27]
#     d[i][23] = "无座：" + d[i][23]
#
#     if d[i][4] == "WMQ":
#         print(
#             f"{d[i][10]} 车次:{d[i][0]} 开始时间：{d[i][5]} 到达时间：{d[i][6]}  历时：{d[i][7]}  {d[i][27]}  {d[i][23]}  {d[i][28]}")
