# By：仰晨
# 文件名：翻译chat
# 时 间：2023/3/19 2:57


import requests

url = 'https://api.mymemory.translated.net/get'


def translate_text(text, target_language):
    params = {
        'q': text,
        'langpair': f'en|{target_language}'
    }
    response = requests.get(url, params=params)
    return response.json()['responseData']['translatedText']


"""
常见的ISO 639-1代码：
英语：en        中文：zh
西班牙语：es     法语：fr
阿拉伯语：ar     俄语：ru
德语：de        日语：ja
韩语：ko        意大利语：it
"""
text = 'you'
target_language = 'zh'          # 翻译为中文
translation = translate_text(text, target_language)
print(translation)
