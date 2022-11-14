# @Time   : 2022/11/10 15:17
# @Author : LOUIE
# @Desc   : to do something ...
from utils import logwrap
from case.position import login_pos


class LoginPage:

    def __init__(self, poco_instance):
        self.poco = poco_instance

    def choose_env(self):
        self.poco(login_pos.pre_env)

    def click_ok(self):
        pass

    def transaction(self):
        self.choose_env()






















