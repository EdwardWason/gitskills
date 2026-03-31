#!/usr/bin/env python3
"""
微信集成示例
基于OpenClaw官方微信插件
"""

import os
import requests
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

class WeChatIntegration:
    """微信集成类"""
    
    def __init__(self):
        """初始化微信集成"""
        # 企业微信配置
        self.wecom_corp_id = os.getenv('WECOM_CORP_ID')
        self.wecom_app_secret = os.getenv('WECOM_APP_SECRET')
        self.wecom_agent_id = os.getenv('WECOM_AGENT_ID')
        
        # 微信个人号配置（使用iLink Bot）
        self.weixin_bot_token = os.getenv('WEIXIN_BOT_TOKEN')
        self.weixin_api_url = os.getenv('WEIXIN_API_URL', 'https://api.ilink.qq.com')
        
        self.access_token = None
    
    def get_wecom_access_token(self):
        """获取企业微信访问令牌"""
        if not self.access_token:
            url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self.wecom_corp_id}&corpsecret={self.wecom_app_secret}"
            response = requests.get(url)
            if response.status_code == 200:
                self.access_token = response.json().get('access_token')
        return self.access_token
    
    def send_wecom_message(self, user_id, message):
        """发送消息到企业微信"""
        access_token = self.get_wecom_access_token()
        if access_token:
            url = f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}"
            payload = {
                "touser": user_id,
                "msgtype": "text",
                "agentid": self.wecom_agent_id,
                "text": {
                    "content": message
                }
            }
            response = requests.post(url, json=payload)
            return response.json()
        return {"error": "Failed to get access token"}
    
    def send_weixin_message(self, message):
        """发送消息到微信个人号（使用iLink Bot）"""
        if self.weixin_bot_token:
            url = f"{self.weixin_api_url}/send_message"
            payload = {
                "token": self.weixin_bot_token,
                "message": message
            }
            response = requests.post(url, json=payload)
            return response.json()
        return {"error": "WEIXIN_BOT_TOKEN not set"}
    
    def handle_command(self, command, args):
        """处理微信命令"""
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
    wechat_int = WeChatIntegration()
    
    # 发送测试消息到企业微信
    # wechat_int.send_wecom_message('user123', 'GitSkills测试消息')
    
    # 发送测试消息到微信个人号
    wechat_int.send_weixin_message('GitSkills测试消息')
    
    # 处理命令
    result = wechat_int.handle_command('repo list', [])
    wechat_int.send_weixin_message(f'仓库列表：\n{result}')

