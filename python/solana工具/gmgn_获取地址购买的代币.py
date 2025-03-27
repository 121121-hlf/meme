# import requests
import time

from DrissionPage import Chromium
import requests

address = "DNfuF1L62WWyW3pNakVkyGGFzVVhj4Yr52jSmdTyeBHm"
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "priority": "u=1, i",
    "referer": f"https://gmgn.ai/sol/address/{address}",
    "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Google Chrome\";v=\"134\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"134.0.6998.167\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"134.0.6998.167\", \"Not:A-Brand\";v=\"24.0.0.0\", \"Google Chrome\";v=\"134.0.6998.167\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "\"\"",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
}

tab = Chromium().latest_tab
tab.listen.start(
    f'api/v1/wallet_holdings/sol/{address}')  # 开始监听，指定获取包含该文本的数据包

tab.get(f"https://gmgn.ai/sol/address/{address}")
res = tab.listen.wait()  # 等待并获取一个数据包
data_json = res.response.body
holdings = data_json["data"]["holdings"]
for holding in holdings:
    token_address = holding["token"]["token_address"]

    if holding["buy_30d"] == 0:
        # print("buy_30d is 0, skip", token_address)
        continue
    start_holding_at = holding["start_holding_at"] - 8 * 60 * 60
    print("token_address:", token_address, "start_holding_at:", start_holding_at)
    start_time = start_holding_at - 60*5
    end_time = start_holding_at
    print("start_time:", start_time, "end_time:", end_time)
#     转为  年月日时分秒 格式
    start_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time))
    end_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time))
    print("start_time_str:", start_time_str, "end_time_str:", end_time_str)
