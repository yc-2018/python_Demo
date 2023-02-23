# 仰晨不牛马
# 牛马时间：2022/5/23 22:51:59
print('hello\tnm')  # \t制表符，代表1到4个空格
print('hello\nnm')  # \n换行
print('hello\rnm')  # \r回到本行首位，会覆盖前面的
print('hello\bnm')  # \b是退格

print('http:\\\\www.baidu.com')  # \\=\
print('他说\'我是牛马\'')  # \'='

# 元字符，不要转义字符起作用就在''加r或R   !!!注意最后一个字符不可以是一个反斜杠（ 比如print(r'我是牛马\')#可以是两个\\）
print(r'他说\n我是牛马\t')
