# By：仰晨
# 文件名：4、GithubTOTP
# 时 间：2023/8/22 12:23
import time
import pyotp
# print('当前令牌为:', pyotp.TOTP('VP46GTHEM7JFRBZZ').now())


# 生成一个密钥（base32 编码）
secret_key = 'VP46GTHEM7JFRBZZ'


# 使用密钥和时间间隔（默认为 30 秒）创建一个 TOTP 对象
totp = pyotp.TOTP(secret_key)

# 生成当前的 OTP
current_otp = totp.now()
print(f"当前 OTP: {current_otp}")

# 验证 OTP（为演示目的，我们使用刚生成的 OTP）
is_valid = totp.verify(current_otp)
print(f"OTP 是否有效？ {is_valid}")

# 为了演示 OTP 有效性窗口，等待下一个时间间隔
time.sleep(31)

# 再次尝试验证 OTP（由于时间窗口已过，应该无效）
is_valid = totp.verify(current_otp)
print(f"OTP 仍然有效吗？ {is_valid}")