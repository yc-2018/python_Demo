# By：仰晨
# 文件名：9、主动报错
# 时 间：2022/11/9 18:30

try:
    a = int(input("请输入一个1~100的数"))

    if 0 <= a <= 100:
        print("分数为：", a)
    else:
        raise Exception("分数不正确")        # 主动报错

except Exception as c:                      # 捕捉报错内容 起别名为c
    print(c)











