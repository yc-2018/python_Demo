# By：仰晨
# 文件名：常用属性
# 时 间：2023/7/2 16:08


import socket


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建一个 IPv4 的 TCP 套接字
    server_socket.bind(('0.0.0.0', 5000))  # 绑定服务器地址和端口
    server_socket.listen(1)  # 监听客户端连接，允许的最大连接数为 1

    print("服务器正在等待客户端连接...")

    connection, client_address = server_socket.accept()  # 当有客户端连接时，返回新的套接字和客户端地址
    print(f"客户端 {client_address} 已连接。")

    # 获取并显示套接字信息
    print(f"套接字类型（sockfd.type）: {connection.type}")
    print(f"套接字地址类型（sockfd.family）: {connection.family}")
    print(f"套接字绑定地址（sockfd.getsockname()）: {connection.getsockname()}")
    print(f"套接字文件描述符（sockfd.fileno()）: {connection.fileno()}")
    print(f"连接套接字客户端地址（sockfd.getpeername()）: {connection.getpeername()}")

    # 设置并获取套接字选项值
    connection.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)  # 打开 TCP keepalive
    keepalive_value = connection.getsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE)  # 获取 TCP keepalive 选项值
    print(f"套接字选项值（sockfd.getsockopt(level, option)）: SO_KEEPALIVE = {keepalive_value}")

    connection.close()  # 关闭连接套接字
    server_socket.close()  # 关闭服务器套接字


if __name__ == "__main__":
    main()
