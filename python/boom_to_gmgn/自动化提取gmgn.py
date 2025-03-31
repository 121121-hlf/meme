# import requests
import time

from DrissionPage import Chromium

from pymongo import MongoClient
from datetime import datetime
from curl_cffi import requests

# 连接到MongoDB服务器
client = MongoClient('mongodb://localhost:27017/')

# 选择数据库
db = client['boom_db']

# 选择集合
collection = db['boom_walletAddress']

# 查询集合中a字段的内容

# documents = collection.find({}, {'walletAddress': 1, '_id': 0})
# 获取当前日期，格式为年月日
today = datetime.now().strftime('%Y-%m-%d')
tab = Chromium().latest_tab
tab.listen.start(
    f'limit=50&orderby=last_active_timestamp&direction=desc&showsmall=true&sellout=true&tx30d=true')  # 开始监听，指定获取包含该文本的数据包


def parse_percentage_strings(s):
    # 去除百分号并转换为浮点数
    s_list = s.split("\n")
    s = s_list[0]
    value = float(s.strip().replace('%', ''))
    # 将百分比转换为小数形式
    decimal_value = value
    return decimal_value


def get_cookies():
    tab.refresh()
    cookies = tab.cookies()
    cookies_item = {}
    for cookie in cookies:
        cookies_item[cookie['name']] = cookie['value']
    # print(cookies_item)
    return cookies_item


def get_is_show_alert_cont():
    # time.sleep(1)
    res = tab.listen.wait()  # 等待并获取一个数据包
    # print(address, res.url)
    # print(res.response.body)
    data_json = res.response.body
    holdings = data_json["data"]["holdings"]
    is_show_alert_cont = 0
    for holding in holdings:
        if holding["token"]["is_show_alert"]:
            is_show_alert_cont += 1
    # print(is_show_alert_cont)
    return is_show_alert_cont


while True:
    documents = collection.find(
        {'is_gmgn': {'$ne': today}, 'fraud': {'$ne': 1}},
        {'walletAddress': 1, '_id': 0}
    )
    for document in documents:
        # address = "DfMxre4cKmvogbLrPigxmibVTTQDuzjdXojWzjCXXhzj"
        address = document['walletAddress']
        # print(address)
        tab.get(f'https://gmgn.ai/sol/address/{address}')
        tab.ele('@class=css-pt4g3d').click()
        yk_7 = tab.ele('@class=css-1vmazyz').next()
        sl_7 = tab.ele('@class=css-1gqg0yf').next()
        is_show_alert_cont = get_is_show_alert_cont()
        if is_show_alert_cont >= 48:
            print(f"{address} {is_show_alert_cont} 危险代币达到45，标记为诈骗")
            collection.update_one(
                {'walletAddress': address},
                {'$set': {'fraud': 1}}
            )
            continue
        if '--' in yk_7.text or '--' in sl_7.text:
            print(f"{address} 未找到数据，标记为未提币")
            collection.update_one(
                {'walletAddress': address},
                {'$set': {'ys_7_int': 0, 'sl_7_int': 0, 'is_gmgn': today}}
            )
            continue
        ys_7_int = parse_percentage_strings(yk_7.text)
        sl_7_int = parse_percentage_strings(sl_7.text)
        collection.update_one(
            {'walletAddress': address},
            {'$set': {'ys_7_int': ys_7_int, 'sl_7_int': sl_7_int, 'is_gmgn': today}}
        )
        print(address, ys_7_int, sl_7_int)

        # print(parse_percentage_strings(yk_7.text), parse_percentage_strings(sl_7.text))
