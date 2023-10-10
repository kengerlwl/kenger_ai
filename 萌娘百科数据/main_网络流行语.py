import requests
import bs4
from spider_of_word import *
import Kit

main_host = "https://zh.moegirl.org.cn"
start_url = "https://zh.moegirl.org.cn/Template:%E4%B8%AD%E5%9B%BD%E7%BD%91%E7%BB%9C%E6%B5%81%E8%A1%8C%E8%AF%AD%E5%8F%A5"
module = "中国网络流行语句"


start_url = "https://zh.moegirl.org.cn/Template:%E6%AC%A7%E7%BE%8E%E7%BD%91%E7%BB%9C%E6%B5%81%E8%A1%8C%E8%AF%AD%E5%8F%A5"
module = "欧美网络流行语句"


rsp = requests.get(start_url)
db = Kit.sqlitDatabase('mengNiang.db')

# 使用bs4解析
soup = bs4.BeautifulSoup(rsp.text, "html.parser")

# 使用CSS选择器定位元素
# target_element = soup.select("#mw-content-text > div > table")
target_element = soup.select("#mw-content-text > div > table > tbody > tr > td > table > tbody > tr > td > div > a")

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
