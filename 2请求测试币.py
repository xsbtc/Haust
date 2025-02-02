import csv
import requests

# 从配置文件中读取代理IP
with open('ip.config', 'r') as f:
    proxy_ip = f.readline().strip()

# 设置代理
proxies = {
    'http': proxy_ip,
    'https': proxy_ip,
}

# 读取钱包地址
with open('wallet.csv', mode='r') as file:
    reader = csv.DictReader(file)
    addresses = [row['Address'] for row in reader]

# 设置请求的URL
url = "https://faucet.haust.app/api/claim"

# 初始化计数器
count = 0

# 遍历钱包地址并发送POST请求
for address in addresses:
    # 增加计数器
    count += 1

    # 设置请求体
    payload = {"address": address}

    try:
        # 发送POST请求
        response = requests.post(url, json=payload, proxies=proxies)

        # 检查响应状态码
        if response.status_code == 200:
            print(f"第 {count} 次执行操作成功：{response.json()['msg']}")
        else:
            print(f"第 {count} 次执行操作失败，状态码：{response.status_code}")

    except requests.RequestException as e:
        print(f"第 {count} 次执行操作时发生错误：{e}")

# 提示用户操作完成
print("所有操作已完成。")
