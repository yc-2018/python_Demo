# By：仰晨
# 文件名：测试套接字客户端
# 时 间：2023/6/29 9:24
import socket

# 创建一个套接字对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接到服务器
server_address = ('localhost', 5000)
client_socket.connect(server_address)

# 向服务器发送数据
client_socket.sendall(b'Hello, Server!')

# 接收服务器发送的数据
data = client_socket.recv(1024)
print(f'接收到的数据：{data.decode()}')

# 关闭套接字
client_socket.close()
