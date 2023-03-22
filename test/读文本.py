# By：仰晨
# 文件名：读文本
# 时 间：2023/3/22 17:22

import pyttsx3

# 初始化语音引擎
engine = pyttsx3.init()
# 使用语音引擎朗读文本“呆毛hello world”
engine.say("呆毛hello wo rld hello wor ldh e llo worldhello worldhello worldhello world")
# 运行语音引擎，等待文本朗读完成
engine.runAndWait()
