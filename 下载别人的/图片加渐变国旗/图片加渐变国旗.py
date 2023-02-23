import math

import numpy as np
from PIL import Image       # PIL安装失败是因为python版本不对，python3 使用pip install pillow
# 把原图放在相同的文件夹 并把名字改成  photo.jpeg

def generate_flag_photo():
    # 国旗路径
    flag_img_path = "./flag.jpg"
    # 头像路径
    photo_img_path = "./photo.jpeg"
    # 载入国旗图片
    flag_img = Image.open(flag_img_path)
    # 载入头像图片
    photo_img = Image.open(photo_img_path)
    # 国旗图片的宽和高
    flag_width, flag_height = flag_img.size
    # 头像的宽和高
    photo_width, photo_height = photo_img.size
    # 如果国旗图片的大小大于头像的大小， 就将国旗进行缩小
    if photo_width < flag_width:
        # flag_img = cv2.resize(flag_img, (photo_width, flag_height * photo_width / flag_width))
        flag_img = flag_img.resize((photo_width, int(flag_height * photo_width / flag_width)), Image.ANTIALIAS)
        flag_width, flag_height = flag_img.size
    if photo_height < flag_height:
        # flag_img = cv2.resize(flag_img, (flag_width * photo_height / flag_height, photo_height))
        flag_img = flag_img.resize((int(flag_width * photo_height / flag_height), photo_height), Image.ANTIALIAS)
        flag_width, flag_height = flag_img.size
    # 如果国旗的尺寸太小了，就将国旗进行放大
    if flag_width * 2 < photo_width:
        # flag_img = cv2.resize(flag_img, (flag_width * 2, flag_height * 2))
        flag_img = flag_img.resize((flag_width * 2, flag_height * 2), Image.ANTIALIAS)
        flag_width, flag_height = flag_img.size
    # 现在进行融合
    flag_min = min(flag_width, flag_height)
    flag_img = np.array(flag_img)
    photo_img = np.array(photo_img)
    for i in range(photo_width):
        for j in range(photo_height):
            distance = int(math.sqrt(i * i + j * j))
            if distance > flag_min:
                # 如果超出国旗的大小了，就只是用头像像素
                alpha = 1
            else:
                alpha = distance / flag_min
            if i < flag_min and j < flag_min:
                for k in range(3):
                    #
                    photo_img[i][j][k] = int(alpha * photo_img[i][j][k] + (1 - alpha) * flag_img[i][j][k])
    Image.fromarray(photo_img).save("res.jpeg")


if __name__ == '__main__':
    generate_flag_photo()
