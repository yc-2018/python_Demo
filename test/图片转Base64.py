# By：仰晨
# 文件名：图片转Base64
# 时 间：2023/3/19 3:08

import base64

with open(input('请输入图片全路径'), "rb") as image_file:
    print(f'data:image/jpeg;base64,{str(base64.b64encode(image_file.read()))[2:-1]}')
    """
    不同格式头要换
    data:image/gif;base64,
    data:image/x-icon;base64,
    data:image/jpeg;base64,
    data:image/bmp;base64
    data:image/png;base64,
    """
