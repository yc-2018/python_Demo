# By：仰晨
# 文件名：爬wallhaven热榜壁纸
# 时 间：2023/9/12 22:01

import requests
from lxml import etree
doc = requests.get("https://wallhaven.cc/toplist?page=1").text
small_list = etree.HTML(doc).xpath("/html/body/main/div/section/ul/li")
small_pic_list = [pic.xpath("./figure/@data-wallpaper-id")[0] for pic in small_list]
pic_format_lst = ["png" if len(pic.xpath("./figure/div/span")) == 2 else "jpg" for pic in small_list]
pic_url_list = [f"https://w.wallhaven.cc/full/{pic[:2]}/wallhaven-{pic}.{f}" for pic, f in zip(small_pic_list, pic_format_lst)]

for url in pic_url_list:
    filename = url.split('/')[-1].replace('wallhaven-', '')
    save_path = r'E:\Users\Dell\Desktop\新建文件夹'

    # 构建POST请求数据    token没开好像是可以为空，的看别人js脚本说加就必须要加在第一个 max-connection-per-server可不写  out可以不写
    data = {
        'jsonrpc': '2.0',
        'id': '1',
        'method': 'aria2.addUri',
        'params': ['token:OTDbw1UqdUV5', [url], {'dir': save_path, "out": filename, "max-connection-per-server": "16"}]
    }
    # 发送POST请求  , verify=True 表示开启 SSL 证书验证  没什么乱用   还是下载不了HTTPS协议的图片
    response = requests.post('http://localhost:16800/jsonrpc', json=data)
    # 输出HTTP响应内容
    print(response.json())

