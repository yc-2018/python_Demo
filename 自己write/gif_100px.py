# By：仰晨
# 文件名：gif_100px
# 时 间：2023/4/29 15:12
# 描 述：把一个指定的文件夹下面的gif格式的图片批量修改其宽度为100像素（高度等比例调整），并输出到指定文件夹下

from PIL import Image
import os


def resize_gif(input_path, output_path, new_width):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    for filename in os.listdir(input_path):
        if filename.endswith('.gif'):
            image = Image.open(os.path.join(input_path, filename))
            frames = []
            try:
                while True:
                    frames.append(image.copy())
                    image.seek(image.tell() + 1)
            except EOFError:
                pass
            new_height = int(frames[0].height * (new_width / frames[0].width))
            frames = [frame.resize((new_width, new_height), Image.Resampling.LANCZOS) for frame in frames]
            frames[0].save(os.path.join(output_path, filename.replace(".gif", "_new.gif")), save_all=True, append_images=frames[1:])
            print(f'完成{filename}...')


resize_gif(r'E:\Users\Dell\Desktop\新建文件夹', r'E:\Users\Dell\Desktop\new表情包', 100)
