# 仰晨
# 始时间：2022/8/14 18:54:57
# 文件名：57、文件对象的常用方法

# 方法名                                               说明
# read([size])              从文件中读取size个字节或字符的内容返回。若省略[size]，则读取到文件末尾，即一次读取文件所有内容
# readline()                从文本文件中读取一行内容
# readlines()               把文本文件中每一行都作为独立的字符串对象，并将这些对象放入列表返回
# write(str)                将字符串str内容写入文件
# writelines(s_list)        将字符串列表s_list写入文本文件，不添加换行符
# seek(offset[,whence])     把文件指针移动到新的位置，offset表示相对于whence的位置:
#                           offset:为正往结束方向移动，为负往开始方向移动
#                           whence不同的值代表不同含义:
#                           0:从文件头开始计算（默认值)
#                           1:从当前位置开始计算
#                           2:从文件尾开始计算
# tell()                    返回文件指针的当前位置
# flush()                   把缓冲区的内容写入文件,但不关闭文件                      # 相当于先保存一下
# close()                   把缓冲区的内容写入文件，同时关闭文件，释放文件对象相关资源


file = open('56、文本.txt', 'r', encoding='utf-8')        # 如果文件本来就是GBK格式的话，就不用写, encoding='utf-8'
print(file.read(4))                                     # 写个4，表示只读取4个字符，不写就输出全部内容
file.close()                                            # 关闭文件


file = open('56、文本.txt', 'r', encoding='utf-8')
print(file.readline(3))                                  # 写个3，表示只读取第一行的前3个字符，不写就是整一行
file.close()

file = open('56、文本.txt', 'a', encoding='utf-8')
file.write('国家富强，民族振兴')                             # 把国家富强，民族振兴 写入文本
file.close()

lst = ['和谐', '友善', '敬业', '平等']
file = open('56、文本.txt', 'a', encoding='utf-8')
file.writelines(lst)                                    # 把列表内容 写入文本
file.close()

file = open('56、文本.txt', 'a', encoding='utf-8')
file.write('国家富强，民族振兴\n')                             # 把国家富强，民族振兴 写入文本
file.close()

print('-----------------------------------------')
file = open('56、文本.txt', 'r', encoding='utf-8')
file.seek(3)                                                # utf-8 三个字节一个中文    gbk 2个字节一个中文
print(file.read())
print(file.tell())                                          # 返回指针当前位置
file.close()
































