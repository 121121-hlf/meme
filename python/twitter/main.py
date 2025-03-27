import asyncio
import time

from twikit import Client

USERNAME = 'meme_grok'
EMAIL = 'hlf1171850713@gmail.com'
PASSWORD = 'hlf121121'

# 初始化客户端
client = Client('en-US')


async def main():
    await client.login(
        auth_info_1=USERNAME,
        auth_info_2=EMAIL,
        password=PASSWORD,
        cookies_file='cookies.json'
    )
    tweets = await client.search_tweet('4TBi66vi32S7J8X1A6eWfaLHYmUXu7CStcEmsJQdpump', 'Latest')
    print("第一次大小", len(tweets))
    for tweet in tweets:
        print(tweet.id)
    #     print(tweet.created_at_datetime)
    #     print(tweet.text)
    print("==================")
    while True:
        time.sleep(2)
        more_tweets = await tweets.next()  # Retrieve more tweets
        print("大小", len(more_tweets))
        for tweet in more_tweets:
            print(tweet.id)
        #     print(tweet.created_at_datetime)
        #     print(tweet.text)
        print("==================")
        if len(more_tweets) == 0:
            break

    print('登录成功')


asyncio.run(main())
