import time

import requests


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
    "sol-aut": "MgHRZPP-5ZuTE7=B9dls0fKMBx7e4re3sNXnT6HF",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
}
cookies = {
    "_ga": "GA1.1.1030425754.1729572772",
    "cf_clearance": "ZEXKlIXxwDdjVDpJAWKThzfKFszqtlC8kgdjNSu1yNo-1743067109-1.2.1.1-daKcyxACxWmIPCtSnB_rW7zSqA1w5J_fRrkB_FFDqCZV8SINKldzWzJbytgvSOL4quV_yzdWfDfTLkhPns6H4q4a675FNqSzj1Szbxz.Sqnq_zHQ4r.qbDywLMC7j0kqj6RBM_lEuS3rlYeWJxQ9zqelic2wZELz5vnI6NlorAY1uSTBADOOGiDsZUaPMKa72TTiMV_fe9aUf_I0uLvwfo06UUjeIfmx99nHJvYssq7ZaQDR7khi5rfRr8xk5kqqcFCq7eY3PHleh.FahSaZ95s_wzd3TJiFJZxOwYzvnEXIK80MlJHqaK.DCOxmq1XW4WjDZf2lQbTt3SfOSOLMUb_1HB.1D_UDxz4Hn1mh6VY",
    "_ga_PS3V7B7KV0": "GS1.1.1743065435.364.1.1743067302.0.0.0"
}
url = "https://api-v2.solscan.io/v2/token/activity/dextrading"
params = {
    "address": "4Q8zRhEUH8oTJvfd1qXxE2m7zWSVFjHHD7sZPvWWpump",
    "page": "2",
    "page_size": "100",
    "from_time": "1741413666",
    "to_time": "1741413966"
}
# response = requests.get(url, headers=headers, cookies=cookies, params=params)
cont = 1
while 1:
    print("第{}次请求", cont)
    response = requests.get(url, headers=headers, params=params)

    print(response.text)
    print(response)
    time.sleep(2)
    cont+=1