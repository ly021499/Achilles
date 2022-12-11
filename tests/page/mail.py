# @Time   : 2022/11/18 15:42
# @Author : LOUIE
# @Desc   : 邮件
from utils import log
from tests.position import camera_pos, profile_pos
from tests.lib.page import Page


class Mail(Page):

    @log.wrap('打开邮件')
    def open_mail(self):
        self.click(camera_pos.mail_pos)

    @log.wrap('一键已读')
    def receive_rewards(self):
        self.click(profile_pos.read_all_pos)

    @log.wrap('关闭邮件')
    def close_mail(self):
        self.click(profile_pos.close_mail_pos)

    @log.wrap('一键领取')
    def one_click_collection(self):
        self.click(profile_pos.read_all_pos)





