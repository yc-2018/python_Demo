# By：仰晨
# 文件名：图片空间
# 时 间：2023/4/6 12:59


def little_zip_to_img(img, rar, new_file_name=None):
    """
    适合小文件，大文件可能会卡，
    因为是按字节来读取的 会一直读到完，就会占用高内存
    """
    if not new_file_name:
        new_file_name = "new_image.rar.jpg"
    # 将参数1的图片和参数2的压缩包的内容合并，并输出到新图片文件中
    with open(img, "rb") as file1, open(rar, "rb") as file2, open(new_file_name, "wb") as file3:
        file3.write(file1.read() + file2.read())


def big_zip_to_img(img, rar, new_file_name=None):
    if not new_file_name:
        new_file_name = "new_image.rar.jpg"

    # 定义缓冲区大小为 4096 字节
    buffer_size = 4096

    # 打开文件1，读取内容
    with open(img, "rb") as img:
        # 打开文件2，读取内容
        with open(rar, "rb") as rar:
            # 将文件1和文件2的内容合并，并输出到文件3中
            with open(new_file_name, "wb") as new_file_name:
                # 循环读取图片的缓冲区数据并写入文件3
                data = img.read(buffer_size)
                while data:
                    new_file_name.write(data)
                    data = img.read(buffer_size)

                # 循环读取压缩包的缓冲区数据并写入文件3
                data = rar.read(buffer_size)
                while data:
                    new_file_name.write(data)
                    data = rar.read(buffer_size)


little_zip_to_img(r"E:\Users\Dell\Desktop\1.jpeg", r'E:\Users\Dell\Desktop\Desktop.rar', r'E:\Users\Dell\Desktop\new1.rar.jpg')
big_zip_to_img(r"E:\Users\Dell\Desktop\1.jpeg", r'E:\Users\Dell\Desktop\Desktop.rar', r'E:\Users\Dell\Desktop\new2.rar.jpg')


