# By：仰晨
# 文件名：5、试试令牌
# 时 间：2023/8/22 14:08
import time
import pyotp
from colorama import Fore, Style, init, Back
import pyperclip
import os

init()  # 初始化颜色


def get_now_otp(key):
    """
    获取当前opt
    :param key: 你的令牌
    :return: 一次性验证码
    """
    return pyotp.TOTP(key).now()  # 返回一个TOTP对象


def otp_expiry_time():
    """
    下一个OTP的开始时间和otp密钥无关。每一个OTP都是基于一个统一的时间间隔生成的，比如每30秒或者每60秒。
    :return: 当前otp结束时间
    """
    now = time.time()  # 获取当前时间的时间戳（以秒为单位）
    interval = 30  # TOTP的默认时间间隔是30秒
    next_otp_start_time = ((int(now / interval) + 1) * interval)  # 计算下一个OTP的开始时间
    return int(next_otp_start_time - now)  # 计算当前OTP的过期时间（即下一个OTP的开始时间）


def main(you_key):
    otp = None
    while True:
        now_otp = get_now_otp(you_key)
        if now_otp == otp:
            print(otp_expiry_time(), end=' ')
        else:
            if otp is not None:
                print()
                os.system('cls')
            otp = get_now_otp(you_key)
            pyperclip.copy(otp)  # 复制到剪贴板
            print(Style.RESET_ALL + "当前 OTP 为" + Fore.GREEN + otp, end=f'{Fore.BLUE} 已复制到剪贴板')
            print(Style.RESET_ALL + Back.YELLOW + f"过期时间为{Style.RESET_ALL + Fore.RED} {otp_expiry_time()}", end=' ')
        time.sleep(1)


if __name__ == '__main__':
    main('GitHub的2FA凭证')
