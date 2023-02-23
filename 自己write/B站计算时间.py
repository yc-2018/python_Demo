# By：仰晨
# 文件名：B站计算时间
# 时 间：2022/10/27 2:20
# 优 化：2022/11/23 *：** 加上百分比**进度条**用字符串.ljust()对齐代替\t**用f"字符串｛｝"代替一些字符串.format()**单个视频给出温馨提示
# 待 优：鬼畜视频集合只显示一个视频的问题，想法：判断  链接['data']["pages"]==1  就换为  链接['data']['ugc_season']['sections'][0]['episodes']  循环拿i['page']['duration'] 2022.11.23 解决
import math
import requests
import re


# B站获取到的时间是一个整数，这个整数是秒数  所以要转换为 时分秒
def 单位转换(原全秒):
    分钟 = math.floor(原全秒 / 60)
    秒 = 原全秒 % 60
    if 分钟 > 60:
        小时 = math.floor(分钟 / 60)
        分钟 = 分钟 % 60
        return f"{小时}小数{分钟}分钟{秒}秒"
    else:
        return f"{分钟}分钟{秒}秒"


def 剩下时间(索引, flag=False, 方式=1):
    剩下总时间 = 0
    while 索引 <= 列表索引:
        if 方式 == 1:
            剩下总时间 += 链接['data']["pages"][索引]["duration"]
        else:
            剩下总时间 += 链接['data']['ugc_season']['sections'][0]['episodes'][索引]['page']['duration']
        索引 += 1
    if flag:
        return 剩下总时间
    else:
        return 单位转换(剩下总时间)


if __name__ == '__main__':
    浏览器标识 = {"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                           'Chrome/98.0.4758.139 Safari/537.36'}
    reg = "(?<=={\"aid\":)[0-9]*"
    方式 = 1  # 正常教程列表默认1  牛马链接改2

    while True:
        输入链接 = input('请输入链接')
        if "www.bilibili.com/video/" in 输入链接:
            try:
                B站 = requests.get(输入链接).text
                ree = re.findall(reg, B站)  # 拿到json链接的列表
                链接 = requests.get('https://api.bilibili.com/x/web-interface/view?aid={}'.format(ree[0]), 浏览器标识).json()
                视频列表 = 链接['data']["pages"]

                if len(视频列表) == 1:
                    视频列表 = 链接['data']['ugc_season']['sections'][0]['episodes']
                    列表索引 = len(视频列表) - 1
                    方式 = 2
                    if len(视频列表) == 1:
                        print("\033[3;32;43m本程序主要用来用来算视频集合的进度，比如一个教程有100个视频，你看到52个，看后面的还有多长时间要看，单个视频用本程序没有什么意义\033[0m")

                    总时长 = 0
                    for time in 视频列表:
                        总时长 += time['page']['duration']

                else:
                    列表索引 = len(视频列表) - 1
                    总时长 = 链接['data']["duration"]

                print('总时长为', 单位转换(总时长))
                print("░" * 100)
                集 = 1

                for i in 视频列表:
                    剩下秒 = 剩下时间(集, True, 方式) / 总时长 * 100
                    if 方式 == 1:
                        转换时间 = 单位转换(i['duration'])
                    else:
                        转换时间 = 单位转换(i['page']['duration'])
                    print(f"第{str(集).zfill(3)}集 时间为{转换时间}".ljust(22) + f"剩下时长为：{剩下时间(集, flag=False, 方式=方式)}",
                          end=f"\t还有{round(剩下秒, 2)}%未看\n")
                    print(("░" * int(剩下秒)).rjust(100, "▓"))
                    集 += 1

            except Exception as e:
                print('失败了，如果不是链接有问题，那就是有其他问题:', e)
            finally:
                break

        else:
            print("""print('\033[1;31m 输入的链接有误，正确链接如下\033[0m')
                     \033[1;36mhttps://www.bilibili.com/video/\033[0mBV15G4y1Z7q1/
                  """)

    # 打包就要加，不然加载完就会自动关闭窗口
    input('回车关闭窗口')
