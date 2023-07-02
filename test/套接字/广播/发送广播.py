# By：仰晨
# 文件名：发送广播
# 时 间：2023/7/2 15:56
import socket


def main():
    # 创建一个UDP套接字
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 设置套接字选项SO_BROADCAST为1，以启用广播功能
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # 定义广播地址和端口
    broadcast_address = ('255.255.255.255', 8888)

    # 要发送的消息
    message = "Hello, 这个是广播信息!"

    try:
        # 向广播地址发送消息
        client_socket.sendto(message.encode(), broadcast_address)
        print("Broadcast message sent.")
    except Exception as e:
        print(f"Error sending broadcast: {e}")
    finally:
        # 关闭套接字
        client_socket.close()


if __name__ == "__main__":
    main()
