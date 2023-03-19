# By：仰晨
# 文件名：Motrix试试
# 时 间：2023/3/20 1:53

import requests
"""
在 HTTPS 协议下，服务端与客户端之间的通信会进行加密，以确保传输内容的安全性。
但是，如果服务器没有正确配置 SSL 证书或者 SSL 证书过期等问题，就可能会导致 HTTPS 连接失败，从而无法下载该图片
"""
# 设置下载链接和保存路径
url = 'http://www.douyin.com/aweme/v1/play/?video_id=v0200fg10000cg8sbcbc77u82169ebhg&line=0&file_id=c9ad93b76c204bc8af7f4f0d7f0469b9&sign=2ae7e3e08a7f2983256340fa83f99811&is_play_url=1&source=PackSourceEnum_PUBLISH&aid=6383'
filename = "dy.mp4"
save_path = r'E:\Users\Dell\Desktop'

# 构建POST请求数据    token没开好像是可以为空，的看别人js脚本说加就必须要加在第一个 max-connection-per-server可不写  out可以不写
data = {
    'jsonrpc': '2.0',
    'id': '1',
    'method': 'aria2.addUri',
    'params': ['token:OTDbw1UqdUV5', [url], {'dir': save_path, "out": filename, "max-connection-per-server": "16"}]
}

# 发送POST请求  , verify=True 表示开启 SSL 证书验证  没什么乱用   还是下载不了HTTPS协议的图片
response = requests.post('http://localhost:16800/jsonrpc', json=data)

# 输出HTTP响应内容
print(response.json())
