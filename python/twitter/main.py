import asyncio
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
    client.save_cookies('cookies.json')
    print('登录成功')


asyncio.run(main())
