# By：仰晨
# 文件名：带颜色输出
# 时 间：2023/7/15 13:58


"""
首先，安装colorama库。打开命令行，运行：
pip install colorama
"""


from colorama import Fore, Style, init, Back

# 初始化colorama，使其在所有支持的平台上都能使用彩色输出
init()  # pycharm不需要，cmd才要

print(Fore.RED + '你好')
print(Fore.GREEN + '世界')
print(Fore.BLUE + 'ikun')
print('66666666666666666')
print(Style.RESET_ALL)  # 重置颜色到默认设置
print(777)
print(Style.BRIGHT+"你干嘛")
print(Back.GREEN)
print(Fore.BLUE + '哎呦')


input(Fore.RED + '在cmd 不支持 输入前面写')
"""
在上面的例子中，Fore.RED、Fore.GREEN、Fore.BLUE是用来改变字体颜色的，Style.RESET_ALL用来重置颜色到默认设置。

colorama库支持多种颜色，包括：

Fore（前景色）：BLACK（黑色）, RED（红色）, GREEN（绿色）, YELLOW（黄色）, BLUE（蓝色）, MAGENTA（洋红）, CYAN（青色）, WHITE（白色）, RESET（重置）.
Back（背景色）：BLACK（黑色）, RED（红色）, GREEN（绿色）, YELLOW（黄色）, BLUE（蓝色）, MAGENTA（洋红）, CYAN（青色）, WHITE（白色）, RESET（重置）.
Style（样式）：DIM（暗淡）, NORMAL（正常）, BRIGHT（亮色）, RESET_ALL（全部重置）.
"""