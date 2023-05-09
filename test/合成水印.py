# By：仰晨
# 文件名：合成水印
# 时 间：2023/5/10 1:48
from PIL import Image, ImageDraw, ImageFont
import piexif

# 读取图片和EXIF信息
image_path = r"F:\T图像\IMG_20191115_152223.jpg"
image = Image.open(image_path)
exif_data = image.info.get("exif")

# 获取图片尺寸
width, height = image.size

# 计算新图片高度
new_height = int(height * 1.1)

# 创建新的白色背景画布
white_canvas = Image.new("RGB", (width, new_height), (255, 255, 255))

# 将原始图片粘贴到新画布上
white_canvas.paste(image, (0, 0))

# 添加文字
draw = ImageDraw.Draw(white_canvas)
text = "哎呦 你干嘛居中"
font = ImageFont.truetype(r"C:\Windows\Fonts\simhei.ttf", size=int(height*0.05))  # 请确保你有正确的字体文件路径"arial.ttf", size=20
print(int(height*0.05))
text_width, text_height = draw.textsize(text, font=font)
x = (width - text_width) // 2
y = height + (new_height - height - text_height) // 2
draw.text((x, y), text, fill=(0, 0, 0), font=font)

# 保存图片（保留EXIF信息）
white_canvas.save(r"E:\Users\Dell\Desktop\output.jpg", "JPEG", exif=exif_data)



