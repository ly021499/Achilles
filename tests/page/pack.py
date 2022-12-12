# @Time   : 2022/11/17 18:29
# @Author : LOUIE
# @Desc   : 背包
from utils import log
from tests.position import camera_pos
from tests.lib.page import Page


class PackPage(Page):

    @log.wrap('打开邮件')
    def open_pack(self):
        self.click(camera_pos.pack_pos)

    @log.wrap('使用道具')
    def use_props(self):
        self.click(camera_pos, sleep_interval=1)


if __name__ == '__main__':
    from tests.lib.driver.unity_window import get_unity_window_poco_instance
    page = PackPage(get_unity_window_poco_instance())

    page.open_pack()
