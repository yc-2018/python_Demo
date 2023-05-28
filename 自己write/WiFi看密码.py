# By：仰晨
# 文件名：WiFi看密码
# 时 间：2023/4/9 5:40
import subprocess
import re


def cn(str1):
    """面向win10 CMD->有中文会导致不能对齐 有一个中文就减少一个对齐的量
    :param str1: WiFi名字或密码"""
    count = 0
    for char in str1:
        if '\u4e00' <= char <= '\u9fff':
            count += 1
    return count


output = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True).stdout.decode('gbk')
# print(output)
wifis = [wifi.strip() for wifi in re.findall(r'所有用户配置文件\s*:\s*(.+)', output)]
# print(wifis)

print("▓▓▓▓ wifi名▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 密码▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
for wifi in wifis:
    results = subprocess.run(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear'], capture_output=True).stdout.decode('gbk', errors='ignore').split('\\n')
    # print(results)
    password = re.search(r'关键内容\s*:\s*(.+)', str(results))
    if password:
        password = password.group(1).strip().split("\\r\\n\\r\\n")[0]
    else:
        password = ' '

    print("▓ "+f'{wifi.ljust(18-cn(wifi), " ")}▓  {password}'.ljust(40-cn(wifi), " ")+"▓")
input("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 回车退出▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\n公众号：仰晨")


