# By：仰晨
# 文件名：不需要缓存声音
# 时 间：2023/3/12 16:09
"""
python-sounddevice3，它可以播放WAV文件，但是需要用soundfile模块来读取文件数据。
你可以先用requests模块来获取声音链接的内容，并且把它保存到一个BytesIO对象中，然后用soundfile模块来读取这个对象，
并且用sounddevice模块来播放数据。你也可以用一个循环来重复播放3次，比如：
"""
from io import BytesIO
import sounddevice as sd
import soundfile as sf
import requests


response = requests.get('https://fanyi.baidu.com/gettts?lan=en&text=python&spd=3&source=web')
data = BytesIO(response.content)
for i in range(3):
    data.seek(0)        # 将指针重置为数据的开头
    samples, fs = sf.read(data, dtype='float32')
    sd.play(samples, fs)
    status = sd.wait()  # 等到文件播放完毕
input()
