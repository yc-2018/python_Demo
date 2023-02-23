# 仰晨
# 始时间：2022/8/22 16:31:58
# 文件名：改步数
# 小米运动的
import requests
数据 = {'user': '13421767752', 'pass': 'aa12345678', 'step': '66779'}
网址 = 'http://apk.52dun.cn/'
结果 = requests.post(网址, 数据)
print(结果.text)







































