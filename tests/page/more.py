# @Time   : 2022/11/18 9:40
# @Author : LOUIE
# @Desc   : 更多
from utils import log
from tests.position import camera_pos, more_pos
from tests.lib.page import Page


class MorePage(Page):

    @log.wrap('打开更多菜单')
    def open_more(self):
        self.click(camera_pos.more_pos)

    @log.wrap('打开系统签到')
    def click_signed(self):
        self.click(more_pos.signed)

    @log.wrap('打开等级奖励')
    def click_grade_reward(self):
        self.click(more_pos.grade_reward)

