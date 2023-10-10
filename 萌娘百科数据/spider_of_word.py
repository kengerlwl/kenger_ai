import requests
import bs4
import Kit


def save_data_sqlite(ans_dict):
    db = Kit.sqlitDatabase('mengNiang.db')
    db.insert_data(**ans_dict)
    db.close()


# 处理单个词条
def process_url(target_url, word_title, module="萌娘百科"):
    rsp = requests.get(target_url)
    soup = bs4.BeautifulSoup(rsp.text, "html5lib")
    target_element = soup.select("#mw-content-text > div")

    ans_dict = {
        'word_title': '',
        'timestamp': Kit.str_time(),
        'html_content': '',
        'p_content': '',
        'module': module
    }



    if target_element:
        target_element = target_element[0]
        h_list = target_element.select("h1, h2, h3, h4, h5, h6")
        p_list = target_element.select("p")

        p_content = ""
        for p in p_list:
            p_content += p.get_text() + "\n"

        timestamp = Kit.str_time()

        ans_dict['word_title'] = word_title
        ans_dict['timestamp'] = timestamp
        ans_dict['html_content'] = rsp.text
        ans_dict['p_content'] = p_content

        save_data_sqlite(ans_dict)
    else:
        print("未找到目标元素")


if __name__ == "__main__":
    # 调用函数并传入参数
    target_url = "https://zh.moegirl.org.cn/%E5%8F%88%E9%BB%91%E6%88%91%E5%A4%A7oo"
    word_title = "又黑我大oo"
    process_url(target_url, word_title)
