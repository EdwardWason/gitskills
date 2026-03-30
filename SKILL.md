---
name: "gitskills"
description: "GitHub CLI-like tool for OpenClaw to control GitHub account through various IM channels. Invoke when user needs to manage GitHub repositories, issues, PRs, and other GitHub operations through IM."
---

# GitSkills

## 功能概述

GitSkills是一个专门为OpenClaw设计的GitHub CLI-like工具，允许用户通过各种IM通道控制GitHub账号，实现各种GitHub操作，同时保护个人信息和token安全。

## 支持的操作

### 1. 仓库管理

- 创建仓库
- 克隆仓库
- 删除仓库
- 列出仓库
- 查看仓库详情

### 2. 分支管理

- 创建分支
- 切换分支
- 合并分支
- 删除分支
- 列出分支

### 3. PR管理

- 创建PR
- 查看PR列表
- 查看PR详情
- 合并PR
- 关闭PR

### 4. Issue管理

- 创建Issue
- 查看Issue列表
- 查看Issue详情
- 关闭Issue
- 添加评论

### 5. 提交管理

- 提交代码
- 查看提交历史
- 撤销提交

## 安装与配置

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置环境变量

创建`.env`文件，添加以下内容：

```
# GitHub API Token
GITHUB_TOKEN=your_github_token_here

# IM Channel Configuration
IM_CHANNEL=your_im_channel_here
IM_API_KEY=your_im_api_key_here
```

### 3. 配置IM通道

根据你使用的IM通道，配置相应的API密钥和参数。

## 使用方法

### 基本命令格式

```
@GitSkills <command> [options]
```

### 示例命令

#### 仓库管理

```
@GitSkills create-repo --name my-repo --description "My new repository"
@GitSkills clone-repo --url https://github.com/username/repo.git
@GitSkills list-repos
```

#### 分支管理

```
@GitSkills create-branch --name feature-branch --repo username/repo
@GitSkills switch-branch --name feature-branch
@GitSkills merge-branch --source feature-branch --target main
```

#### PR管理

```
@GitSkills create-pr --title "Add new feature" --body "This adds a new feature" --head feature-branch --base main --repo username/repo
@GitSkills list-prs --repo username/repo
@GitSkills merge-pr --number 1 --repo username/repo
```

#### Issue管理

```
@GitSkills create-issue --title "Bug report" --body "Something is broken" --repo username/repo
@GitSkills list-issues --repo username/repo
@GitSkills close-issue --number 1 --repo username/repo
```

## 安全措施

1. **Token安全**：GitHub token存储在环境变量中，不硬编码在代码中
2. **权限控制**：根据用户需求设置最小权限的token
3. **操作验证**：重要操作需要用户确认
4. **日志记录**：记录所有操作，便于审计
5. **错误处理**：处理异常情况，避免信息泄露

## 支持的IM通道

- Slack
- Discord
- Telegram
- WeChat
- Email

## 扩展功能

### 自定义命令

可以通过配置文件添加自定义命令，扩展功能。

### 自动化工作流

可以设置自动化工作流，例如：
- 当PR创建时自动通知
- 当Issue关闭时自动标记
- 定期清理无用分支

## 常见问题

### Q: 如何获取GitHub token？
A: 登录GitHub账号，进入Settings → Developer settings → Personal access tokens → Generate new token

### Q: 如何配置IM通道？
A: 参考各IM平台的API文档，获取API密钥并配置在.env文件中

### Q: 如何处理权限错误？
A: 确保GitHub token具有足够的权限，参考GitHub文档设置正确的权限范围

### Q: 如何扩展功能？
A: 编辑main.py文件，添加新的命令处理函数

## 技术实现

- 语言：Python
- 依赖：PyGithub, python-dotenv, requests
- 架构：模块化设计，易于扩展

## 后续计划

- 添加更多IM通道支持
- 实现更复杂的自动化工作流
- 提供Web界面管理
- 支持团队协作功能
