# By：仰晨
# 文件名：8、for和枚举
# 时 间：2022/11/9 17:21

lst = ["鸡", "你", "太", "美"]

print("原列表", lst)
for index, value in enumerate(lst):
    print(index, value)


# 枚举就是让可迭代序列加个序号，从0开始
"""
运行结果：
原列表 ['鸡', '你', '太', '美']
0 鸡
1 你
2 太
3 美
"""












