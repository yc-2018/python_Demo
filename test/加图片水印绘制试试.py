# By：仰晨
# 文件名：加图片水印试试
# 时 间：2023/5/12 23：09

from PIL import Image


# 打开图片并获取尺寸
a_img = Image.open(r"E:\Users\Dell\Desktop\a.jpg")
a_width, a_height = a_img.size

# 创建一个10*240，颜色为#ddd的新图像 # 直接计算b_img缩放后的高度
b_width, b_height = int(a_height * 0.05/24), int(a_height * 0.05)
b_img_color = (221, 221, 221)
b_img = Image.new("RGB", (b_width, b_height), color=b_img_color)


# 粘贴b_img到a_img右下角
location = (int(a_width * 0.78 - b_img.size[0]), int(a_height * 0.98 - b_img.size[1]))
a_img.paste(im=b_img, box=location)

# 保存合成后的图像
a_img.save(r"E:\Users\Dell\Desktop\result.jpg")
