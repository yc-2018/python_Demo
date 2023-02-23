# 欲仰清晨却已星辰（懒）
# 始时间：2022/7/19 17:39:21
# 文件名：字符串编码和解码
# import select

字符串ss = "鲁莽比懦弱更接近勇敢"

# 编码
print(字符串ss.encode(encoding='GBK'))         # 在GBK编码中一个中文占2个字节      b'\xc2\xb3\xc3\xa7\xb1\xc8\xc5\xb3\xc8\xf5\xb8\xfc\xbd\xd3\xbd\xfc\xd3\xc2\xb8\xd2'
print(字符串ss.encode(encoding='UTF-8'))       # 在utf-8中，一个中文占3个字节      b'\xe9\xb2\x81\xe8\x8e\xbd\xe6\xaf\x94\xe6\x87\xa6\xe5\xbc\xb1\xe6\x9b\xb4\xe6\x8e\xa5\xe8\xbf\x91\xe5\x8b\x87\xe6\x95\xa2'


# 解码
# byte代表一个二进制数据（字节类型的数据）
byte = 字符串ss.encode(encoding='GBK')
print(byte.decode(encoding='gbk'))          # 鲁莽比懦弱更接近勇敢

bbbb = 字符串ss.encode(encoding='UTF-8')
print(bbbb.decode(encoding='utf-8'))        # 鲁莽比懦弱更接近勇敢

print(b'\xc2\xb3\xc3\xa7\xb1\xc8\xc5\xb3\xc8\xf5\xb8\xfc\xbd\xd3\xbd\xfc\xd3\xc2\xb8\xd2'.decode(encoding='gbk'))       # 鲁莽比懦弱更接近勇敢

print('仰晨'.encode(encoding='gbk'))


# 结束时间 ： 2022.7.19  18：02