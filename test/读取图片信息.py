# By：仰晨
# 文件名：读取图片信息
# 时 间：2023/5/9 22:41

import piexif

# 打开图片并获取EXIF数据
data = piexif.load(r'F:\T图像\新建文件夹\IMG_20201127_143813.jpg')

# 获取所有键值对
for key in data:
    print(key, data[key])
    print("----------------------")

print('————————————————————————————————————————————————————————————')

print("机型："+data["0th"][piexif.ImageIFD.Model].decode('utf-8'))
print("拍摄时间："+data["0th"][piexif.ImageIFD.DateTime].decode('utf-8'))

# 获取快门速度or曝光时间 [s]
shutter_speed_value = data["Exif"][piexif.ExifIFD.ExposureTime]
shutter_speed = f"1/{round(float(shutter_speed_value[1])/float(shutter_speed_value[0]))}"
# 获取光圈值
aperture_value = data['Exif'][piexif.ExifIFD.FNumber]
aperture_fstop = aperture_value[0] / aperture_value[1]
aperture = f'f/{aperture_fstop:.2f}'
# 获取 ISO 感光度
iso = "IOS"+str(data["Exif"][piexif.ExifIFD.ISOSpeedRatings])

# 输出拍摄信息
print(f"光圈值、快门速度、感光度:{aperture} {shutter_speed} {iso}")
gps_N = data['GPS'][2]
print(f"{gps_N[0][0]/gps_N[0][1]:02.0f}°{int(gps_N[1][0]/gps_N[1][1])}\'{int(gps_N[2][0]/gps_N[2][1])}\"N")
gps_N = data['GPS'][4]
print(f"{gps_N[0][0]/gps_N[0][1]:02.0f}°{int(gps_N[1][0]/gps_N[1][1])}\'{int(gps_N[2][0]/gps_N[2][1])}\"E")
"""
piexif.load('example.jpg')读取的是图像的EXIF元数据信息，其中包含了很多键值对。以下是一些常见键的含义：

- '0th': 图像文件本身的属性。

  - piexif.ImageIFD.Make: 相机制造商
  - piexif.ImageIFD.Model: 相机型号
  - piexif.ImageIFD.XResolution: 水平分辨率
  - piexif.ImageIFD.YResolution: 垂直分辨率
  - piexif.ImageIFD.ResolutionUnit: 分辨率单位（1=无单位，2=英寸，3=厘米）

- 'Exif': 存储拍摄参数、相机设置等信息。

  - piexif.ExifIFD.ExposureTime: 曝光时间
  - piexif.ExifIFD.ISOSpeedRatings: ISO感光度
  - piexif.ExifIFD.FNumber: 光圈大小
  - piexif.ExifIFD.DateTimeOriginal: 拍摄时间
  - piexif.ExifIFD.FocalLength: 焦距

- 'GPS': 存储全球定位系统（GPS）信息。

  - piexif.GPSIFD.GPSLatitudeRef: 纬度（N/S）
  - piexif.GPSIFD.GPSLatitude: 纬度数值
  - piexif.GPSIFD.GPSLongitudeRef: 经度（E/W）
  - piexif.GPSIFD.GPSLongitude: 经度数值
  - piexif.GPSIFD.GPSAltitudeRef: 海拔高度参考（0=海平面，1=海拔）
  - piexif.GPSIFD.GPSAltitude: 海拔高度数值

- 'Interop'键是EXIF的一个子集，用于存储数据与照片之间的互通性信息，以便在不同设备和软件之间共享和查看照片时能够正确解释照片格式和属性等信息。它包含了一些标签，例如相机制造商、相机型号、ISO感光度、曝光时间等，与0TH中的一些字段信息类似。
    在这个样例中，由于 'Interop' 键为空字典，则说明此照片的EXIF元数据没有相机设备的互通信息，也就是相机厂商或者拍摄设备并未填写该标签信息。如果使用不同的设备去读取，或许会有些键存在，并且会包含一些具体的信息。

- '1st': 缩略图。

  - piexif.ImageIFD.JPEGInterchangeFormat: JPEG数据起始位置
  - piexif.ImageIFD.JPEGInterchangeFormatLength: JPEG数据大小

以上是一些常见的键值对含义，不同的照片由于保存信息的不同版本和摄影设备不同而会有所不同。
======================================================================================"""


"""====================================================================================
0th {256: 4624, 272: b'Redmi Note 8 Pro', 257: 3472, 274: 6, 306: b'2021:03:25 20:41:29', 34665: 154, 34853: 3172, 271: b'Xiaomi'}解释这些键
这些键值对包含了照片的基本属性和一些信息，以下是它们的含义解释：
    - 256: 所拍摄的图像的宽度。
    - 257: 所拍摄的图像的高度。
    - 271: 设备制造商名称，此处为'Xiaomi'。
    - 272: 设备型号，此处为'Redmi Note 8 Pro'。
    - 274: 每个组件的位深度，通常为8、10、12或16。在这里，它表示每个颜色通道的位深度为6位。所以总共有2^6=64个不同亮度等级来表示每个颜色通道。
    - 306: 拍摄日期和时间，格式为'YYYY:MM:DD HH:MM:SS'
    - 34665: 用于存储用于图像处理或压缩的相关设置等信息
    - 34853: 拍摄大小，即图像文件的大小，以字节为单位。
需要注意的是，不同厂商的设备可能会使用不同的标签来存储相同的信息，所以具体的键值对定义和解释可能会有一定的差异。


Exif {33437: (189, 100), 37386: (543, 100), 33434: (60002000, 1000000000), 37385: 0, 34855: 5162, 40963: 2600, 40962: 4624, 37378: (184, 100), 37377: (-405, 100), 37520: b'177'}键的意思
这些键值对包含了照片的拍摄参数和一些信息，以下是它们的含义解释：
    - 33437: 光圈值，即F值。在这里，它表示光圈大小为f/1.89。光圈值 = 分数值 = 分子 / 分母
    - 33434: 快门速度（秒）。在这里，它表示快门速度为1/2000秒。快门速度 = 分数倒数 = 分母 / 分子即 1/（60002000/1000000000） ≈ 0.00002 ≈ 1/2000 seconds)，也就是说，在拍摄这张照片时，相机的快门保持开放了2000分之一秒（或者是 1/2000 秒）。
    - 37377: 红色色彩平衡系数（RB），通常用于颜色校正。
    - 37378: 绿色色彩平衡系数（GR）。
    - 37385: 闪光灯被触发的状态。在这里，它表示未使用闪光灯。
    - 37386: 焦距（毫米）。在这里，它表示焦距为5.43mm。
    - 34855: ISO感光度，即摄像机传感器的灵敏度。
    - 40962: 图像高度（以像素为单位），与0TH中的高度值相同。
    - 40963: 图像宽度（以像素为单位），与0TH中的宽度值相同。
    - 37520: 地理位置信息。在这里，它是一个包含经纬度坐标和海拔高度的字节数组。
需要注意的是，不同品牌、型号、版本的照相机，可存储的 EXIF 标签可能会有差异。因此，相机制造商的存储习惯和名称也会不一样。因此，这里列出的并非是所有可能存在的 EXIF 标签和解释，而是常见的标签和样例含义。


GPS {1: b'N', 2: ((23, 1), (10, 1), (331, 100)), 3: b'E', 4: ((113, 1), (22, 1), (2409, 100)), 7: ((12, 1), (46, 1), (21, 1)), 29: b'2019:09:27'}键的意思
这些键值对包含了照片的GPS信息，以下是它们的含义解释：
    - 1: 纬度参考（N/S），此处为北半球（N）。
    - 2: 纬度数值，以元组格式存储。在这里，纬度为23度10分33.1秒（23, 10, 331/100），即23.175861°。
    - 3: 经度参考（E/W），此处为东经（E）。
    - 4: 经度数值，以元组格式存储。在这里，经度为113度22分24.09秒（113, 22, 2409/100），即113.373358°。
    - 7: 海拔高度，以元组格式存储。在这里，海拔高度为12.7725米。
    - 29: GPS日期和时间信息，格式为'YYYY:MM:DD'。
需要注意的是并非所有的图片都包含GPS信息。如果图片中没有该信息，则代码将会报错。
"""
