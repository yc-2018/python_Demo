import re
import requests
import json

headers = {
    "accept":
    "*/*",
    "accept-encoding":
    "identity;q=1, *;q=0",
    "accept-language":
    "zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7,zh-TW;q=0.6,de;q=0.5,fr;q=0.4,ca;q=0.3,ga;q=0.2",
    "range":
    "bytes=0-",
    "sec-fetch-dest":
    "video",
    "sec-fetch-mode":
    "no-cors",
    "sec-fetch-site":
    "cross-sit",
    "user-agent":
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}


def http_get(url):
    resp = requests.get(url, headers=headers, timeout=20)
    return resp


def get_item_id(short_url):
    res = http_get(short_url)
    item_id = re.findall(r"(?<=video/)\d+", res.url)[0]
    print(item_id)
    return item_id


def get_play_url(item_id):
    api_url = "https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=" + item_id
    api = http_get(api_url).text 
    api = json.loads(api)
    playwm = api['item_list'][0]['video']['play_addr']['url_list'][0]
    play = playwm.replace('/playwm/', '/play/') 
    return play


def fetch(short_url):
    item_id = get_item_id(short_url)
    return get_play_url(item_id)


url = fetch("https://v.douyin.com/jWqQXB5/")
print(url)