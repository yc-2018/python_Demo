# By：仰晨
# 文件名：正则判断
# 时 间：2023/3/19 23:50
import re


# 判断字符串是否包含英文字母
def has_alpha(string):
    pattern = r'[a-zA-Z]'
    match = re.search(pattern, string)
    print(f'——————{match}————————')
    return bool(match)


# 测试
print(has_alpha('Hello, World!'))   # True
print(has_alpha('12345'))           # False
print(has_alpha('中文字符串abc'))     # True
print(has_alpha(''))                # False
print(bool(re.search(r'[a-zA-Z]', "试试")))
