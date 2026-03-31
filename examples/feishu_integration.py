#!/usr/bin/env python3
"""
飞书集成示例
"""

import os
import requests
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

class FeishuIntegration:
    """飞书集成类"""
    
    def __init__(self):
        """初始化飞书集成"""
        self.feishu_app_id = os.getenv('FEISHU_APP_ID')
        self.feishu_app_secret = os.getenv('FEISHU_APP_SECRET')
        self.feishu_bot_url = os.getenv('FEISHU_BOT_URL', 'https://open.feishu.cn/open-apis/bot/v2/hook')
        self.access_token = None
    
    def get_access_token(self):
        """获取飞书访问令牌"""
        if not self.access_token:
            url = "https://open.feishu.cn/open-apis/auth/v3/app_access_token/internal/"
            headers = {
                "Content-Type": "application/json"
            }
            payload = {
                "app_id": self.feishu_app_id,
                "app_secret": self.feishu_app_secret
            }
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                self.access_token = response.json().get('app_access_token')
        return self.access_token
    
    def send_message(self, message):
        """发送消息到飞书"""
        # 使用飞书机器人Webhook发送消息
        webhook_url = os.getenv('FEISHU_WEBHOOK_URL')
        if webhook_url:
            payload = {
                "msg_type": "text",
                "content": {
                    "text": message
                }
            }
            response = requests.post(webhook_url, json=payload)
            return response.json()
        return {"error": "FEISHU_WEBHOOK_URL not set"}
    
    def handle_command(self, command, args):
        """处理飞书命令"""
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
    feishu_int = FeishuIntegration()
    
    # 发送测试消息
    feishu_int.send_message('GitSkills测试消息')
    
    # 处理命令
    result = feishu_int.handle_command('repo list', [])
    feishu_int.send_message(f'仓库列表：\n{result}')
