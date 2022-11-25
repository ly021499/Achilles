# @Time   : 2022/11/22 17:00
# @Author : LOUIE
# @Desc   : 飞空艇外围
import time

from utils import logwrap, logstep
from case.position import outer_pos, profile_pos
from case.lib.page import Page


"""
前置操作：
1. 新增秒杀英雄薇薇安
2. 每个副本战斗英雄出厂配置需要设置好薇薇安
3. 虚影殿堂中的副本顺序需要调整
"""


class OuterPage(Page):

    @logwrap('副本入口 - 塔尔魔术工坊')
    def magic_workshop(self):
        return self.click(outer_pos.magic_workshop_pos)

    def retry(self, pos):
        # 防止进入错误的副本，增加重试机制，最多五次
        count = 0
        while count < 5:
            self.click(pos)
            if not self.exists(pos):
                self.close_page()
                count += 1
                continue
            return

    @logwrap('副本入口 - 虚影殿堂')
    def the_shadow_keep(self):
        return self.retry(outer_pos.the_shadow_keep_pos)

    @logwrap('副本入口 - 贪婪禁地')
    def forbidden_sector(self):
        return self.retry(outer_pos.forbidden_sector_pos)

    @logwrap('副本入口 - 茫然遗迹')
    def lost_sector(self):
        return self.retry(outer_pos.lost_sector_pos)

    @logwrap('副本入口 - 苍穹之城')
    def sky_city(self):
        return self.retry(outer_pos.sky_city_pos)

    @logwrap('副本入口 - 元素峡谷')
    def elemental_valley(self):
        return self.retry(outer_pos.elemental_valley_pos)

    def get_page_title(self):
        text = self.get_text(outer_pos.page_title_pos)
        logstep(f'获取副本标题: {text}')
        return text

    @logwrap('返回上一级页面')
    def close_page(self):
        self.click(outer_pos.close_page_pos)

    @logwrap('进入副本详情页')
    def enter_btn(self):
        self.click(outer_pos.enter_btn_pos)

    @logwrap('进入战斗配置页面')
    def into_fight(self):
        self.click(outer_pos.into_fight_pos)

    @logwrap('开始战前配置')
    def choose_superheroes(self):
        self.click(outer_pos.wwa_hero_pos)
        if self.exists(outer_pos.hero_name_pos):
            self.click(outer_pos.close_hero_page_pos)
            self.drag_to(outer_pos.wwa_hero_pos, outer_pos.play_hero_pos)

    @logwrap('战斗一触即发...')
    def fighting(self):
        self.click(outer_pos.fighting_pos)

    def fighting_and_back_trans(self):
        self.fighting()
        logstep('战斗开始，请耐心等待战斗结束 ...')
        self.wait_for_appearance(outer_pos.continue_pos, timeout=25)
        logstep('战斗结束了，获得胜利 ...')
        while self.exists(outer_pos.continue_pos):
            self.touch_optional_position()

    def play_trans(self, *challenges):
        for challenge in challenges:
            if self.exists(challenge):

                self.click(challenge)
            # 判断是否是虚影殿堂副本，需要判断哪些副本可以进入，否则跳过
            if self.exists(outer_pos.the_shadow_keep_pos):
                if not self.exists(outer_pos.enter_btn_pos):
                    continue
            logstep(f"选择关卡：{str(challenge).split('=')[1]} ...")
            # outer.choose_superheroes()
            self.enter_btn()
            self.into_fight()
            self.fighting_and_back_trans()
            if self.exists(outer_pos.into_fight_pos):
                self.close_page()
        self.close_page()
        logstep('副本闯关完成 ...')

    @logwrap('刷副本：茫然遗迹')
    def lost_sector_trans(self):
        self.lost_sector()
        self.play_trans(outer_pos.bihna_pos, outer_pos.chester_pos,
                        outer_pos.guule_pos, outer_pos.papillaire_pos)

    @logwrap('刷副本：元素峡谷')
    def elemental_valley_trans(self):
        self.elemental_valley()
        self.play_trans(outer_pos.frost_lord_pos, outer_pos.pyro_lord_pos, outer_pos.gale_lord_pos,
                        outer_pos.stone_lord_pos)

    @logwrap('刷副本：贪婪禁地')
    def forbidden_sector_trans(self):
        self.forbidden_sector()
        self.play_trans(outer_pos.potion_pos, outer_pos.the_gold_pos)

    @logwrap('刷副本：虚影殿堂')
    def the_shadow_keep_trans(self):
        self.the_shadow_keep()
        self.play_trans(outer_pos.mage_pos, outer_pos.defender_pos)

    def find(self):
        if self.exists(outer_pos.the_shadow_keep_pos):
            if self.exists(outer_pos.fighter_pos) and self.exists(outer_pos.enter_btn_pos):
                self.click(outer_pos.enter_btn_pos)


if __name__ == '__main__':
    from case.lib.driver.unity_window import get_unity_window_poco_instance
    outer = OuterPage(get_unity_window_poco_instance())
    outer.elemental_valley_trans()
    outer.forbidden_sector_trans()
    outer.lost_sector_trans()
    outer.the_shadow_keep_trans()





