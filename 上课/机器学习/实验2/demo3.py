# By：仰晨
# 文件名：demo3
# 时 间：2023/3/30 0:38

from PIL import Image, ImageEnhance

# 打开图像文件
img = Image.open("image.jpg")
en = ImageEnhance.Brightness(img).enhance(2)
en.show()



