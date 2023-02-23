# 仰晨
# 始时间：2022/8/14 23:05:58
# 文件名：58、with语句

# with语句(上下文管理器)
# with语句可以自动管理上下文资源,不论什么原因跳出with块,都能确保文件正确的关闭，以此来达到释放资源的目的


print(type(open('58、文本.txt', 'r')))         # <class '_io.TextIOWrapper'>，这个类就称之为上下文管理器 open('58、文本.txt', 'r')

with open('58、文本.txt', 'r') as txt:
    print(txt.read())


# with语句 复制图片 试试↓

with open('56、图片.png', 'rb') as png:                    # 打开图片 起个别名叫png
    with open('58、复制的图片.png', 'wb') as fz_png:        # 创建图片 起个别名叫fz_png
        fz_png.write(png.read())                          # 在fz_png里面写入在png中读取的数据






































