import requests
import bs4
from spider_of_word import *
import Kit

main_host = "https://zh.moegirl.org.cn"
start_url = "https://zh.moegirl.org.cn/%E5%8E%9F%E7%A5%9E"
module = "原神"


rsp = requests.get(start_url)
db = Kit.sqlitDatabase('mengNiang.db')

# 使用bs4解析
soup = bs4.BeautifulSoup(rsp.text, "html.parser")

# 使用CSS选择器定位元素
# target_element = soup.select("#mw-content-text > div > table")
target_element = soup.select("#mw-content-text > div > table > tbody > tr > td > table > tbody > tr td > table > tbody > tr > td.navbox-list.navbox-odd > table > tbody > tr > td.navbox-list.navbox-even > div > a")

# 检查是否找到了目标元素
if target_element:
    # 打印目标元素
    print("数量：", len(target_element))
    for word_baike in target_element:
        title = word_baike['title']
        herf = word_baike['href']
        target_url = main_host + herf

        print("\n\n\n")
        ans = db.read_data(title)
        if ans:
            print("已存在：", title)
            continue

        print("开始爬取数据")
        print("标题：", title)
        print("链接：", target_url)
        process_url(target_url, title, module)


else:
    print("未找到目标元素")
