# By：仰晨
# 文件名：调用下载
# 时 间：2022/12/5 1:55

import os
import time
from pyaria2 import Aria2RPC


def get_file_from_url(link, file_name):
    jsonrpc = Aria2RPC()

    options = {"dir": r"E:\\Users\\Dell\\Desktop", "out": file_name, }
    res = jsonrpc.addUri([link], options=options)


def get_file_from_cmd(link):
    exe_path = r'D:\panMotrix\Motrix.exe'
    order = exe_path + ' -s16 -x10 ' + link
    os.system(order)


if __name__ == '__main__':
    link = 'https://pngimg.com/uploads/acorn/small/acorn_PNG37022.png'
    filename = '海阔天空.png'
    start = time.time()
    get_file_from_cmd(link)
    get_file_from_url(link, filename)

    end = time.time()
    print(f"耗时:{end - start:.2f}")
