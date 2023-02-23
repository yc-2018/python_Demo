# 仰晨
# 始时间：2022/9/6 11:09:04
# 文件名：stu_system

import os
filename = 'student.txt'


def main():
    while True:
        cd()            # 调用菜单
        xz = int(input('请选择相应的功能'))
        if xz in [0, 1, 2, 3, 4, 5, 6, 7]:
            if xz == 0:
                tc = input('确定退出系统吗？（y/n）')
                if tc == 'y' or tc == "Y":
                    print('欢迎下次光临')
                    break
                else:
                    continue

            if xz == 1:
                lr()

            if xz == 2:
                cz()

            if xz == 3:
                sc()

            if xz == 4:
                xg()

            if xz == 5:
                px()

            if xz == 6:
                tj()

            if xz == 7:
                xs()


# 菜单------------------------------------------------------------------------------------
def cd():
    print("""
    =======================学生信息管理系统===================
    -----------------------功能菜单-------------------------
                           1、录入学生信息
                           2、查找学生信息
                           3、删除学生信息
                           4、修改学生信息
                           5、排序
                           6、统计学生总人数
                           7、显示所有学生信息
                           0、退出    
    -------------------------------------------------------                   
    """)


# 录入信息--------------------------------------------------------------------------------
def lr():
    student_list = []
    while True:
        id = input('请输入学生ID（如1001）')
        if not id:
            break
        name = input('请输入姓名')
        if not name:
            break

        try:
            yy = input('请输入英语成绩')          # 原 yy = int(input('请输入英语成绩'))
            py = input('请输入python成绩')
            java = input('请输入Java成绩')

        except:
            print('成绩输入有误，请重新输入（整数）')
            continue
        # 将学生信息保存到字典中
        student = {'id': id, 'name': name, 'yy': yy, 'py': py, 'java': java}
        # 将学生信息添加到列表当中
        student_list.append(student)

        jx = input('是否继续添加（y/n）\n')
        if jx == 'y' or jx == 'Y':
            continue
        else:
            break
    # 保存文件
    save(student_list)
    print('--------学生信息录入成功--------')


def save(lst):      # 保存录入信息---------------
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')

    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()

# 查找-------------------------------------------------------------------------------------
def cz():
    student_cz = []
    while True:
        id = ''
        name = ''
        if os.path.exists(filename):
            mode = input('按ID查找请输入 1  ，按名字查找请输入  2  \n')
            if mode == '1':
                id = input('请输入想要查询的学生ID')
            elif mode == '2':
                name = input('请输入想要查询的学生名字')
            else:
                print('输入有误，请重新输入')
                cz()                            # 重新调用本函数
            with open(filename, 'r', encoding='utf-8') as rfile:
                student = rfile.readlines()
                for item in student:
                    d = dict(eval(item))
                    if id != '':
                        if id == d['id']:
                            student_cz.append(d)
                    elif name != '':
                        if d['name'] == name:
                            student_cz.append(d)
                    # else:
                    #     print('您啥都没输入怎么查...')
                    #     return
            # 显示查询结果
            show_student(student_cz)
            # 清空列表
            student_cz.clear()
            jx = input('是否要继续查询？y/n')
            if jx == 'y' or jx == "Y":
                continue
            else:
                break

        else:
            print('一个学生信息都还没录入呢')
            return


def show_student(lst):
    if len(lst) == 0:
        print('系统无该学生数据')
        return
    # 标题格式
    format_title = "{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}"
    # {:^6}中 数字表示所占宽度 符号^表示居中显示 \t表示添加制表符
    print(format_title.format('ID', '姓名', '英语成绩', 'python成绩', 'Java成绩', '总成绩'))
    # 定义内容显示格式
    format_data = "{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}"
    for item in lst:
        print(format_data.format(item['id'],
                                 item['name'],
                                 item.get('yy'),
                                 item.get('py'),
                                 item.get('java'),
                                 int(item.get('yy'))+int(item['py'])+int(item.get('java'))
                                 ))


# 删除-------------------------------------------------------------------------------------
def sc():
    while True:
        student_id = input('请输入要删除的学生ID\n')
        if student_id != '':
            if os.path.exists(filename):
                # 在 Python 中，exists 函数用于判断输入的路径是否存在，如果存在，不管是文件或者是目录，都返回 True，否则，返回 False。
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False     # 标记是否删除

            if student_old:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for itme in student_old:
                        d = dict(eval(itme))       # 将字符串转为字典     原d = dict(eval(itme))       d = eval(itme)
                                                    # 我们在从键盘输入数据时，Python接收的是字符串类型，这时我们可以使用eval()函数，将输入的数据进行还原
                        if d['id'] != student_id:
                            wfile.write(str(d)+'\n')
                        else:
                            flag = True
                    if flag:
                        print(f'学号为{student_id}的学生信息已删除')
                    else:
                        print('没找到学号为{}的学生信息'.format(student_id))
            else:
                print('无学生数据')
                break
            xs()        # 删除之后要重新显示所有学生信息
            jx = input('是否继续删除？（y/n）\n')
            if jx == 'y' or jx == 'Y':
                continue
            else:
                break


# 修改-------------------------------------------------------------------------------------
def xg():
    xs()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()
    else:
        return

    student_id = input('请输入想要修改的学生的ID')
    with open(filename, 'w', encoding='utf-8') as wfile:
        for itme in student_old:
            d = dict(eval(itme))
            if d['id'] == student_id:
                print('找到学生信息了，可以修改了')
                while True:
                    try:
                        d['name'] = input('请输入名字')
                        d['yy'] = input('请输入英语成绩')
                        d['py'] = input('请输入python成绩')
                        d['java'] = input('请输入java成绩')
                        wfile.write(str(d) + '\n')
                        print('////////////修改成功\\\\\\\\\\\\\\\\')
                    except:
                        print('输入有误请重新输入')
                    else:
                        break
            else:
                wfile.write(str(d) + '\n')
        jx = input('还要改别的学生信息吗 y/n\n')
        if jx == 'y' or jx == 'Y':
            xg()


# 排序------------------------------------------------------------------------------------
def px():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_list = rfile.readlines()
        student_new = []
        for itme in student_list:
            d = dict(eval(itme))
            student_new.append(d)
    else:
        print('无学生信息，无法排序')
        return

    sj_bool = True     # 升降序()优化............
    s_or_j = input('默认降序，降序请按 s \n')
    if s_or_j == 'j':
        sj_bool = False

    mode = input('请选择排序方式：1、按英语成绩排序   2、按python成绩排序     3、按Java成绩排序     其他任意键、按总成绩排序：\n')
    if mode == '1':
        # .sort(key=(排序关键字)，reverse=（升（false（默认））降（true）序）
        student_new.sort(key=lambda x: int(x['yy']), reverse=sj_bool)
    elif mode == '2':
        student_new.sort(key=lambda x: int(x['py']), reverse=sj_bool)
    elif mode == '3':
        student_new.sort(key=lambda x: int(x['java']), reverse=sj_bool)
    else:
        student_new.sort(key=lambda x: int(x['yy'])+int(x['py'])+int(x['java']), reverse=sj_bool)

    show_student(student_new)


# 统计------------------------------------------------------------------------------------
def tj():
    if os.path.exists(filename):
        with open(filename, 'r', encoding="utf-8") as rfile:
            student_list = rfile.readlines()
            if student_list:
                print(f'共有{len(student_list)}名学生')
            else:
                print('学生列表为空')
    else:
        print('暂无学生信息，一条都还没有，快去按1录入吧')


# 显式所有学生信息------------------------------------------------------------------------------------
def xs():
    student_lst = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student = rfile.readlines()
            for itme in student:
                student_lst.append(eval(itme))
            if student_lst:
                show_student(student_lst)
            else:
                print('学生列表为空！！！！！！')
    else:
        print('没有学生数据，快去按1录入吧')


if __name__ == '__main__':
    main()

r"""
-------------------------------------------------------------------------
安装第三方模块
·在线安装方式
            pip install Pylnstaller
·执行打包操作
            pyinstaller -F E:\Pycharm\student管理系统\stusystem.py

-F	打包到一个.exe文件里面
-w	窗口程序打包（tkinter,PyQt等）
-c	控制台程序打包（输入输出）
"""
