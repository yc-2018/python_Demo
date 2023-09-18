# By：仰晨
# 文件名：获取王者全英雄高清图--2023.2.16+多线程
# 时 间：2022/12/9 20:32
import threading
import requests
import os


def getImg(hero):
    count = 1
    # 获取信号量以确保线程数不超过8
    semaphore.acquire()

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

    # 线程完成时释放信号量-------------------------------------
    semaphore.release()


if __name__ == '__main__':
    try:
        os.mkdir('ny')  # 创建文件夹
    except FileExistsError:
        pass
    os.chdir('ny')  # 设置当前路径

    url_json = requests.get('https://pvp.qq.com/web201605/js/herolist.json').json()
    print(url_json)

    # 限制多线程使用最大值为8的BoundedSemaphore对象创建
    semaphore = threading.BoundedSemaphore(value=8)

    for hero_ in url_json:
        # 多线程开始
        threading.Thread(target=getImg, args=(hero_,)).start()    # daemon用来设置线程是否随主线程退出而退出。默认False,

    print("主进程结束了@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")


