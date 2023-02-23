# By：仰晨
# 文件名：改计算机名
# 时 间：2023/2/7 1:24

import logging
import os
import time
import wmi
import coloredlogs as coloredlogs

coloredlogs.install(level="INFO", fmt='%(asctime)s [%(levelname)s] %(message)s', level_styles={
    'info': {'color': 'yellow', 'bold': False},
    'warn': {'color': 'red', 'bold': True},
    'error': {'color': 'magenta', 'bold': False}}, isatty=True)


def charge_name():
    logging.info('请输入新的计算机名称')
    newname = input()
    win = wmi.WMI()
    for system in win.Win32_ComputerSystem():
        system.Rename(newname)
    logging.info('已将计算机名称修改为' + newname + '电脑将在2秒后重启')
    time.sleep(2)
    os.system('shutdown -r -t 2')


if __name__ == '__main__':
    charge_name()