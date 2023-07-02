# By：仰晨
# 文件名：demo
# 时 间：2023/6/29 11:20
import socket


def main():
    # 创建一个TCP套接字
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接到服务器
    server_address = ('example.com', 80)
    client_socket.connect(server_address)

    try:
        # 准备一个简单的HTTP GET请求（使用中文路径）
        request = "GET /中文路径 HTTP/1.1\r\nHost: example.com\r\nConnection: close\r\n\r\n"
        client_socket.sendall(request.encode())

        # 接收响应
        response = b''
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            response += data

        # 打印响应
        print(response.decode(errors='replace'))
    finally:
        # 关闭套接字
        client_socket.close()


if __name__ == "__main__":
    main()
