# 仰晨不牛马
# 牛马时间：2022/6/12 01:31:57

for _ in range(3):
    mima = int(input('输入密码'))
    if mima == 556:
        print('密码正确')
        break
    else:
        print('密码错误')
else:  # 这个是和for并列的，当没有执行break的时候就会执行，while语句也是一样
    print('密码3次错误')
