import time

import requests


def get_solscan_data(user_address, token_address, start_time, end_time):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "origin": "https://solscan.io",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://solscan.io/",
        "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Google Chrome\";v=\"134\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        # "sol-aut": "MgHRZPP-5ZuTE7=B9dls0fKMBx7e4re3sNXnT6HF",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
    }
    cookies = {
        "_ga": "GA1.1.1030425754.1729572772",
        "cf_clearance": "ZEXKlIXxwDdjVDpJAWKThzfKFszqtlC8kgdjNSu1yNo-1743067109-1.2.1.1-daKcyxACxWmIPCtSnB_rW7zSqA1w5J_fRrkB_FFDqCZV8SINKldzWzJbytgvSOL4quV_yzdWfDfTLkhPns6H4q4a675FNqSzj1Szbxz.Sqnq_zHQ4r.qbDywLMC7j0kqj6RBM_lEuS3rlYeWJxQ9zqelic2wZELz5vnI6NlorAY1uSTBADOOGiDsZUaPMKa72TTiMV_fe9aUf_I0uLvwfo06UUjeIfmx99nHJvYssq7ZaQDR7khi5rfRr8xk5kqqcFCq7eY3PHleh.FahSaZ95s_wzd3TJiFJZxOwYzvnEXIK80MlJHqaK.DCOxmq1XW4WjDZf2lQbTt3SfOSOLMUb_1HB.1D_UDxz4Hn1mh6VY",
        "_ga_PS3V7B7KV0": "GS1.1.1743065435.364.1.1743067302.0.0.0"
    }
    # address = "DNfuF1L62WWyW3pNakVkyGGFzVVhj4Yr52jSmdTyeBHm"
    address_list = []

    # response = requests.get(url, headers=headers, cookies=cookies, params=params)
    cont = 1
    index = 0
    while 1:
        url = "https://api-v2.solscan.io/v2/token/activity/dextrading"
        params = {
            "address": f"{token_address}",
            "page": cont,
            "page_size": "100",
            "from_time": f"{start_time}",
            "to_time": f"{end_time}"
        }
        print(f"第{cont}次请求", )
        response = requests.get(url, headers=headers, params=params)
        # response = requests.get(url, headers=headers, cookies=cookies, params=params)
        print(response.status_code)
        data_json = response.json()
        data_list = data_json["data"]
        # print(data_json)
        if len(data_list) == 0:
            print("数据已全部获取")
            break
        for data in data_list:
            try:
                amount_info = data["amount_info"]
                token1 = amount_info["token1"]
                # token2 = amount_info["token2"]
                if "So1111" in token1:
                    from_address = data["from_address"]
                    address_list.append(from_address)
            except Exception as e:
                print(e)
                print("数据格式错误",data)
                continue
        cont += 1
        time.sleep(4)
        # break
    # print(address_list)
    for i, value in enumerate(address_list):
        if value == user_address:
            print("第{}次请求，第{}条数据为目标地址".format(cont, index))
            index = i
            break

    ok_address_list = address_list[index:]
    # 将ok_address_list去重
    ok_address_list = list(set(ok_address_list))
    # print(f"{token_address} 交易地址列表去重：{ok_address_list}")
    return ok_address_list
