# By：仰晨
# 文件名：GetBilibiliHotData
# 时 间：2022/11/21 17:27

import requests
import pandas as pd
import random


def get_data():
    # 创建一个DataFrame数据类型，并写入表头
    xlsx = pd.DataFrame(columns=("排名", "视频名", "分区", "播放量", "时长（秒）", "分辨率", "发布地点", "UP主", "视频链接"))

    url_dict = {"全站综合": "0",  # 全站综合
                "动画": "1",  # 动画
                "音乐": "3",  # 音乐
                "舞蹈": "129",  # 舞蹈
                "游戏": "4",  # 游戏
                "知识": "36",  # 知识
                "科技": "188",  # 科技
                "运动": "234",  # 运动
                "汽车": "223",  # 汽车
                "生活": "160",  # 生活
                "美食": "211",  # 美食
                "动物": "217",  # 动物
                "鬼畜": "119",  # 鬼畜
                "时尚": "155",  # 时尚
                "娱乐": "5",  # 娱乐
                "国创相关": "168",  # 国创相关
                }
    user_agent = [
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
        "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
    ]

    for key in url_dict:
        i = 0
        url = f"https://api.bilibili.com/x/web-interface/ranking/v2?rid={url_dict.get(key)}&type=all"
        headers = {"User-Agent": random.choice(user_agent)}

        json = requests.get(url, headers=headers).json()

        for list_data in json["data"]["list"]:
            视频名 = list_data['title']
            分区 = list_data['tname']
            播放量 = list_data['stat']['view']
            时长 = list_data['duration']
            分辨率 = f"{list_data['dimension']['width']}*{list_data['dimension']['height']}"
            try:
                发布地点 = list_data['pub_location']
            except KeyError:
                发布地点 = ''

            UP主 = list_data['owner']['name']
            视频链接 = list_data['short_link']
            xlsx.loc[i] = [i + 1, 视频名, 分区, 播放量, 时长, 分辨率, 发布地点, UP主, 视频链接]  # 添加行数据
            i += 1
            # print(视频名, 分区, 播放量, 时长, 分辨率, 发布地点, UP主, 视频链接)
        xlsx.to_excel(key + "热榜.xlsx", index=False)  # 不需要索引默认是true 改成false
        print(key + "热榜.xlsx-完成")
    print("全部完成")


if __name__ == '__main__':
    get_data()
