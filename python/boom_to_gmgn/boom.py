import random
import time

from curl_cffi import requests
# import requests
from pymongo import MongoClient
impersonates = [
    # Edge
    "edge99",
    "edge101",
    # Chrome
    "chrome99",
    "chrome100",
    "chrome101",
    "chrome104",
    "chrome107",
    "chrome110",
    "chrome116",
    "chrome119",
    "chrome120",
    "chrome123",
    "chrome124",
    "chrome99_android",
    # Safari
    "safari15_3",
    "safari15_5",
    "safari17_0",
    "safari17_2_ios",
    # alias
    "chrome",
    "edge",
    "safari",
    "safari_ios",
    "chrome_android",
]
# MongoDB连接设置
client = MongoClient('mongodb://localhost:27017/')
db = client['boom_db']  # 替换为你的数据库名
collection = db['boom_walletAddress']  # 替换为你的集合名
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "origin": "https://boom.meme",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Google Chrome\";v=\"134\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
}
# url = "https://api.boom.meme/signal/list"
url = "https://api.boom.meme/sol/signal/list"
while True:
    impersonate = random.choice(impersonates)
    print(f"正在使用 {impersonate}")
    response = requests.get(url, headers=headers, impersonate=impersonate, )
    # response = requests.get(url, headers=headers)
    print(response.status_code)
    data_json = response.json()
    data_list = data_json["data"]
    address_list = set()
    for data in data_list:
        # print(data)
        swapLogs = data["swapLogs"]
        for swapLog in swapLogs:
            walletAddress = swapLog["walletAddress"]
            # 将钱包地址插入到MongoDB中
            result = collection.update_one(
                {"walletAddress": walletAddress},  # 查询条件
                {"$setOnInsert": {"walletAddress": walletAddress}},  # 只在插入时设置
                upsert=True  # 如果不存在则插入
            )
            if result.upserted_id:
                print(f"钱包地址 {walletAddress} 成功插入")
            else:
                pass
                # print(f"钱包地址 {walletAddress} 已存在，未插入")
    time.sleep(100)
