### README.md

```markdown
# EVM Wallet and NFT Minting Script

这是一个Python项目，旨在生成EVM钱包地址、领取测试代币，并铸造测试NFT。

## 项目结构

- `generate_wallets.py`: 生成EVM钱包地址并保存到`wallet.csv`文件中。
- `claim_tokens.py`: 从`wallet.csv`中读取钱包地址，并通过HTTP请求领取测试代币。
- `mint_nft.py`: 从`wallet.csv`中读取钱包地址，并与合约交互以铸造测试NFT。

## 环境要求

- Python 3.x
- 安装的Python库：
  - `eth-account`
  - `requests`
  - `web3`

## 安装

1. 克隆或下载此项目。
2. 使用以下命令安装所需的Python库：

   ```bash
   pip install -r requirements.txt
```

## 使用说明

1. **生成钱包地址**

   运行`generate_wallets.py`以生成EVM钱包地址，并将其保存到`wallet.csv`文件中。

   ```bash
   python generate_wallets.py
   ```

2. **领取测试代币**

   运行`claim_tokens.py`以从`wallet.csv`中读取钱包地址，并通过HTTP请求领取测试代币。

   ```bash
   python claim_tokens.py
   ```

3. **铸造测试NFT**

   运行`mint_nft.py`以从`wallet.csv`中读取钱包地址，并与合约交互以铸造测试NFT。

   ```bash
   python mint_nft.py
   ```

## 配置

- `wallet.csv`: 存储生成的钱包地址和私钥。
- `ip.config`: 存储代理IP地址（仅一行文本）。

## 注意事项

- 确保在进行任何操作之前已正确设置代理IP。
- 请注意保护您的私钥，切勿在生产环境中使用这些测试钱包。
