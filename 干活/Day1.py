# By：仰晨
# 文件名：Day1
# 时 间：2023/6/20 20:14

def demo1():
    """
    练习:在控制台输入一个变量，再获取一个变量让两个变量交换输出结果
    """
    in1 = input("请输入第一个变量")
    in2 = input("请输入第二个变量")

    item = in1
    in1 = in2
    in2 = item
    del item

    print(f"第一个变量为{in1}")
    print(f"第一个变量为{in2}")
    return print("www")


if __name__ == '__main__':
    print(demo1())

