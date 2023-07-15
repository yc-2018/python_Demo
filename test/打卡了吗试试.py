# By：仰晨
# 文件名：打卡了吗试试
# 时 间：2023/7/10 20:15

import requests

from datetime import datetime
from colorama import Fore, Style, init

# 初始化colorama，使其在所有支持的平台上都能使用彩色输出
init(convert=True)

current_date = datetime.now().strftime('%Y-%m-%d')  # 当天时间

def getDK(_id):
    import json
    url = r"http://tx.17tongx.com/web/dataset/call_kw/tx.hr.attendance.daily/web_search_read"

    payload = json.dumps({
        "id": 12,
        "jsonrpc": "2.0",
        "method": "call",
        "params": {
            "model": "tx.hr.attendance.daily",
            "method": "web_search_read",
            "args": [],
            "kwargs": {
                "limit": 80,
                "offset": 0,
                "order": "",
                "context": {
                    "lang": "zh_CN",
                    "tz": "Asia/Shanghai",
                    "uid": 25,
                    "allowed_company_ids": [
                        1
                    ],
                    "bin_size": True,
                    "params": {
                        "action": 955,
                        "model": "tx.hr.attendance.daily",
                        "view_type": "list",
                        "menu_id": 104,
                        "cids": 1
                    }
                },
                "count_limit": 10001,
                "domain": [
                    "&",
                    [
                        "date",
                        "=",
                        current_date  # 当天时间
                    ],
                    [
                        "pin",
                        "ilike",
                        _id  # 工号搜索
                    ]
                ],
                "fields": [
                    "pin",
                    "employee_id",
                    "department_id",
                    "employee_job_id",
                    "attendance_time",
                    "normal_overtime_hours",
                    "holiday_overtime_hours",
                    "date",
                    "punch_in_morning",
                    "clock_out_morning",
                    "punch_in_afternoon",
                    "clock_out_afternoon",
                    "punch_in_evening",
                    "clock_out_evening",
                    "late_leave_early"
                ]
            }
        }
    })
    headers = {
        'Cookie': 'session_id=0c5d10baed2669a7805e9daacf2208c8fb4df17a',
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Host': 'tx.17tongx.com',
        'Connection': 'keep-alive'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    # 试试拿请求头
    # headers = response.headers
    # for key, value in headers.items():
    #     print(f"{key}:{value}")

    json = response.json()
    try:
        print(f"{json['result']['records'][0]['employee_id'][1]}")
        print(f"{json['result']['records'][0]['date']}")
        print(f"早上签入{json['result']['records'][0]['punch_in_morning']}")
        print(f"早上签出{json['result']['records'][0]['clock_out_morning']}")
        print(f"中午签入{json['result']['records'][0]['punch_in_afternoon']}")
        print(f"中午签出{json['result']['records'][0]['clock_out_afternoon']}")
        print(f"晚上签入{json['result']['records'][0]['punch_in_evening']}")
        print(f"晚上签出{json['result']['records'][0]['clock_out_evening']}")
        # print(f"晚上签出{json['result']['records'][0]}")
    except IndexError:
        print(Fore.RED + '还没打卡或工号不存在', end="")
        print(Style.RESET_ALL)  # 重置颜色到默认设置
        # print(f"{json}")


getDK(19)

while True:
    _id = input('====================ikun几号====================')   # 重置颜色到默认设置
    if not _id:
        break
    getDK(_id)

