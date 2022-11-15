# @Time   : 2022/11/10 15:17
# @Author : LOUIE
# @Desc   : to do something ...
from utils import logwrap
from case.position import login_pos
from case.lib.page import Page


class LoginPage(Page):

    def choose_env(self):
        self.click(login_pos.pre_env_pos)

    def click_ok(self):
        self.click(login_pos.ok_btn_pos)

    def transaction(self):
        self.choose_env()
        self.click_ok()






















