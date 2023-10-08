import csv

# 从raw.txt文件中读取文本数据
with open("raw.txt", mode='r', encoding='utf-8') as text_file:
    lines = text_file.read().splitlines()

# 初始化一个空的数据列表
data = []

# 处理文本数据并添加到数据列表中
for i in range(0, len(lines), 2):
    # 跳过空行
    if not lines[i].strip() or not lines[i+1].strip():
        continue

    number = int(lines[i])
    text = lines[i + 1]
    data.append((number, text))

# 指定CSV文件名
csv_filename = "tieba.csv"
# 写入CSV文件
with open(csv_filename, mode='w', encoding='utf-8', newline='') as file:
    # 写入数据
    for item in data:
        # writer.writerow(item)
        file.write(item[1] + "\n")

# # 写入CSV文件
# with open(csv_filename, mode='w', encoding='utf-8', newline='') as file:
#     writer = csv.writer(file, delimiter="")
    
#     # # 写入表头
#     # writer.writerow(["编号", "文本"])
    
#     # # 写入数据
#     # for item in data:
#     #     writer.writerow(item)
#     # 写入数据
#     print(data)
#     for item in data:
#         # writer.writerow()
#         writer.writerow("sdfa")


print(f"数据已成功写入 {csv_filename} 文件。")
