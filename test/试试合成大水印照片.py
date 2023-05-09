# By：仰晨
# 文件名：试试合成大水印照片
# 时 间：2023/5/10 2:37

from PIL import Image, ImageDraw, ImageFont
import piexif

# 读取图片和EXIF信息
image_path = r"F:\T图像\新建文件夹\IMG_20201127_144025.jpg"
image = Image.open(image_path)
exif_data = image.info.get("exif")
# 获取原始EXIF数据
data = piexif.load(exif_data)

# 获取图片尺寸
width, height = image.size

# 计算新图片高度
new_height = int(height * 1.1)

# 创建新的白色背景画布
white_canvas = Image.new("RGB", (width, new_height), (255, 255, 255))

# 将原始图片粘贴到新画布上
white_canvas.paste(image, (0, 0))


# 添加文字
def add_text(text, size, x, y, font=r"C:\Windows\Fonts\msyhl.ttc", old_x=False):
    """
    :param text: 要添加的文字
    :param size: 文字大小：按图片高的比例1很小，10和图片水印一样大
    :param x: 文字在水印的位置，0在最左边 10在最右边
    :param old_x: 如果是True 表示传入的值是上次返回的，可以直接用的
    :param y: 文字在水印的位置，0在最上面 10在最下面
    :param font:字体文件路径:默认微软雅黑细体，机型和拍摄参数用微软雅黑粗体
    :return:x的值
    """
    draw = ImageDraw.Draw(white_canvas)
    text = text
    size = int(height * 0.01 * size)
    font = ImageFont.truetype(font, size=size)  # 请确保你有正确的字体文件路径"arial.ttf", size=20
    text_width, text_height = draw.textsize(text, font=font)
    if not old_x:
        x = (width - text_width) * 0.1 * x
    y = height + ((new_height - height) - text_height) * 0.1 * y
    draw.text((x, y), text, fill=(0, 0, 0), font=font)
    return x


# 打开图片并获取EXIF数据
# data = piexif.load(r'F:\T图像\新建文件夹\IMG_20201127_143813.jpg')

# 获取快门速度or曝光时间 [s]
shutter_speed_value = data["Exif"][piexif.ExifIFD.ExposureTime]
shutter_speed = f"1/{round(float(shutter_speed_value[1]) / float(shutter_speed_value[0]))}"
# 获取光圈值
aperture_value = data['Exif'][piexif.ExifIFD.FNumber]
aperture_fstop = aperture_value[0] / aperture_value[1]
aperture = f'f/{aperture_fstop:.2f}'
# 获取 ISO 感光度
iso = "IOS" + str(data["Exif"][piexif.ExifIFD.ISOSpeedRatings])

# 获取拍摄位置
gps_N = data['GPS'][2]
gps_N = f"{gps_N[0][0] / gps_N[0][1]:02.0f}°{int(gps_N[1][0] / gps_N[1][1])}\'{int(gps_N[2][0] / gps_N[2][1])}\"N"
gps_E = data['GPS'][4]
gps_E = f"{gps_E[0][0] / gps_E[0][1]:02.0f}°{int(gps_E[1][0] / gps_E[1][1])}\'{int(gps_E[2][0] / gps_E[2][1])}\"E"

# 机型
x_value = add_text(data["0th"][piexif.ImageIFD.Model].decode('utf-8'), size=2.4, x=0.35, y=2, font=r"C:\Windows\Fonts\msyhbd.ttc")
# 拍摄时间
add_text(data["0th"][piexif.ImageIFD.DateTime].decode('utf-8'), size=1.8, x=x_value, old_x=True, y=6.5)
# 拍摄参数
x_value = add_text(f"{aperture} {shutter_speed} {iso}", size=2.3, x=9.5, y=3, font=r"C:\Windows\Fonts\msyhbd.ttc")
# 拍摄位置
add_text(f"{gps_N} {gps_E}", size=1.8, x=x_value, old_x=True, y=7)

# 保存图片（保留EXIF信息）
white_canvas.save(r"E:\Users\Dell\Desktop\output.jpg", "JPEG", exif=exif_data)
