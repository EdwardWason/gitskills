# GitSkills

GitHub CLI-like tool designed for OpenClaw, allowing control of GitHub accounts through various IM channels.

GitHub CLI-like工具，专为OpenClaw设计，允许通过各种IM通道控制GitHub账号。

## 功能特性 | Features

- **仓库管理 | Repository Management**：创建、列出、查看、删除仓库 | Create, list, view, delete repositories
- **分支管理 | Branch Management**：创建、列出分支 | Create, list branches
- **PR管理 | PR Management**：创建、列出PR | Create, list PRs
- **Issue管理 | Issue Management**：创建、列出Issue | Create, list issues
- **安全措施 | Security Measures**：token存储在环境变量中 | Token stored in environment variables
- **IM通道支持 | IM Channel Support**：Slack、Discord、Telegram、微信、邮件 | Slack, Discord, Telegram, WeChat, Email

## 安装说明 | Installation

### 方法一：克隆仓库安装 | Method 1: Clone Repository

1. **克隆仓库 | Clone Repository**：
   ```bash
   git clone https://github.com/EdwardWason/gitskills.git
   cd gitskills
   ```

2. **安装依赖 | Install Dependencies**：
   ```bash
   pip install -r requirements.txt
   ```

3. **配置环境变量 | Configure Environment Variables**：
   Create `.env` file：
   ```
   # GitHub API Token
   GITHUB_TOKEN=your-github-token
   
   # IM Channel Configuration
   IM_CHANNEL=your-im-channel
   IM_API_KEY=your-im-api-key
   ```

   创建`.env`文件：
   ```
   # GitHub API Token
   GITHUB_TOKEN=你的GitHub令牌
   
   # IM通道配置
   IM_CHANNEL=你的IM通道
   IM_API_KEY=你的IM API密钥
   ```

### 方法二：通过Releases安装 | Method 2: Install via Releases

1. **下载技能压缩包 | Download Skill Zip Package**：
   - 访问 [GitHub Releases](https://github.com/EdwardWason/gitskills/releases)
   - 下载最新版本的 `github-operations-skill.zip` 文件

2. **安装到OpenClaw | Install to OpenClaw**：
   - 打开OpenClaw
   - 进入「技能管理」页面
   - 点击「安装技能」按钮
   - 选择下载的 `github-operations-skill.zip` 文件
   - 等待安装完成

3. **配置环境变量 | Configure Environment Variables**：
   - 安装完成后，在OpenClaw技能管理页面找到「github-operations」技能
   - 点击「配置」按钮
   - 填写所需的环境变量（GitHub Token、IM通道配置等）
   - 保存配置

### 如何创建技能压缩包（维护者指南） | How to Create Skill Zip Package (Maintainer Guide)

1. **更新技能文件 | Update Skill Files**：
   - 确保 `github-operations` 目录中的所有文件都是最新的
   - 包括 `SKILL.md`、`_meta.json`、`requirements.txt` 和 `scripts/` 目录中的代码文件

2. **创建压缩包 | Create Zip Package**：
   - 在项目根目录执行以下命令：
     ```bash
     # Windows
     Compress-Archive -Path ".trae\skills\github-operations\*" -DestinationPath "github-operations-skill.zip" -Force
     
     # macOS/Linux
     zip -r github-operations-skill.zip .trae/skills/github-operations/
     ```

3. **发布到GitHub Releases | Publish to GitHub Releases**：
   - 访问 GitHub 仓库页面
   - 点击「Releases」选项卡
   - 点击「Draft a new release」按钮
   - 填写版本号、标题和描述
   - 上传 `github-operations-skill.zip` 文件
   - 点击「Publish release」按钮

### 方法三：手动安装到OpenClaw | Method 3: Manual Installation to OpenClaw

1. **克隆仓库 | Clone Repository**：
   ```bash
   git clone https://github.com/EdwardWason/gitskills.git
   cd gitskills
   ```

2. **复制技能到OpenClaw | Copy Skill to OpenClaw**：
   - Windows：
     ```bash
     robocopy ".trae\skills\github-operations" "C:\Users\你的用户名\.openclaw\skills\github-operations" /E
     ```
   - macOS/Linux：
     ```bash
     cp -r .trae/skills/github-operations ~/.openclaw/skills/
     ```

3. **安装依赖 | Install Dependencies**：
   ```bash
   pip install -r requirements.txt
   ```

4. **配置环境变量 | Configure Environment Variables**：
   - 在OpenClaw中配置环境变量，或创建 `.env` 文件在技能目录中

## 使用方法 | Usage

### 基本命令 | Basic Commands

#### 仓库管理 | Repository Management
```bash
# 列出所有仓库 | List all repositories
python main.py repo list

# 创建新仓库 | Create new repository
python main.py repo create --name my-repo --description "我的新仓库"  # Chinese description
python main.py repo create --name my-repo --description "My new repository"  # English description

# 获取仓库详情 | Get repository details
python main.py repo get --name my-repo

# 删除仓库 | Delete repository
python main.py repo delete --name my-repo
```

#### 分支管理 | Branch Management
```bash
# 创建新分支 | Create new branch
python main.py branch create --repo my-repo --name feature-branch

# 列出分支 | List branches
python main.py branch list --repo my-repo
```

#### PR管理 | PR Management
```bash
# 创建PR | Create PR
python main.py pr create --repo my-repo --title "添加新功能" --body "这是一个新功能" --head feature-branch --base main  # Chinese
python main.py pr create --repo my-repo --title "Add new feature" --body "This is a new feature" --head feature-branch --base main  # English

# 列出PR | List PRs
python main.py pr list --repo my-repo
```

#### Issue管理 | Issue Management
```bash
# 创建Issue | Create issue
python main.py issue create --repo my-repo --title "Bug报告" --body "有东西坏了"  # Chinese
python main.py issue create --repo my-repo --title "Bug report" --body "Something is broken"  # English

# 列出Issue | List issues
python main.py issue list --repo my-repo
```

## 安全措施 | Security Measures

- **Token安全 | Token Security**：GitHub token存储在环境变量中，不硬编码在代码中 | GitHub token stored in environment variables, not hardcoded in code
- **权限控制 | Permission Control**：使用最小权限的token | Use token with minimum permissions
- **操作验证 | Operation Verification**：重要操作需要用户确认 | Important operations require user confirmation
- **日志记录 | Logging**：记录所有操作，便于审计 | Record all operations for auditing
- **错误处理 | Error Handling**：处理异常情况，避免信息泄露 | Handle exceptions to avoid information leakage

## 支持的IM通道 | Supported IM Channels

- **Slack**：企业协作平台 | Enterprise collaboration platform
- **Discord**：游戏社区平台 | Gaming community platform
- **Telegram**：即时通讯应用 | Instant messaging app
- **飞书**：字节跳动企业协作平台 | ByteDance enterprise collaboration platform
- **企业微信**：腾讯企业协作平台 | Tencent enterprise collaboration platform
- **微信个人号**：通过iLink Bot接入 | WeChat personal account via iLink Bot
- **邮件**：传统邮件通知 | Traditional email notification

## IM通道配置 | IM Channel Configuration

### 飞书配置 | Feishu Configuration

1. 获取飞书机器人Webhook URL | Get Feishu bot Webhook URL
2. 在`.env`文件中添加 | Add to `.env` file：
   ```
   FEISHU_WEBHOOK_URL=https://open.feishu.cn/open-apis/bot/v2/hook/your-webhook-id
   ```
3. 运行示例 | Run example：
   ```bash
   python examples/feishu_integration.py
   ```

### 企业微信配置 | WeCom Configuration

1. 获取企业微信应用配置 | Get WeCom app configuration
2. 在`.env`文件中添加 | Add to `.env` file：
   ```
   WECOM_CORP_ID=your-corp-id
   WECOM_APP_SECRET=your-app-secret
   WECOM_AGENT_ID=your-agent-id
   ```

   ```
   WECOM_CORP_ID=你的企业ID
   WECOM_APP_SECRET=你的应用密钥
   WECOM_AGENT_ID=你的应用ID
   ```
3. 运行示例 | Run example：
   ```bash
   python examples/wechat_integration.py
   ```

### 微信个人号配置 | WeChat Personal Account Configuration

1. 获取iLink Bot Token | Get iLink Bot Token
2. 在`.env`文件中添加 | Add to `.env` file：
   ```
   WEIXIN_BOT_TOKEN=your-ilink-bot-token
   WEIXIN_API_URL=https://api.ilink.qq.com
   ```

   ```
   WEIXIN_BOT_TOKEN=你的iLink Bot Token
   WEIXIN_API_URL=https://api.ilink.qq.com
   ```
3. 运行示例 | Run example：
   ```bash
   python examples/wechat_integration.py
   ```

### Slack配置 | Slack Configuration

1. 获取Slack API Token | Get Slack API Token
2. 在`.env`文件中添加 | Add to `.env` file：
   ```
   SLACK_API_TOKEN=your-slack-api-token
   ```

   ```
   SLACK_API_TOKEN=你的Slack API Token
   ```
3. 运行示例 | Run example：
   ```bash
   python examples/slack_integration.py
   ```

## 贡献指南 | Contribution Guide

详见[CONTRIBUTING.md](CONTRIBUTING.md)文件。
See [CONTRIBUTING.md](CONTRIBUTING.md) file for details.

## 许可证 | License

本项目采用MIT许可证 - 详见[LICENSE](LICENSE)文件。
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
