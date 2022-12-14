# @Time   : 2022/11/4 16:05
# @Author : LOUIE
# @Desc   : 固定视图

from utils import log
from tests.position import camera_pos
from tests.lib.page import Page


class CameraPage(Page):

    @log.wrap('打开据点情报')
    def open_pack(self):
        self.click(camera_pos.pack_pos)

    @log.wrap('打开背包')
    def open_pack(self):
        self.click(camera_pos.pack_pos)

    @log.wrap('打开行记')
    def open_pack(self):
        self.click(camera_pos.pack_pos)

    @log.wrap('打开英雄')
    def open_pack(self):
        self.click(camera_pos.pack_pos)

    @log.wrap('打开异界列车')
    def open_pack(self):
        self.click(camera_pos.pack_pos)

    @log.wrap('点击画面中心位置')
    def open_pack(self):
        self.poco.click([0.5, 0.5])
















