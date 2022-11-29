# @Time   : 2022/11/10 15:17
# @Author : LOUIE
# @Desc   : 副本
from utils import logwrap
from case.lib.page import Page


class InstancePage(Page):

    @logwrap('选择环境')
    def choose_env(self):
        self.click(pre_env_pos)

    @logwrap('点击确定')
    def click_confirm(self):
        self.click(confirm_btn_pos, sleep_interval=1)

    @logwrap('关闭公告')
    def close_note(self):
        self.click(close_note_pos)

    @logwrap('进入游戏')
    def enter_game(self):
        from case.lib.driver.android_app import get_android_poco_instance
        poco = get_android_poco_instance()
        poco(enter_game_pos).click()

    @logwrap("点击进入游戏")
    def click_enter(self):
        self.sleep(30)
        self.click(click_enter_pos)

    @logwrap("如果存在则关闭奖励页面")
    def close_reward_note(self):
        if self.exists(close_reward_pos):
            self.click(close_reward_pos)

    @logwrap("如果存在则关闭英雄页面")
    def close_hero_note(self):
        while self.exists(close_hero_note):
            self.click(close_hero_note)

    @logwrap("检查网络是否错误")
    def close_net_error(self):
        if self.exists(close_net_error):
            self.click(close_net_error)
        self.sleep(8)























