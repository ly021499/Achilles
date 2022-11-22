# @Time   : 2022/11/22 17:00
# @Author : LOUIE
# @Desc   : 飞空艇外围
from utils import logwrap, log
from case.position import outer_pos, profile_pos
from case.lib.page import Page


class OuterPage(Page):

    @logwrap('副本入口 - 塔尔魔术工坊')
    def magic_workshop(self):
        return self.click(outer_pos.magic_workshop_pos)

    @logwrap('副本入口 - 虚影殿堂')
    def hall_of_shadow(self):
        return self.click(outer_pos.hall_of_shadow_pos)

    @logwrap('副本入口 - 贪婪禁地')
    def land_of_greed(self):
        return self.click(outer_pos.land_of_greed_pos)

    @logwrap('副本入口 - 茫然遗迹')
    def land_of_greed(self):
        return self.click(outer_pos.lost_relics_pos)

    @logwrap('副本入口 - 苍穹之城')
    def firmament_city(self):
        return self.click(outer_pos.firmament_city_pos)

    @logwrap('副本入口 - 元素峡谷')
    def valley_of_elements(self):
        return self.click(outer_pos.valley_of_elements_pos)

    def get_page_title(self):
        text = self.get_text(outer_pos.page_title_pos)
        log.info(f'获取副本标题: {text}')
        return text

    @logwrap('关闭页面')
    def close_page(self):
        self.click(outer_pos.close_page_pos)

    @logwrap('进入副本')
    def enter_btn(self):
        self.click(outer_pos.enter_btn_pos)


if __name__ == '__main__':
    from case.lib.driver.unity_window import get_unity_window_poco_instance
    outer = OuterPage(get_unity_window_poco_instance())
    # outer.get_page_title()
    outer.enter_btn()





