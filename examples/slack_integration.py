#!/usr/bin/env python3
"""
Slack集成示例
"""

import os
import slack
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 初始化Slack客户端
slack_token = os.getenv('SLACK_API_TOKEN')
client = slack.WebClient(token=slack_token)

class SlackIntegration:
    """Slack集成类"""
    
    def __init__(self):
        """初始化Slack集成"""
        self.client = client
    
    def send_message(self, channel, message):
        """发送消息到Slack频道"""
        response = self.client.chat_postMessage(
            channel=channel,
            text=message
        )
        return response
    
    def handle_command(self, command, args):
        """处理Slack命令"""
        # 这里可以集成GitSkills的功能
        # 例如：python main.py repo list
        import subprocess
        result = subprocess.run(
            ['python', 'main.py'] + command.split() + args,
            capture_output=True,
            text=True
        )
        return result.stdout

# 示例用法
if __name__ == '__main__':
    slack_int = SlackIntegration()
    
    # 发送测试消息
    slack_int.send_message('#general', 'GitSkills测试消息')
    
    # 处理命令
    result = slack_int.handle_command('repo list', [])
    slack_int.send_message('#general', f'仓库列表：\n{result}')
