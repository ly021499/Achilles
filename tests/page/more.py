# @Time   : 2022/11/18 9:40
# @Author : LOUIE
# @Desc   : 更多
from utils import logwrap
from tests.position import camera_pos, more_pos
from tests.lib.page import Page


class MorePage(Page):

    @logwrap('打开更多菜单')
    def open_more(self):
        self.click(camera_pos.more_pos)

    @logwrap('打开系统签到')
    def click_signed(self):
        self.click(more_pos.signed)

    @logwrap('打开等级奖励')
    def click_grade_reward(self):
        self.click(more_pos.grade_reward)


if __name__ == '__main__':
    from core.lib.driver.unity_window import get_unity_window_poco_instance
    page = MorePage(get_unity_window_poco_instance())
    # page.click_grade_reward()
    poco = get_unity_window_poco_instance()
    poco("SafeArea/MainNewUIMoreView(Clone)/GridView/Viewport/Content/Notice(Clone)").click()
