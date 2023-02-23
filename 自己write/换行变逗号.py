import pyperclip

'''
print('粘贴在这，点2次确定就已经在剪贴板了')
he = ''
while True:
    电话 = input()
    if 电话 == '':
        break
    he = he + 电话 + ','

he = he[:-1]
print(he, end='')
pyperclip.copy(he)
'''
电话 = input('\t\t\t\tby:仰晨----不可思意\n请粘贴电话号码:\n')
nb = 电话.isdecimal()
end = ''
if nb:
    count = len(电话)
    print('总长：', count, '号码个数', count/11)
    t = 0
    w = 11
    while w <= count:
        var = 电话[t:w]
        end = end + var + ','
        # print(var, end=',')
        t = t + 11
        w = w + 11

    print(end[:-1], '\n数据已复制到剪贴板')
    pyperclip.copy(end[:-1])

else:
    print('--------------------------')
    print('!!!包涵非数字字符请检查!!!')
    print('--------------------------')

input('\n回车键结束')