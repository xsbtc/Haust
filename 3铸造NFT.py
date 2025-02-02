from web3 import Web3
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

# 连接到测试网
rpc_url = "https://rpc-testnet.haust.app"
web3 = Web3(Web3.HTTPProvider(rpc_url, request_kwargs={'proxies': proxies}))

# 检查连接是否成功
if not web3.is_connected():
    print("无法连接到测试网")
    exit()

# 目标合约地址和数据
contract_address = "0x6B3f185C4c9246c52acE736CA23170801D636c8E"
data = "0x6871ee40"

# 链ID
chain_id = 1523903251

# 读取钱包地址和私钥
with open('wallet.csv', mode='r') as file:
    reader = csv.DictReader(file)
    wallets = [(row['Address'], row['Private Key']) for row in reader]

# 初始化计数器
count = 0

# 遍历钱包并发送交易
for address, private_key in wallets:
    count += 1
    try:
        # 获取账户的nonce
        nonce = web3.eth.get_transaction_count(address)

        # 获取当前网络的gas价格
        gas_price = web3.eth.gas_price

        # 构建交易
        transaction = {
            'to': contract_address,
            'value': 0,
            'gas': 200000,  # 设定一个合理的gas限制
            'gasPrice': gas_price + 20390000000,
            'nonce': nonce,
            'data': data,
            'chainId': chain_id,
        }

        # 签署交易
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key)

        # 发送交易
        tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)

        # 等待交易确认
        tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

        # 检查交易是否成功
        if tx_receipt['status'] == 1:
            print(f"第 {count} 次执行操作成功，交易哈希：{web3.to_hex(tx_hash)}")
        else:
            print(f"第 {count} 次执行操作失败，重试中...")

    except Exception as e:
        print(f"第 {count} 次执行操作时发生错误：{e}")

# 提示用户操作完成
print("所有操作已完成。")
