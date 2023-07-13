# By：仰晨
# 文件名：翻译chat
# 时 间：2023/3/19 2:57


import requests

# 使用网络出海会报错所以要明确代理用不用，如果不用就写None
proxies = {
    'http': "127.0.0.1:2334",
    'https': "127.0.0.1:2334",
}

url = 'https://api.mymemory.translated.net/get'


def translate_text(text, target_language):
    params = {
        'q': text,
        'langpair': f'en|{target_language}'
    }
    response = requests.get(url, params=params, proxies=proxies)
    return response.json()['responseData']['translatedText']


"""
常见的ISO 639-1代码：
英语：en        中文：zh
西班牙语：es     法语：fr
阿拉伯语：ar     俄语：ru
德语：de        日语：ja
韩语：ko        意大利语：it
"""
text = 'you is pig'
target_language = 'zh'          # 翻译为中文
translation = translate_text(text, target_language)
print(translation)
