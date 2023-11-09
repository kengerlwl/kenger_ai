import sqlite3

class sqlitDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        # 数据库创建数据库表，不会清空已有的数据
        self.create_table()


    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS crawled_data (
                word_title TEXT PRIMARY KEY,
                timestamp TEXT,
                html_content TEXT,
                p_content TEXT,
                module TEXT DEFAULT '中国网络流行语句'
            )
        ''')
        self.conn.commit()

    def insert_data(self, word_title, timestamp, html_content, p_content, module):
        try:
            self.cursor.execute('''
                INSERT OR REPLACE INTO crawled_data (word_title, timestamp, html_content, p_content, module)
                VALUES (?, ?, ?, ?, ?)
            ''', (word_title, timestamp, html_content, p_content, module))
            self.conn.commit()
            print(f'数据已成功插入或更新：{word_title}')
        except sqlite3.Error as e:
            print(f'插入数据时发生错误：{e}')

    def read_data(self, word_title):
        try:
            self.cursor.execute('''
                SELECT * FROM crawled_data WHERE word_title=?
            ''', (word_title,))
            item = self.cursor.fetchone()

            # 返回所有数据
            all_data = []

            if item:
            
                # print(item)
                return {
                    'word_title': item[0],
                    'timestamp': item[1],
                    'html_content': item[2],
                    'p_content': item[3],
                    'module': item[4]
                }
          
            else:
                print(f'未找到数据：{word_title}')
                return None
        except sqlite3.Error as e:
            print(f'读取数据时发生错误：{e}')
            return None
        
    def read_data_by_module(self, module):
        try:
            self.cursor.execute(f'''
                SELECT * FROM crawled_data WHERE module=?
            ''', (module,))
            data = self.cursor.fetchall()

            # 返回所有数据
            all_data = []

            if data:
                for item in data:
                    # print(item)
                    item_dict = {
                        'word_title': item[0],
                        'timestamp': item[1],
                        'html_content': item[2],
                        'p_content': item[3],
                        'module': item[4]
                    }
                    all_data.append(item_dict)
          
                return all_data
            else:
                print(f'未找到数据：')
                return []
        except sqlite3.Error as e:
            print(f'读取数据时发生错误：{e}')
            return []   
    
    def read_all_data(self):
        try:
            self.cursor.execute('''
                SELECT * FROM crawled_data
            ''')
            data = self.cursor.fetchall()

            # 返回所有数据
            all_data = []

            if data:
                for item in data:
                    # print(item)
                    item_dict = {
                        'word_title': item[0],
                        'timestamp': item[1],
                        'html_content': item[2],
                        'p_content': item[3],
                        'module': item[4]
                    }
                    all_data.append(item_dict)
          
                return all_data
            else:
                print(f'未找到数据：')
                return []
        except sqlite3.Error as e:
            print(f'读取数据时发生错误：{e}')
            return []

    def close(self):
        self.conn.close()



if __name__ == "__main__":
    db = sqlitDatabase('../mengNiang.db')
    # db.insert_data('test42', '2020-01-012', 'test', 'test', "test")
    # a = db.read_all_data()
    # a = db.read_data('太长不看')
    a = db.read_data_by_module('中国网络流行语句')
    # print(a)
    for i in a:
        print(i['word_title'])
    db.close()