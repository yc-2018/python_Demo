# By：仰晨
# 文件名：拿代理
# 时 间：2023/6/19 9:39
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
    """
    从指定URL获取代理信息
    :param url: 代理信息网页的URL
    :return: 代理信息列表
    """
    proxies = []
    response = requests.get(url, proxies={'http': None, 'https': None})
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
            "name": f'{datetime.today().day}号_{get_ip_country(tds[0].text)}'
        }
        proxies.append(proxy)

    print(f"获取代理信息:{proxies}")
    return proxies


def test_latency(proxy):
    """
    测试给定代理的延迟
    :param proxy: 代理信息字典
    :return: 延迟时间（以秒为单位）
    """
    start_time = time.time()
    try:
        sock = socket.create_connection((proxy['ip'], int(proxy['port'])), timeout=3)
        sock.close()
        latency = time.time() - start_time
    except (socket.timeout, ConnectionRefusedError, OSError):
        latency = float('inf')

    print(f"测试代理延迟:{latency}")
    return latency


# 获取延迟最低的代理
def get_best_proxy(proxies):
    """
    从给定的代理列表中找出延迟最低的代理
    :param proxies: 代理信息列表
    :return: 延迟最低的代理信息字典
    """
    best_latency = float('inf')
    best_proxy = None

    for proxy in proxies:
        latency = test_latency(proxy)
        if latency < best_latency:
            best_latency = latency
            best_proxy = proxy

    print(f"获取延迟最低的代理:{best_proxy}")
    return best_proxy


# 更新v2rayN配置文件
def update_v2rayN_config(best_proxy, config_path):
    """
    使用给定的最佳代理信息更新v2rayN配置文件
    :param best_proxy: 延迟最低的代理信息字典
    :param config_path: v2rayN配置文件路径
    """
    # 程序路径
    exe_path = r"D:\green\v2rayN-Core\v2rayN.exe"

    # 使用taskkill命令强制结束程序
    os.system(f"taskkill /IM {os.path.basename(exe_path)} /F")

    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)

    # 修改 guiNConfig.json
    config['vmess'][4]['address'] = best_proxy['ip']
    config['vmess'][4]['port'] = int(best_proxy['port'])
    config['vmess'][4]['id'] = best_proxy['password']
    config['vmess'][4]['security'] = best_proxy['method']
    config['vmess'][4]['remarks'] = best_proxy['name']

    # 将更新后的配置写回文件
    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2)

    # 如有必要，重启v2rayN
    # os.system(r"D:\green\v2rayN-Core\v2rayN.exe")
    # 使用subprocess.Popen()启动程序，不等待其结束
    subprocess.Popen(exe_path)


def main():
    url = "https://4.weiwei.in/2020.html"
    config_path = r"D:\green\v2rayN-Core\guiNConfig.json"

    proxies = get_proxy_info(url)
    best_proxy = get_best_proxy(proxies)
    update_v2rayN_config(best_proxy, config_path)


if __name__ == "__main__":
    main()
