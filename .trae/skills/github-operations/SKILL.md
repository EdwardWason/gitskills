# GitHub Operations Skill

A comprehensive GitHub operations skill for OpenClaw, allowing users to manage GitHub repositories, branches, PRs, and issues through various IM channels.

## Features

- **Repository Management**: Create, list, view, delete repositories
- **Branch Management**: Create, list branches
- **PR Management**: Create, list PRs
- **Issue Management**: Create, list issues
- **Git History Cleaning**: Remove sensitive files from git history
- **IM Channel Integration**: Feishu, WeCom, Weixin, Slack

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/EdwardWason/gitskills.git
   cd gitskills
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**:
   Create a `.env` file with your GitHub token and IM channel configurations.

## Usage

### Basic Commands

#### Repository Management
```bash
# List all repositories
python main.py repo list

# Create new repository
python main.py repo create --name my-repo --description "My new repository"

# Get repository details
python main.py repo get --name my-repo

# Delete repository (requires confirmation)
python main.py repo delete --name my-repo
```

#### Branch Management
```bash
# Create new branch
python main.py branch create --repo my-repo --name feature-branch

# List branches
python main.py branch list --repo my-repo
```

#### PR Management
```bash
# Create PR
python main.py pr create --repo my-repo --title "Add new feature" --body "This is a new feature" --head feature-branch --base main

# List PRs
python main.py pr list --repo my-repo
```

#### Issue Management
```bash
# Create Issue
python main.py issue create --repo my-repo --title "Bug report" --body "Something is broken"

# List Issues
python main.py issue list --repo my-repo
```

#### Git History Cleaning
```bash
# Clean sensitive file from git history
python main.py clean --repo my-repo --file sensitive-file.txt
```

#### Send Message to IM Channel
```bash
# Send message to default channel
python main.py message --content "Hello from GitSkills"

# Send message to specific channel
python main.py message --content "Hello from GitSkills" --channel feishu
```

## Security

- **Token Security**: GitHub token stored in environment variables
- **Permission Control**: Use token with minimum permissions
- **Operation Verification**: Important operations require user confirmation
- **Logging**: Record all operations for auditing
- **Error Handling**: Handle exceptions to avoid information leakage

## IM Channel Configuration

### Feishu
```
FEISHU_WEBHOOK_URL=https://open.feishu.cn/open-apis/bot/v2/hook/your-webhook-id
```

### WeCom
```
WECOM_CORP_ID=your-corp-id
WECOM_APP_SECRET=your-app-secret
WECOM_AGENT_ID=your-agent-id
```

### Weixin
```
WEIXIN_BOT_TOKEN=your-ilink-bot-token
WEIXIN_API_URL=https://api.ilink.qq.com
```

### Slack
```
SLACK_API_TOKEN=your-slack-api-token
SLACK_CHANNEL=#general
```

## Dependencies

- PyGithub
- python-dotenv
- requests

## License

MIT License