# By：仰晨
# 文件名：bs4爬pngimg全站图片链接
# 时 间：2022/12/9 3:18
import os
import requests as req
from bs4 import BeautifulSoup


def get_html(url_text):
    iii = 0
    while iii < 3:
        try:
            html = req.get(url_text, timeout=5).text        # 5秒就报错
            return html
        except req.exceptions.RequestException:
            iii += 1
    if iii == 3:
        raise Exception("请求超时-----")        # 主动报错


word_dir = os.getcwd()  # 获取当前目录
try:
    os.mkdir('pngTXT')  # 创建文件夹
except FileExistsError:
    pass
os.chdir('pngTXT')  # 设置当前路径

url = "https://pngimg.com"
html_doc = req.get(url).text  # 加了请求头反而返回空
# print(html_doc)
res = BeautifulSoup(html_doc, 'lxml')

# 链接的倒数第而个就是大类是名字
print('开始拿每个大类的每个物体')
aa = res.select('.sub_category a')
element = []
for i in aa:
    element.append(url + i.get("href"))
print(element)
print(len(element))

print('开始拿的每个物体的每个图片')
for i in element:
    # 如果一次没爬完就 重复了 那就多写个if
    txt_name = i.split('/')[-2] + ' ' + i.split('/')[-1] + '.txt'
    if not os.path.exists(txt_name):  # 如果不存在文件就执行，不然就是爬过了就跳过
        get_link = get_html(i)        # 获取图片网页的内容
        # print(get_link)
        pic_lst_ = BeautifulSoup(get_link, 'lxml').find_all(name='link', attrs={
            'itemprop': 'contentUrl'})  # 图片连接都有一个属性itemprop="contentUrl"
        print(len(pic_lst_))

        with open(txt_name, 'w') as txt:
            for ii in pic_lst_:
                txt.write(url + ii.get("href") + '\n')

        print(i.split('/')[-1] + '--ok?')
