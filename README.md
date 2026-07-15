# GitSkills

GitHub CLI-like tool designed for OpenClaw, providing GitHub repository management through API.

GitHub CLI-like工具，专为OpenClaw设计，通过API提供GitHub仓库管理功能。

## 功能特性 | Features

- **仓库管理 | Repository Management**：创建、列出、查看、删除仓库 | Create, list, view, delete repositories
- **分支管理 | Branch Management**：创建、列出分支 | Create, list branches
- **PR管理 | PR Management**：创建、列出PR | Create, list PRs
- **Issue管理 | Issue Management**：创建、列出Issue | Create, list issues
- **安全措施 | Security Measures**：token存储在环境变量中 | Token stored in environment variables

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
   ```

   创建`.env`文件：
   ```
   # GitHub API Token
   GITHUB_TOKEN=你的GitHub令牌
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
   - 填写所需的环境变量（GitHub Token）
   - 保存配置

### 方法三：手动安装到OpenClaw | Method 3: Manual Installation to OpenClaw

1. **克隆仓库 | Clone Repository**：
   ```bash
   git clone https://github.com/EdwardWason/gitskills.git
   cd gitskills
   ```

2. **复制技能到OpenClaw | Copy Skill to OpenClaw**：
   - Windows：
     ```bash
     robocopy ".main\skills\github-operations" "C:\Users\你的用户名\.openclaw\skills\github-operations" /E
     ```
   - macOS/Linux：
     ```bash
     cp -r .main/skills/github-operations ~/.openclaw/skills/
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

# 删除仓库 | Delete repository (requires confirmation)
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
- **无外部数据出口 | No External Data Egress**：不包含IM消息发送功能，避免数据泄露风险 | No IM messaging functionality to prevent data leakage

## 贡献指南 | Contribution Guide

详见[CONTRIBUTING.md](CONTRIBUTING.md)文件。
See [CONTRIBUTING.md](CONTRIBUTING.md) file for details.

## 许可证 | License

本项目采用MIT许可证 - 详见[LICENSE](LICENSE)文件。
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.