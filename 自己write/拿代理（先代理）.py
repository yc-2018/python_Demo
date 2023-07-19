# By：仰晨
# 文件名：哪代理（多）
# 时 间：2023/7/15 16:17
import requests
from bs4 import BeautifulSoup
import time
import socket
import json
import os
import subprocess
from datetime import datetime


# 拿到ip的国家来备注
def get_ip_country(ip):
    url = f"https://www.bejson.com/Bejson/Api/Ip/getIp?ip={ip}"
    headers = {
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Accept': '*/*',
        'Host': 'www.bejson.com',
        'Connection': 'keep-alive'
    }
    response = requests.request("POST", url, headers=headers, proxies={'http': None, 'https': None})
    return response.json()['data']['country']


# 拿到代理信息列表
def get_proxy_info(url):
    pro = {
        'http': "127.0.0.1:2334",
        'https': "127.0.0.1:2334",
    }
    proxies = []
    response = requests.get(url, proxies=pro)
    soup = BeautifulSoup(response.text, 'html.parser')
    trs = soup.find_all('tr')

    # 解析每个代理的信息
    for tr in trs[1:]:
        tds = tr.find_all('td')
        proxy = {
            'ip': tds[0].text,
            'port': tds[1].text,
            'method': tds[2].text,
            'password': tds[3].text,
            'location': tds[4].text,
        }
        proxies.append(proxy)

    print(f"获取代理信息:{proxies}")
    return proxies


# 测试延迟
def test_latency(proxy):
    # 记录当前时间作为开始时间
    start_time = time.time()
    try:
        # 尝试创建一个连接到代理服务器的socket
        # 如果在3秒内无法建立连接，将会抛出一个timeout异常
        sock = socket.create_connection((proxy['ip'], int(proxy['port'])), timeout=3)
        # 连接建立成功，关闭socket
        sock.close()
        # 计算从开始时间到现在所经过的时间，作为延迟
        latency = time.time() - start_time
    except (socket.timeout, ConnectionRefusedError, OSError):
        # 如果在尝试建立连接时出现异常，将延迟设置为无限大
        latency = float('inf')

    # 如果延迟不是无限大（即，能成功连接到代理服务器）
    if latency != float('inf'):
        # 将延迟转换为字符串，保留两位小数
        latency_str = "{:.2f}".format(latency)
        # 在代理的名称中添加日期、代理服务器所在国家和延迟信息
        proxy['name'] = f'{datetime.today().day}号_{get_ip_country(proxy["ip"])}_{latency_str}s'
        print(f"测试代理延迟:{latency}")
        # 返回更新后的代理信息
        return proxy
    else:
        # 如果不能成功连接到代理服务器，返回None
        return None


# 获取全部有效代理
def get_all_valid_proxies(proxies):
    valid_proxies = []

    for proxy in proxies:
        latency_test_result = test_latency(proxy)
        if latency_test_result is not None:
            valid_proxies.append(latency_test_result)

    print(f"获取所有有效代理:{valid_proxies}")
    return valid_proxies


# 更新v2rayN配置文件
def update_v2rayN_config(valid_proxies, config_path):
    # 程序路径
    exe_path = r"D:\green\v2rayN-Core\v2rayN.exe"

    # 使用taskkill命令强制结束程序
    os.system(f"taskkill /IM {os.path.basename(exe_path)} /F")

    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)

    # 修改 guiNConfig.json
    for i, proxy in enumerate(valid_proxies, start=7):
        config['vmess'][i]['address'] = proxy['ip']
        config['vmess'][i]['port'] = int(proxy['port'])
        config['vmess'][i]['id'] = proxy['password']
        config['vmess'][i]['security'] = proxy['method']
        config['vmess'][i]['remarks'] = proxy['name']

    # 将更新后的配置写回文件
    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2)

    # 使用subprocess.Popen()启动程序，不等待其结束
    subprocess.Popen(exe_path)


def main():
    url = "https://ss.weiwei.in/2020.html"
    config_path = r"D:\green\v2rayN-Core\guiNConfig.json"

    proxies = get_proxy_info(url)
    valid_proxies = get_all_valid_proxies(proxies)
    update_v2rayN_config(valid_proxies, config_path)


if __name__ == "__main__":
    main()
