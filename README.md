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

- Slack
- Discord
- Telegram
- 微信
- 邮件

## 贡献指南

详见[CONTRIBUTING.md](CONTRIBUTING.md)文件。

## 许可证

本项目采用MIT许可证 - 详见[LICENSE](LICENSE)文件。
