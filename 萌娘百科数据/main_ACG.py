import requests
import bs4
from spider_of_word import *
import Kit

main_host = "https://zh.moegirl.org.cn"
start_url = "https://zh.moegirl.org.cn/Template:ACG%E7%BB%8F%E5%85%B8%E5%8F%B0%E8%AF%8D"
module = "ACG经典台词"

start_url = "https://zh.moegirl.org.cn/Template:ACG%E5%9C%88%E7%94%A8%E8%AF%AD"
module = "ACG圈用语"

start_url ="https://zh.moegirl.org.cn/Template:%E5%BC%B9%E5%B9%95%E6%96%87%E5%8C%96"
module = "弹幕文化"


rsp = requests.get(start_url)
db = Kit.sqlitDatabase('mengNiang.db')

# 使用bs4解析
soup = bs4.BeautifulSoup(rsp.text, "html.parser")

# 使用CSS选择器定位元素
# target_element = soup.select("#mw-content-text > div > table")
target_element = soup.select("#mw-content-text > div > table > tbody > tr > td > table > tbody > tr > td.navbox-list.navbox-even > div > a")

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
