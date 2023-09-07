# By：仰晨
# 文件名：5、图片gps转经纬度
# 时 间：2023/9/7 19:16

# 解析exif数据
gps_ifd = {1: b'N', 2: ((23, 1), (9, 1), (5994, 100)), 3: b'E', 4: ((113, 1), (17, 1), (3269, 100)),
           7: ((6, 1), (17, 1), (11, 1)), 29: b'2020:11:27'}

lat_ref = gps_ifd.get(1)  # 纬度参考,N或S
lat = gps_ifd.get(2)  # 纬度

lon_ref = gps_ifd.get(3)  # 经度参考,E或W
lon = gps_ifd.get(4)  # 经度


def conv_to_degress(value):
    """将经纬度的值转换为度"""
    d = float(value[0][0]) / float(value[0][1])
    m = float(value[1][0]) / float(value[1][1])
    s = float(value[2][0]) / float(value[2][1])
    return d + (m / 60.0) + (s / 3600.0)


lat = conv_to_degress(lat)
lon = conv_to_degress(lon)

print(f"Latitude: {lat_ref}{lat}")
print(f"Longitude: {lon_ref}{lon}")
print(f"Longitude: {lon}")
