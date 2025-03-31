from DrissionPage import Chromium

tab = Chromium().latest_tab
tab.get(f'https://x.com/search?q=66QLFR3jtpixFTCWR9GpSHEYsrJjNuzSJSCa1kgHpump')
while True:
    tab.scroll(600)
    devs = tab.ele(
        'xpath://*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/section/div/div/div//div[@dir="auto"]//text()')
    print(devs)
    tab.wait(5)
