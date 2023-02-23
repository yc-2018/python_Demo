# -*- coding: utf-8 -*-
# @Time    : 2022/10/26 7:41
# @Author  : Naraci
# @File    : 写真优化重构版.py

import parsel
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 '
                  'Safari/537.36 '
}


def url_request(url):
    request = requests.get(url=url, headers=headers)
    # 设置编码格式防止乱码
    request.encoding = 'utf-8'
    html_text = request.text
    # 转换数据类型
    parse_forats = parsel.Selector(html_text)
    parse_forats_list = parse_forats.xpath('//section//div//ul//span/text()').getall()[-1]  # 取该页面总页数
    num_list = [i for i in parse_forats_list if str.isdigit(i)]  # Python isdigit() 方法检测字符串是否只由数字组成。返回True or False.
    add_list = ''
    for i in num_list:
        add_list = add_list + i

    number_end = int(add_list)  # 转换成整数类型
    # 页面地址 https://www.wxept.com/qqmn/rbmn/page/2
    html_url = url
    # 遍历每个页面地址
    for page in range(1, number_end + 1):
        if page == 1:
            request_url = html_url
        else:
            request_url = html_url + '/page/' + str(page)

        for page_list in range(1, number_end + 1):
            request_url.encode('utf-8')
            url_list = requests.get(url=request_url, headers=headers)
            selector = url_list.text
            selector = parsel.Selector(selector)  # 转换数据类型
            content = selector.xpath('//div//div/article')  # 获取所有需要的标签
            for article in content:
                pic_title = article.xpath('./h2/a/text()').get()  # 套图标题 用于命名文件夹  返回为对象属性需要用get取出来
                pic_url = article.xpath('./h2/a/@href').get()
                print('已将相册：' + pic_title + '添加到队列！')
                # 发送相册页面地址
                response_pic = requests.get(url=pic_url, headers=headers).text
                # 获取相册页面所有页数
                selector_2 = parsel.Selector(response_pic)
                img_url = selector_2.xpath('//section/div/a/span').getall()[-2]
                num_list = [i for i in img_url if str.isdigit(i)]  # Python isdigit() 方法检测字符串是否只由数字组成。返回True or False.
                add_list = ''
                number_list = pic_url.split('.html')[0]
                # 遍历出所有页面
                for i in num_list:
                    add_list = add_list + i
                number_end = int(add_list)
                for page in range(1, number_end + 1):
                    if page == 1:
                        request_html_url = number_list + '.html'
                    else:
                        request_html_url = number_list + '.html/' + str(page)
                    print(request_html_url)
                    # 解析图片地址
                    response_pic = requests.get(url=request_html_url, headers=headers).text
                    selector_2 = parsel.Selector(response_pic)
                    img_url = selector_2.xpath('//section//article//a/img/@src').getall()
                    for pic_url in img_url:
                        # 发送图片链接请求，获取图片数据以二进制数据保存
                        img_data = requests.get(url=pic_url, headers=headers).content
                        # 数据保存
                        fil_name = pic_url.split('/')[-1]  # 获取图片名字
                        with open('meitudownload\\' + fil_name, mode='wb') as fp:  # wb 二进制
                            fp.write(img_data)
                            print('下载完成:' + fil_name)


if __name__ == '__main__':
    print('请在文件目录手动新建meitudownload目录')
    print('在下面网址复制url粘贴值下方：https://www.wxept.com/qqmn/')
    put_url = input('请输入正确分类页面url')
    # url = 'https://www.wxept.com/qqmn/dlmn'
    url = put_url
    url_request(url)

    # 文件根目录手动创建meitu文件夹
