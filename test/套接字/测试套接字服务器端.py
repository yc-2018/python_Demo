# By：仰晨
# 文件名：测试套接字服务器端
# 时 间：2023/6/29 9:23
import socket

# 创建一个套接字对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定套接字到指定地址和端口
server_address = ('localhost', 5000)
server_socket.bind(server_address)

# 监听连接
server_socket.listen(1)

print('服务器已启动，等待客户端连接...')

# 接受客户端连接
client_socket, client_address = server_socket.accept()
print(f'客户端已连接：{client_address}')

# 接收客户端发送的数据
data = client_socket.recv(1024)
print(f'接收到的数据：{data.decode()}')

# 发送数据到客户端
client_socket.sendall(b'Hello, Client!')

# 关闭套接字
client_socket.close()
server_socket.close()
