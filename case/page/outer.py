# -*- coding: utf-8 -*-
# @Time   : 2022/11/22 17:00
# @Author : LOUIE
# @Desc   : 飞空艇外围

from utils import logwrap, logstep
from case.position import outer_pos
from case.lib.page import Page


class OuterPage(Page):
    """
    前置操作：
    1. 新增秒杀英雄薇薇安
    2. 每个副本战斗英雄出厂配置需要设置好薇薇安
    3. 虚影殿堂中的副本顺序需要调整
    """

    @logwrap('副本入口 - 塔尔魔术工坊')
    def magic_workshop(self):
        return self.click(outer_pos.magic_workshop_pos)

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

    @logwrap('获取掉落奖励预览')
    def get_reward_preview(self):
        poss = self.poco(outer_pos.reward_icon_pos)
        reward_preview_list = []
        for pos in poss:
            pos.click()
            reward_preview_list.append(self.get_text(outer_pos.reward_name_pos))
            self.touch_optional_position()
        logstep(f'掉落奖励预览: {reward_preview_list}')
        return reward_preview_list

    @logwrap('战斗已结束，获取战斗奖励')
    def get_battle_reward(self):
        poss = self.poco(nameMatches=outer_pos.battle_reward_pos)

        reward_list = []
        label_list = []
        for pos in poss:
            reward_type = pos.offspring(outer_pos.reward_type_pos).get_text()
            label_list.append(reward_type)
            pos.click()
            reward_name = None
            if self.exists(outer_pos.reward_name_pos):
                reward_name = self.get_text(outer_pos.reward_name_pos)
            elif self.exists(outer_pos.lost_reward_name_pos):
                reward_name = self.get_text(outer_pos.lost_reward_name_pos)
                pos.click()
            if reward_name not in reward_list:
                reward_list.append(reward_name)

        battle_reward_list = list(zip(label_list, reward_list))
        logstep(f'战斗奖励: {battle_reward_list}')

        return battle_reward_list

    @logwrap('点击任意位置继续 ...')
    def click_continue(self):
        while self.exists(outer_pos.continue_pos):
            self.click(outer_pos.continue_pos)

    def fighting_and_back_trans(self):
        logstep('战斗一触即发 ...')
        self.click(outer_pos.fighting_pos)
        logstep('战斗开始，请耐心等待战斗结束 ...')
        self.wait_for_appearance(outer_pos.continue_pos, timeout=60)
        logstep('战斗结束了，获得胜利 ...')
        self.sleep(0.68)
        self.click_continue()
        self.sleep(0.88)
        battle_reward_list = self.get_battle_reward()

        self.click_continue()

        return battle_reward_list

    def get_current_energy_value(self):
        energy_text = self.get_text(outer_pos.energy_pos)
        current_energy_value = energy_text.split('/')[0]
        logstep(f'当前能量值：{energy_text}')
        return int(current_energy_value)

    @logwrap('校验副本是否存在 ...')
    def exists_instance(self, instance):
        if self.exists(instance):
            self.click(instance)
        else:
            logstep('副本不存在，请检查错误')
            raise ModuleNotFoundError('副本不存在，请检查错误')

    def play_trans(self, *instances):
        for instance in instances:

            self.exists_instance(instance)

            # 判断是否是虚影殿堂副本，需要判断哪些副本可以进入，否则跳过
            if self.exists(outer_pos.the_shadow_keep_pos):
                if not self.exists(outer_pos.enter_btn_pos):
                    continue

            self.start_energy = self.get_current_energy_value()

            logstep(f"选择关卡：{str(instance).split('=')[1]} ...")
            # outer.choose_superheroes()

            self.enter_btn()

            self.into_fight()
            self.fighting_and_back_trans()

            if self.exists(outer_pos.into_fight_pos):
                self.close_page()

            self.end_energy = self.get_current_energy_value()

        self.close_page()
        logstep('副本闯关完成 ...')

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


if __name__ == '__main__':
    from case.lib.driver.unity_app import get_unity3d_poco_instance
    outer = OuterPage(get_unity3d_poco_instance())
    outer.get_battle_reward()






