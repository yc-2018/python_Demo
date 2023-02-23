# By：仰晨
# 文件名：将 gif 转换成字符动态图
# 时 间：2022/12/14 2:07

from PIL import Image

# 打开 gif 图片
im = Image.open("13.gif")

# 获取图片宽度和高度
width, height = im.size
print(im.size)

# 设置字符集，可以自定义
chars = " .,-~:;=!*#$@"

# 将 gif 转换成字符动态图
for t in range(im.n_frames):
    # 设置当前帧
    im.seek(t)

    # 将当前帧转换成灰度图
    frame = im.convert("L")

    # 打印字符动态图
    for y in range(height):
        for x in range(width):
            # 获取像素值
            pixel = frame.getpixel((x, y))

            # 计算对应的字符
            index = int(pixel / 256 * len(chars))
            char = chars[index]

            # 打印字符
            print(char, end="")
        print()
    print()














