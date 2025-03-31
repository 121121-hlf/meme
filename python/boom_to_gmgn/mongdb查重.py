from pymongo import MongoClient

# 连接到MongoDB服务器
client = MongoClient('mongodb://localhost:27017/')

# 选择数据库
db = client['boom_db']

# 选择集合
collection = db['boom_walletAddress']

while True:
    # 计算集合中的文档总数
    total_count_sl__7_int = collection.count_documents({'fraud': {'$ne': 1}, 'sl_7_int': {'$lt': 100}})

    # 计算前百分之30的文档数量
    limit_count_sl_7_int = int(total_count_sl__7_int * 0.2)

    # 对字段a进行降序排序并取前百分之30的文档
    top_30_docs_limit_count_sl_7_int = collection.find({'fraud': {'$ne': 1}, 'sl_7_int': {'$lt': 100}}).sort('sl_7_int', -1).limit(limit_count_sl_7_int)

    # 计算集合中的文档总数
    total_count_ys__7_int = collection.count_documents({'fraud': {'$ne': 1}, 'sl_7_int': {'$lt': 100}})

    # 计算前百分之30的文档数量
    limit_count_ys_7_int = int(total_count_ys__7_int * 0.3)

    # 对字段a进行降序排序并取前百分之30的文档
    top_30_docs_limit_count_ys__7_int = collection.find({'fraud': {'$ne': 1}, 'sl_7_int': {'$lt': 100}}).sort('ys_7_int', -1).limit(limit_count_ys_7_int)

    # 提取两个查询结果中的walletAddress字段
    wallet_addresses_sl = {doc['walletAddress'] for doc in top_30_docs_limit_count_sl_7_int}
    wallet_addresses_ys = {doc['walletAddress'] for doc in top_30_docs_limit_count_ys__7_int}

    # 计算重合的walletAddress数量
    intersection_count = len(wallet_addresses_sl.intersection(wallet_addresses_ys))

    # 计算重合率
    overlap_rate = intersection_count / min(len(wallet_addresses_sl), len(wallet_addresses_ys))
    # 打印重合的walletAddress
    common_wallet_addresses = wallet_addresses_sl.intersection(wallet_addresses_ys)
    # 更新common_wallet_addresses中的每个地址，设置字段'重合sl_20_ys_30'为1
    for wallet_address in common_wallet_addresses:
        collection.update_one(
            {'walletAddress': wallet_address},
            {'$set': {'coincide_sl_20_ys_30': 10}}
        )
        # print(f'修改：{wallet_address}')
