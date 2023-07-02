# By：仰晨
# 文件名：接收广播
# 时 间：2023/7/2 15:55


import socket  # 导入 socket 模块，用于创建和操作网络套接字


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建一个新的 UDP 套接字
    # 设置 socket 选项 SO_BROADCAST 为 1，以便接收广播数据包
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    server_address = ('', 8888)  # 定义服务器地址，使用空字符串表示监听所有网络接口，端口为 8888
    server_socket.bind(server_address)  # 将套接字绑定到指定的服务器地址

    print("Server is ready to receive broadcast messages...")

    try:
        while True:  # 无限循环
            data, addr = server_socket.recvfrom(1024)  # 从套接字接收最多 1024 字节的数据包，并获取发送方的地址
            # 打印来自发送方的广播数据和地址
            print(f"Received broadcast from {addr}: {data.decode()}")
    except KeyboardInterrupt:  # 当按下 Ctrl+C 时，捕获 KeyboardInterrupt 异常
        print("Shutting down server...")  # 输出关闭服务器的消息
    finally:  # 无论是否发生异常，都将执行以下代码块
        server_socket.close()  # 关闭套接字


if __name__ == "__main__":
    main()
