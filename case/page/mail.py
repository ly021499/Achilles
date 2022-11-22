# @Time   : 2022/11/18 15:42
# @Author : LOUIE
# @Desc   : 邮件
from utils import logwrap
from case.position import camera_pos, profile_pos
from case.lib.page import Page


class Mail(Page):

    @logwrap('打开邮件')
    def open_mail(self):
        self.click(camera_pos.mail_pos)

    @logwrap('一键已读')
    def receive_rewards(self):
        self.click(profile_pos.read_all_pos)

    @logwrap('关闭邮件')
    def close_mail(self):
        self.click(profile_pos.close_mail_pos)

    @logwrap('一键领取')
    def one_click_collection(self):
        self.click(profile_pos.read_all_pos)





