# By：仰晨
# 文件名：16进制转字符串
# 时 间：2023/4/6 0:12
hex_string = "48656c6c6f20776f726c642120e5938ee591a620e4bda0e5b9b2e5989b"

# 将16进制字符串转换为ASCII字符串
ascii_string = bytes.fromhex(hex_string).decode('utf-8')

print(ascii_string)

# ——————————————————————————————————————————————————————————————————


"""字符串转16进制           转的时候会有0x开头  自行删掉"""
str_value = "Hello world! 哎呦 你干嘛"

# 将字符串编码为字节数组
byte_array = str_value.encode('utf-8')

# 将字节数组转换为16进制字符串
hex_string = hex(int.from_bytes(byte_array, byteorder='big'))

print(hex_string)
