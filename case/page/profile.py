# @Time   : 2022/11/17 18:29
# @Author : LOUIE
# @Desc   : to do something ...
from utils import logwrap, log
from case.position import camera_pos, profile_pos
from case.lib.page import Page
from airtest.core import api as air
from utils import factory


class ProfilePage(Page):

    @logwrap('打开头像')
    def open_avatar(self):
        self.click(camera_pos.avatar_pos)

    @logwrap('修改昵称')
    def rename(self):
        self.click(profile_pos.rename_btn_pos)

    @logwrap('输入新的昵称')
    def input_nickname(self):
        self.click(profile_pos.nickname_input_pos)
        air.text(factory.random_name())

    def get_prompt_text(self):
        text = self.get_text(profile_pos.prompt_text_pos)
        log.info(f'📣 📣 📣 operation: 获取提示文本: {text}')
        return text

    @logwrap('确认按钮')
    def ensure(self):
        self.click(profile_pos.ensure_btn_pos)

    @logwrap('点击体力')
    def click_strength(self):
        self.click(profile_pos.strength_pos)

    @logwrap('点击金币')
    def click_coin(self):
        self.click(profile_pos.coin_pos)

    @logwrap('点击钻石')
    def click_jewel(self):
        self.click(profile_pos.jewel_pos)

    @logwrap('购买金币')
    def buy_coin(self):
        self.click(profile_pos.buy_coin_pos)

    @logwrap('购买体力')
    def buy_strength(self):
        self.click(profile_pos.buy_strength_pos)


if __name__ == '__main__':
    from case.lib.driver.unity_window import get_unity_window_poco_instance
    page = ProfilePage(get_unity_window_poco_instance())
    page.open_avatar()
    page.rename()
    page.input_nickname()
    page.ensure()
    # page.get_prompt_text()
    # page.ensure()
