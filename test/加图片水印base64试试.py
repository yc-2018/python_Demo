# By：仰晨
# 文件名：加图片水印试试
# 时 间：2023/5/12 22:44

from PIL import Image
import base64
from io import BytesIO

# 打开图片并获取尺寸
a_img = Image.open(r"E:\Users\Dell\Desktop\a.jpg")
# 不用写   data:image/png;base64,
b_img_data = b'iVBORw0KGgoAAAANSUhEUgAAAAsAAADxCAIAAACSx9oOAAAACXBIWXMAABJ0AAASdAHeZh94AAAAEXRFWHRTb2Z0d2FyZQBTbmlwYXN0ZV0Xzt0AAAA4SURBVGiB7coxAQAACMMwwL/FecEBN0f6Np2kzubeBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEE8EAsogwR5EJ9JuQAAAABJRU5ErkJggg=='  # 使用base64编码后的图片数据
b_img = Image.open(BytesIO(base64.b64decode(b_img_data)))
a_width, a_height = a_img.size
b_width, b_height = b_img.size

# 计算b_img缩放后的高度
new_b_height = int(a_height * 0.05)

# 调整b_img大小
b_img = b_img.resize((int(b_width * new_b_height / b_height), new_b_height))

# 粘贴b_img到a_img右下角
location = (int(a_width * 0.78 - b_img.size[0]), int(a_height * 0.98 - b_img.size[1]))
a_img.paste(im=b_img, box=location)

# 保存合成后的图像
a_img.save(r"E:\Users\Dell\Desktop\result.jpg")
