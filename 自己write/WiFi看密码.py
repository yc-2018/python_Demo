# By：仰晨
# 文件名：WiFi看密码
# 时 间：2023/4/9 5:40
import subprocess
import re
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
        password = None

    print("▓ "+f'{wifi.ljust(18, " ")}▓  {password}'.ljust(40, " ")+"▓")
input("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 回车退出▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\n公众号：仰晨")


