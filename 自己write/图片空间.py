# By：仰晨
# 文件名：图片空间
# 时 间：2023/4/6 12:59  //+4.8...
import os
import os.path as op


def little_zip_to_img(image, rar, new_file_name):
    # 将参数1的图片和参数2的压缩包的内容合并，并输出到新图片文件中
    with open(image, "rb") as file1, open(rar, "rb") as file2, open(new_file_name, "wb") as file3:
        file3.write(file1.read() + file2.read())
    """
        适合小文件，大文件可能会卡，
        因为是按字节来读取的 会一直读到完，就会占用高内存
        100m要2秒左右
        
        下面的100m基本不用一秒    其实下面的方法也是通用的但是 上面的方法它简单呀
    """


def big_zip_to_img(image, rar, new_file_name):
    # 定义缓冲区大小为 4096 字节
    buffer_size = 4096

    # 打开文件1，读取内容
    with open(image, "rb") as image:
        # 打开文件2，读取内容
        with open(rar, "rb") as rar:
            # 将文件1和文件2的内容合并，并输出到文件3中
            with open(new_file_name, "wb") as new_file_name:
                # 循环读取图片的缓冲区数据并写入文件3
                data = image.read(buffer_size)
                while data:
                    new_file_name.write(data)
                    data = image.read(buffer_size)

                # 循环读取压缩包的缓冲区数据并写入文件3
                data = rar.read(buffer_size)
                while data:
                    new_file_name.write(data)
                    data = rar.read(buffer_size)


def lst(ls, r=True):
    try:
        if r:
            i = 1
            for item in ls:
                print(f"{i}、{item}")
                i += 1
        return ls[int(input("请输入你想选择的文件序号")) - 1]
    except IndexError:
        print("序号乱写是不行滴 重新选择吧")
        lst(ls, False)


def newName(image, rar):
    name = input("请输入新文件名（直接回车就用默认名字）")
    if name:
        return name + op.splitext(image)[1]
    else:
        return op.splitext(image)[0] + op.splitext(rar)[1] + op.splitext(image)[1]


if __name__ == '__main__':
    # 定义需要筛选的图片格式
    img_s = (".png", ".jpg", ".gif", "jpeg", "jfif")
    # 定义需要筛选的压缩包格式
    pack_s = (".zip", ".rar", ".7z", "tar", "gzip")

    while True:
        # 指定目录路径
        path = input("请输入工作路径（直接回车默认当前路径）")
        if path:
            if op.isdir(path):
                os.chdir(path)  # 将这个目录设置为当前工作目录
                break
            else:
                print("没找到该文件夹，请重新输入")
        else:
            path = "./"
            break

    # 遍历目录下所有文件，筛选出 .图片 文件
    img_files = [f for f in os.listdir(path) if op.isfile(op.join(path, f)) and f.lower().endswith(img_s)]
    # print(img_files)

    if img_files:
        # 遍历目录下所有文件，筛选出 .压缩包 文件
        pack_files = [f for f in os.listdir(path) if op.isfile(op.join(path, f)) and f.lower().endswith(pack_s)]
        # print(pack_files)
        if pack_files:
            img = lst(img_files)
            pack = lst(pack_files)
            if (op.getsize(img) + op.getsize(pack)) < 1024 ** 2 * 20:
                print("小文件")
                little_zip_to_img(img, pack, newName(img, pack))
            else:
                print("大文件")
                big_zip_to_img(img, pack, newName(img, pack))
            print("-----------success--------------")
        else:
            print('该文件夹没有压缩包文件（".zip", ".rar", ".7z", "tar", "gzip"）')
    else:
        print('该文件夹没有图片文件（".png", ".jpg", ".gif", "jpeg" jfif）')
