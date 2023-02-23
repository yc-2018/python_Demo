# 仰晨不牛马
# 牛马时间：2022/5/24 16:13:19

import keyword

print(keyword.kwlist)  # 查看关键字

name = '牛马不是一般的牛和马'
print(name)
print('标识', id(name))
print('类型', type(name))
print('值', name)  # 值：value

name = '新的牛马，会指向新的内存空间，旧的地址就会变成内存垃圾，'
print('标识', id(name))
print('值', name)
