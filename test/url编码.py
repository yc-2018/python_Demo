# By：仰晨
# 文件名：url编码
# 时 间：2023/7/15 13:34

from urllib.parse import quote_plus

s = "1+1-2\r\n666\n你干嘛"
encoded_s = quote_plus(s)

print(encoded_s)  # 输出: 1%2B1-2

