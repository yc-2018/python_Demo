import pymysql
from pymysql import err
import pandas as pd

host = '127.0.0.1'
user = 'root'
password = '123456'
port = 3306
database = 'python_data'
charset = 'utf8'


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    config = {
        'host': host,
        'user': user,
        'password': password,
        'database': database,
        'charset': charset
    }
    try:
        # ** 的作用则是把字典 config 变成关键字参数传递。
        cnn = pymysql.connect(**config)
        cursor = cnn.cursor()
    except err.OperationalError:  # 捕获数据库不存在异常
        # 如果数据库不存在就创建
        cnn = pymysql.connect(host=host, user=user, password=password)
        cursor = cnn.cursor()
        cursor.execute("CREATE DATABASE " + database)
    # 显示数据库里面的所有表
    cursor.execute("show tables")
    # 获取数据
    table_object = cursor.fetchall()
    # 拿到所以表的名字存起来
    table_list = [t[0] for t in table_object]
    # 判断表存不存在
    if 'order' not in table_list:
        # 不存在就创建
        cursor.execute('''
        CREATE TABLE `order` (	
        id INT ( 11 ) AUTO_INCREMENT PRIMARY KEY,	
        user_id INT ( 11 ),	
        total_amount DOUBLE ( 16, 7 ),
        status VARCHAR (50) ,
        order_data TIMESTAMP
        )
        ''')
    # 数据源文件的名字
    data_file = 'order.xlsx'
    # 读取数据
    data = pd.read_excel(data_file, sheet_name=0)
    # 循环数据
    for key, value in enumerate(data.values):
        # 写sql
        insert_sql = "INSERT INTO `order` ( `user_id`, `total_amount`, `status`, `order_data` ) " \
                     "values (  %d,%f,'%s','%s' )" % (value[2], value[3], value[1], value[0])
        # 写到数据库
        cursor.execute(insert_sql)
        # 事物提交
        cnn.commit()
