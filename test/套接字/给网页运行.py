# By：仰晨
# 文件名：给网页运行
# 时 间：2023/6/29 11:48
import socket

def main():
    # 创建一个TCP套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 设置套接字选项，以便在程序关闭后立即释放端口
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 绑定套接字到地址和端口
    server_address = ('', 8080)
    server_socket.bind(server_address)

    # 开始监听连接
    server_socket.listen(1)
    print("Server is running on http://localhost:8080")

    while True:
        # 接受客户端连接
        client_socket, client_address = server_socket.accept()

        # 定义一个简单的HTML网页内容
        html_content = """
        <!DOCTYPE html>
        <html>
            <head>
                <title>My Simple Web Page</title>
            </head>
            <body>
                <h1>Hello, World!</h1>
                <p>Welcome to my simple web page.</p>
            </body>
        </html>
        """

        # 准备HTTP响应头和响应体
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: {len(html_content)}\r\n\r\n{html_content}"

        # 向客户端发送HTTP响应
        client_socket.sendall(response.encode())

        # 关闭客户端连接
        client_socket.close()

if __name__ == "__main__":
    main()