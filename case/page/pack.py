# @Time   : 2022/11/17 18:29
# @Author : LOUIE
# @Desc   : to do something ...
from utils import logwrap
from case.position import camera_pos
from case.lib.page import Page


class PackPage(Page):

    @logwrap('打开邮件')
    def open_pack(self):
        self.click(camera_pos.pack_pos)

    @logwrap('使用道具')
    def use_props(self):
        self.click(camera_pos, sleep_interval=1)


if __name__ == '__main__':
    from case.lib.driver.unity_window import get_unity_window_poco_instance
    page = PackPage(get_unity_window_poco_instance())

    page.open_pack()
