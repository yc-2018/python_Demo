# By：仰晨
# 文件名：爬wallhaven热榜壁纸
# 时 间：2023/9/12 22:01

import requests
from lxml import etree


# 获取一页的壁纸URL
def get_img_list(page):
    doc = requests.get(f"https://wallhaven.cc/toplist?page={page}").text
    small_list = etree.HTML(doc).xpath("/html/body/main/div/section/ul/li")
    small_pic_list = [pic.xpath("./figure/@data-wallpaper-id")[0] for pic in small_list]
    pic_format_lst = ["png" if len(pic.xpath("./figure/div/span")) == 2 else "jpg" for pic in small_list]
    return [f"https://w.wallhaven.cc/full/{pic[:2]}/wallhaven-{pic}.{f}" for pic, f in zip(small_pic_list, pic_format_lst)]


# 发送到motrix进行下载
def send_motrix_download(page, filename, save_path, index):
    data = {
        'id': 1,
        'jsonrpc': '2.0',
        'method': 'aria2.addUri',
        'params': ['token:ikun666', [url], {'dir': save_path, "out": filename, "max-connection-per-server": "16"}]
    }
    response = requests.post('http://localhost:16800/jsonrpc', json=data)
    print(f"{page}-{index}_.{response.json()}")  # 输出HTTP响应内容


if __name__ == '__main__':
    start_page = int(input('从第几页开始爬'))
    end_page = int(input('第几页结束'))

    for page_ in range(start_page, end_page+1):
        i = 1
        for url in get_img_list(page_):                     # 获取一页的壁纸URL 遍历
            name = f"{page_}-{i}_.{url.split('.')[-1]}"
            path = r'E:\Users\Dell\Desktop\新建文件夹'
            send_motrix_download(page_, name, path, i)      # 发送到motrix进行下载
            i += 1
