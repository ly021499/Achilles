# @Time   : 2022/11/21 16:16
# @Author : LOUIE
# @Desc   : 属性：体力、金币、钻石
from utils import logwrap, log
from tests.position import profile_pos
from tests.lib.page import Page
from airtest.core import api as air


class AttrPage(Page):

    @logwrap('点击体力')
    def click_strength(self):
        return self.click(profile_pos.strength_pos)

    @logwrap('点击金币')
    def click_coin(self):
        return self.click(profile_pos.coin_pos)

    @logwrap('点击钻石')
    def click_jewel(self):
        return self.click(profile_pos.jewel_pos)

    @logwrap('购买金币')
    def buy_coin(self):
        return self.click(profile_pos.buy_coin_pos)

    @logwrap('购买体力')
    def buy_strength(self):
        return self.click(profile_pos.buy_strength_pos)