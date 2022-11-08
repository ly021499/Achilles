# @Time   : 2022/11/2 19:05
# @Author : LOUIE
# @Desc   : 企业微信webhook
import requests
from setting import URL
from utils import log


class Wechat:
    
    def __init__(self) -> None:
        self.content = None

    def build_content(self):
        content = {}
        self.content = content
        return content
    
    def send_msg(self):
        content = self.build_content()
        res = requests.post(url=URL, json=content)
        res.raise_for_status()
        res = res.json()
        if res['errmsg'] == 'ok':
            log.info("Message sent successfully")
        else:
            log.error(f"Message sending failed")


wechat = Wechat()


if __name__ == '__main__':
    wechat.send_msg()

