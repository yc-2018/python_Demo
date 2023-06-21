import requests
import os
import concurrent.futures


def getImg(count, hero):
    while True:
        file_name = hero['cname'] + str(count) + ".jpg"  # 设置图片名
        if os.path.exists(file_name):  # 如果目录本来就有，就跳过
            count += 1
            continue
        else:
            pic_yes = requests.get(
                f'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{hero["ename"]}/{hero["ename"]}-bigskin-{count}.jpg')

            if str(pic_yes) == '<Response [200]>':  # 200就是有，没有就是404
                print('开始写入:' + file_name)

                with open(file_name, 'wb') as pic:
                    pic.write(pic_yes.content)  # 写入图片

            else:
                print('----------------')  # 不存在
                break
            count += 1


if __name__ == '__main__':
    try:
        os.mkdir('ny')  # 创建文件夹
    except FileExistsError:
        pass
    os.chdir('ny')  # 设置当前路径

    url_json = requests.get('https://pvp.qq.com/web201605/js/herolist.json').json()
    print(url_json)

    # 创建一个最大线程数为8的线程池
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        for i in url_json:
            a = 1
            # 提交任务到线程池
            executor.submit(getImg, a, i)

    print("主进程结束了@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
