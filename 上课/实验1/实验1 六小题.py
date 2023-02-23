# By：仰晨
# 文件名：实验1 六小题
# 时 间：2022/10/29 23:01

import pymysql

config = {"host": "127.0.0.1",  # 主机名
          "user": "root",  # 数据库用户名
          "password": "123456",  # 数据库密码
          "port": 3306,  # 端口号  数字不用加双引号
          'database': 'python_data',  # 数据库 库名字  python_data
          'charset': 'utf8'  # 编码
          }

# 连接数据库

连接 = pymysql.connect(**config)  # 连接数据库  **表示可变长参数
游标 = 连接.cursor()  # 在连接基础上通过cursor方法获取游标


def 小题一():  # 查询status为'PROCESSING','PENDING_ORDER_CONFIRM','NO_PENDING_ACTION'
    游标.execute("SELECT * FROM `order` where status in ('PROCESSING','PENDING_ORDER_CONFIRM','NO_PENDING_ACTION')")


def 小题二():  # 查询status不为'PROCESSING','PENDING_ORDER_CONFIRM','NO_PENDING_ACTION','PENDING_TECHNICIAN_NOTIFICATION'
    游标.execute(
        "SELECT * FROM `order` where status not in ("
        "'PROCESSING','PENDING_ORDER_CONFIRM','NO_PENDING_ACTION','PENDING_TECHNICIAN_NOTIFICATION')")


def 小题三():  # 查询total_amount>200的订单数据
    游标.execute("SELECT * FROM `order` WHERE total_amount > 200")


def 小题四():  # 查询total_amount 200 ~ 500 的订单数据
    游标.execute("SELECT * FROM `order` WHERE total_amount BETWEEN 200 and 500")


def 小题五():  # 以user_id为维度，查询每个用户的tatal_amount总金额并排序
    # 设置sql模式
    # 游标.execute("set sql_mode ='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';")
    # 老师方法↓
    游标.execute("select user_id, sum(total_amount) from `order` group by user_id order by sum(total_amount) desc")


def 小题六():  # 以user_id为维度，查询tatal_amount总订单量在3一下的用户ID列表
    # 游标.execute("SELECT user_id, count(total_amount) as count_total_amount FROM `order` GROUP BY total_amount HAVING count_total_amount < 3")
    游标.execute("select user_id, count(total_amount) from `order` group by user_id order by count(total_amount)<3 desc")


if __name__ == '__main__':
    # 小题一()

    # 小题二()

    # 小题三()

    # 小题四()

    小题五()

    # 小题六()

    for i in 游标.fetchall():
        print(i)
