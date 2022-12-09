# -*- coding: utf-8 -*-
# @Time   : 2022/11/22 17:00
# @Author : LOUIE
# @Desc   : 飞空艇外围
import re
from utils import logwrap, logstep
from tests.position.outer_pos import *
from tests.lib.page import Page


class OuterPage(Page):
    """
    前置操作：
    1. 新增秒杀英雄薇薇安
    2. 每个副本战斗英雄出厂配置需要设置好薇薇安
    3. 虚影殿堂中的副本顺序需要调整
    """

    @logwrap('副本入口 - 塔尔魔术工坊')
    def magic_workshop(self):
        return self.click(Magic.magic_workshop_pos)

    @logwrap('副本入口 - 虚影殿堂')
    def the_shadow_keep(self):
        return self.retry(Shadow.shadow_keep_pos)

    @logwrap('副本入口 - 贪婪禁地')
    def forbidden_sector(self):
        return self.retry(Forbid.forbidden_sector_pos)

    @logwrap('副本入口 - 茫然遗迹')
    def lost_sector(self):
        return self.retry(Lost.lost_sector_pos)

    @logwrap('副本入口 - 苍穹之城')
    def sky_city(self):
        return self.retry(Sky.sky_city_pos)

    @logwrap('副本入口 - 元素峡谷')
    def element_valley(self):
        return self.retry(Element.element_valley_pos)

    def get_page_title(self):
        text = self.get_text(Public.page_title_pos)
        logstep(f'当前页面标题: {text}')
        return text

    @logwrap('返回上一级页面')
    def close_page(self):
        self.get_page_title()
        self.click(Public.close_page_pos)

    @logwrap('回到 飞空艇外围')
    def back_to_outer(self):
        if self.exists(Public.close_page_pos):
            self.close_page()
        if self.exists(Public.close_page_pos):
            self.close_page()

    @logwrap('进入副本详情页，选择关卡')
    def enter_btn(self):
        self.click(Public.enter_btn_pos)

    @logwrap('进入战斗配置页面')
    def into_battle(self):
        self.click(Public.into_battle_pos)

    def get_current_level_name(self):
        level_name = self.get_text(Public.level_name_pos)
        logstep(f'当前默认选择关卡: {level_name}')
        return level_name

    def search_current_level_number(self):
        string = self.get_current_level_name()
        expr = r'\d+'
        match_obj = re.search(expr, string)
        if match_obj.group():
            return int(match_obj.group())
        return string

    @logwrap('开始战前配置')
    def choose_superheroes(self):
        self.click(Public.wwa_hero_pos)
        if self.exists(Public.hero_name_pos):
            self.click(Public.close_hero_page_pos)
            self.drag_to(Public.wwa_hero_pos, Public.play_hero_pos)

    @logwrap('点击任意位置继续')
    def click_continue(self):
        while self.exists(Public.continue_pos):
            self.click(Public.continue_pos)

    def fighting(self):
        self.click(Public.fighting_pos)
        logstep('战斗一触即发，请耐心等待战斗结束..')
        self.wait_for_appearance(Public.continue_pos, timeout=60)
        logstep('战斗结束了，获得胜利 ...')
        self.sleep(1)

    def get_current_energy_value(self):
        energy_text = self.get_text(Public.energy_pos)
        current_energy_value = energy_text.split('/')[0]
        logstep(f'当前能量值：{energy_text}')
        return int(current_energy_value)

    @logwrap('校验副本是否存在')
    def exists_instance(self, pos):
        if self.exists(pos):
            self.click(pos)
        else:
            logstep(f"副本: {str(pos).split('=')[1]} 不存在，请检查错误")
            raise ModuleNotFoundError(f"副本: {str(pos).split('=')[1]} 不存在，请检查错误")

    def retry(self, pos):
        # 防止进入错误的副本，增加重试机制，最多五次
        logstep(f"准备进入副本：{str(pos).split('=')[1]}")
        count = 0
        while count < 7:
            self.click(pos)
            if not self.exists(pos):
                self.close_page()
                count += 1
                logstep(f"副本进错了，准备重新进入 ...")
                continue
            return


if __name__ == '__main__':
    from tests.lib.driver.unity_app import get_unity3d_poco_instance
    outer = OuterPage(get_unity3d_poco_instance())
    outer.close_page()






