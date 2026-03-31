# GitSkills

GitHub CLI-like工具，专为OpenClaw设计，允许通过各种IM通道控制GitHub账号。

## 功能特性

- **仓库管理**：创建、列出、查看、删除仓库
- **分支管理**：创建、列出分支
- **PR管理**：创建、列出PR
- **Issue管理**：创建、列出Issue
- **安全措施**：token存储在环境变量中
- **IM通道支持**：Slack、Discord、Telegram、微信、邮件

## 安装说明

1. **克隆仓库**：
   ```bash
   git clone https://github.com/EdwardWason/gitskills.git
   cd gitskills
   ```

2. **安装依赖**：
   ```bash
   pip install -r requirements.txt
   ```

3. **配置环境变量**：
   创建`.env`文件：
   ```
   # GitHub API Token
   GITHUB_TOKEN=你的GitHub令牌
   
   # IM通道配置
   IM_CHANNEL=你的IM通道
   IM_API_KEY=你的IM API密钥
   ```

## 使用方法

### 基本命令

#### 仓库管理
```bash
# 列出所有仓库
python main.py repo list

# 创建新仓库
python main.py repo create --name my-repo --description "我的新仓库"

# 获取仓库详情
python main.py repo get --name my-repo

# 删除仓库
python main.py repo delete --name my-repo
```

#### 分支管理
```bash
# 创建新分支
python main.py branch create --repo my-repo --name feature-branch

# 列出分支
python main.py branch list --repo my-repo
```

#### PR管理
```bash
# 创建PR
python main.py pr create --repo my-repo --title "添加新功能" --body "这是一个新功能" --head feature-branch --base main

# 列出PR
python main.py pr list --repo my-repo
```

#### Issue管理
```bash
# 创建Issue
python main.py issue create --repo my-repo --title "Bug报告" --body "有东西坏了"

# 列出Issue
python main.py issue list --repo my-repo
```

## 安全措施

- **Token安全**：GitHub token存储在环境变量中，不硬编码在代码中
- **权限控制**：使用最小权限的token
- **操作验证**：重要操作需要用户确认
- **日志记录**：记录所有操作，便于审计
- **错误处理**：处理异常情况，避免信息泄露

## 支持的IM通道

- **Slack**：企业协作平台
- **Discord**：游戏社区平台
- **Telegram**：即时通讯应用
- **飞书**：字节跳动企业协作平台
- **企业微信**：腾讯企业协作平台
- **微信个人号**：通过iLink Bot接入
- **邮件**：传统邮件通知

## IM通道配置

### 飞书配置

1. 获取飞书机器人Webhook URL
2. 在`.env`文件中添加：
   ```
   FEISHU_WEBHOOK_URL=https://open.feishu.cn/open-apis/bot/v2/hook/your-webhook-id
   ```
3. 运行示例：
   ```bash
   python examples/feishu_integration.py
   ```

### 企业微信配置

1. 获取企业微信应用配置
2. 在`.env`文件中添加：
   ```
   WECOM_CORP_ID=你的企业ID
   WECOM_APP_SECRET=你的应用密钥
   WECOM_AGENT_ID=你的应用ID
   ```
3. 运行示例：
   ```bash
   python examples/wechat_integration.py
   ```

### 微信个人号配置

1. 获取iLink Bot Token
2. 在`.env`文件中添加：
   ```
   WEIXIN_BOT_TOKEN=你的iLink Bot Token
   WEIXIN_API_URL=https://api.ilink.qq.com
   ```
3. 运行示例：
   ```bash
   python examples/wechat_integration.py
   ```

### Slack配置

1. 获取Slack API Token
2. 在`.env`文件中添加：
   ```
   SLACK_API_TOKEN=你的Slack API Token
   ```
3. 运行示例：
   ```bash
   python examples/slack_integration.py
   ```

## 贡献指南

详见[CONTRIBUTING.md](CONTRIBUTING.md)文件。

## 许可证

本项目采用MIT许可证 - 详见[LICENSE](LICENSE)文件。
