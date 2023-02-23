# 仰晨
# 始时间：2022/8/21 02:42:16
# 文件名：看jd

import requests
import json
import openpyxl
创建表格 = openpyxl.Workbook()                      # Workbook   WWWWW 大写的，他妈的小写搞了一晚2022.8.24 03：24
表格 = 创建表格.create_sheet('工作表名字', 0)           # 0 代表单元格位置

def 获取网页文本(url):
    headers0 = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/62.0"}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.139 Safari/537.36'}
    r = requests.get(url, headers=headers)
    编码 = r.encoding
    r.encoding = 编码
    return r.text


url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100006262957&score=4&sortType=5&page=0&pageSize=11&isShadowSku=1&fold=4'
js = 获取网页文本(url).replace('fetchJSON_comment98(', '').replace(');', '')        # .replace()自带的替换函数
print('-----------',js)
js数据 = json.loads(js)
内容 = js数据['comments']
for a in 内容:
    类型 = a['productColor']
    时间 = a["referenceTime"]
    表格.append([类型, 时间])
    print(类型, '\t', 时间)
print('原数据：', js)
创建表格.save(r'E:\Users\Dell\Desktop\ss.xlsx')                                     # 保存输出
print('-----------------打印结束---------------------------')




































