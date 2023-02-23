# By：仰晨
# 文件名：实验1 多条件数据库读写操作
# 时 间：2022/10/29 15:44

# 导入库
import pymysql
import pandas as pd

# 定义数据库连接信息

config = {"host": "127.0.0.1",          # 主机名
          "user": "root",               # 数据库用户名
          "password": "123456",         # 数据库密码
          "port": 3306,                 # 端口号  数字不用加双引号
          'database': 'python_data',    # 数据库 库名字  python_data
          'charset': 'utf8'             # 编码
          }

# 连接数据库
try:
    连接 = pymysql.connect(**config)          # 连接数据库  **表示可变长参数
    游标 = 连接.cursor()                       # 在连接基础上通过cursor方法获取游标

# 创建再连接数据库
except pymysql.err.OperationalError:
    连接 = pymysql.connect(host="127.0.0.1", user='root', password="123456")
    游标 = 连接.cursor()
    游标.execute("CREATE DATABASE python_data")       # 游标。执行（创建  数据库   python_data）


# 显示该数据库有多少个表
print(游标.execute("show tables"))

# 获取数据
表对象 = 游标.fetchall()         # 返回多个元组，如果没有结果 则返回 ()
print('表的多元组', 表对象)

# 用列表生成式把表对象转换为列表
表列表 = [元组[0] for 元组 in 表对象]
print("表的列表", 表列表)

# 看看又没有叫order的表
if 'order' not in 表列表:
    # 创建表order
    游标.execute('''
        CREATE TABLE `order` (	
        id INT ( 11 ) AUTO_INCREMENT PRIMARY KEY,	# 定义主键
        user_id INT ( 11 ),	
        total_amount DOUBLE ( 16, 7 ),
        status VARCHAR (50) ,
        order_data TIMESTAMP
        )
        ''')

# 读取xlsx文件数据
xlsx_data = pd.read_excel("order.xlsx", sheet_name=0)       # , sheet_name=0可不写，报黄有点不自然

# 开始写入数据库
for 键, 值 in enumerate(xlsx_data.values):
    写入数据库 = "INSERT INTO `order` ( `user_id`, `total_amount`, `status`, `order_data` )"\
               "values (  %d,%f,'%s','%s' )" % (值[2], 值[3], 值[1], 值[0])

    游标.execute(写入数据库)       # 执行数据库命令 写入
    连接.commit()                #

# 关闭游标和连接   关闭后就无法对数据库再进行操作了
# 游标.close()
# 连接.close()




