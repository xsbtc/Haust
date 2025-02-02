from eth_account import Account
import csv

# 设置生成钱包的数量
num_wallets = 100

# 打开或创建一个CSV文件用于写入
with open('wallet.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    # 写入CSV文件的表头
    writer.writerow(['Address', 'Private Key'])

    # 生成指定数量的钱包
    for _ in range(num_wallets):
        # 生成一个新的账户
        account = Account.create()

        # 获取钱包地址
        address = account.address

        # 获取私钥（以十六进制字符串的形式）
        private_key = account.key.hex()

        # 将钱包地址和私钥写入CSV文件
        writer.writerow([address, private_key])

        # 打印生成的钱包地址和私钥，以便查看
        print(f'Address: {address}, Private Key: {private_key}')

# 提示用户生成完成
print(f'{num_wallets} 个钱包地址和私钥已保存到 wallet.csv 文件中。')
