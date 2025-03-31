from gmgn import get_address_buy_token
from solscan import get_solscan_data

if __name__ == '__main__':
    address = "Ay9wnuZCRTceZJuRpGZnuwYZuWdsviM4cMiCwFoSQiPH"
    items = get_address_buy_token(address)
    print(items)
    address_item = {}
    for item in items:
        print("购买的代币", item)
        ok_address_list = get_solscan_data(item['address'], item['token_address'], item['start_time'], item['end_time'])
        for ok_address in ok_address_list:
            if ok_address not in address_item:
                address_item[ok_address] = 1
            else:
                address_item[ok_address] = address_item[ok_address]+1
        print(address_item)
