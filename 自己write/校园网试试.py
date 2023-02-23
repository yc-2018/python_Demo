import requests
import socket


# 获取ip地址
def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('11.255.255.255', 1))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


user_ip = get_host_ip()

# 校园网地址，最好不要用浏览器里的url，还是建议抓包获取
post_addr = "http://192.168.150.88/eportal/logout.jsp?ms2g="

# 下面两个大括号里面都是复制自己学校校园网登录网站中的，冒号两边都要加上双引号
post_header = {
    # 报头信息，通过抓包，获取
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'keep-alive',
    'Cookie': 'EPORTAL_COOKIE_SERVER=; EPORTAL_COOKIE_DOMAIN=; EPORTAL_COOKIE_SAVEPASSWORD=true; EPORTAL_COOKIE_OPERATORPWD=; EPORTAL_COOKIE_USERNAME=202210001182; EPORTAL_COOKIE_PASSWORD=1976e9ed07850f522d9ebd11de9ba9f5e648bacb8aaaf88810ad02acc2d1a11f4533bc868dc364a1c7b9f8ea568ff222dd00ff74814c59b31e756936feb00abea0590fb56646cb5acc3267ce658d8bc109740df11e9484cfc906b1acea545c5743fb6c8b6d3e36ebd5fe877aaa02ccd00df447c142b818e12c24c58782964b5c; EPORTAL_AUTO_LAND=; EPORTAL_USER_GROUP=dianxin; EPORTAL_COOKIE_SERVER_NAME=%E8%AF%B7%E9%80%89%E6%8B%A9%E6%9C%8D%E5%8A%A1; JSESSIONID=BBCC5A3DF15E74559035B8E30A151D32',
    'Host': '192.168.150.88',
    'Referer': 'http://192.168.150.88/eportal/index.jsp?wlanuserip=950a5c64c6db3f2fe18b2c2d2e418ef8&wlanacname=2ad511bc0b2c8c7ca5314a8851326ae5&ssid=&nasip=316f7af94e7a54679137dbc5812e82d1&snmpagentip=&mac=2c1aa19f244fb470a0bf958f04c0719c&t=wireless-v2&url=2c0328164651e2b4f13b933ddf36628bea622dedcc302b30&apmac=&nasid=2ad511bc0b2c8c7ca5314a8851326ae5&vid=5d41ee85b431af01&port=25ca6b42ad223b70&nasportid=f5eb983692924fa26e6431fe9df4835fb172adc9690db3a4d0351e679ebf897448370f72e052a330',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.139 Safari/537.36'
}

post_data = {
    # 正文数据，通过抓包获取
    'userIndex': '33313666376166393465376135343637393133376462633538313265383264315f31302e33342e3133312e3231325f323032323130303031313832',
    'keepaliveInterval': '0'
}
# 提交http请求报文
z = requests.post(post_addr, data=post_data, headers=post_header)

print("登录校园网成功，局域网ip如下：")
print(user_ip)
# input("")