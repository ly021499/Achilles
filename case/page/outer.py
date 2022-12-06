# -*- coding: utf-8 -*-
# @Time   : 2022/11/22 17:00
# @Author : LOUIE
# @Desc   : 飞空艇外围

from utils import logwrap, logstep
from case.position import outer_pos, profile_pos
from case.lib.page import Page
from case.lib.utils import commands as cmd, assertion

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
        return reward_preview_list

    @logwrap('战斗已结束，获取战斗奖励')
    def get_battle_reward(self):
        poss = self.poco(nameMatches=outer_pos.battle_reward_pos)
        battle_reward_list = []
        for pos in poss:
            pos.click()

            reward_name = None
            if self.exists(outer_pos.reward_name_pos):
                reward_name = self.get_text(outer_pos.reward_name_pos)
            elif self.exists(outer_pos.lost_reward_name_pos):
                reward_name = self.get_text(outer_pos.lost_reward_name_pos)
            if reward_name not in battle_reward_list:
                battle_reward_list.append(reward_name)
                print(reward_name)
        return battle_reward_list

    @logwrap('战斗一触即发...')
    def fighting(self):
        self.click(outer_pos.fighting_pos)

    def fighting_and_back_trans(self):
        self.fighting()
        logstep('战斗开始，请耐心等待战斗结束 ...')
        self.wait_for_appearance(outer_pos.continue_pos, timeout=60)
        logstep('战斗结束了，获得胜利 ...')
        self.sleep(0.68)
        self.click(outer_pos.continue_pos)

        battle_reward_list = self.get_battle_reward()

        while self.exists(outer_pos.continue_pos):
            self.click(outer_pos.continue_pos)
            logstep('点击任意位置继续 ...')
        return battle_reward_list

    @logwrap('刷副本：茫然遗迹')
    def lost_sector_trans(self):
        self.lost_sector()
        self.play_trans(outer_pos.bihna_pos, outer_pos.chester_pos,
                        outer_pos.guule_pos, outer_pos.papillaire_pos)

    @logwrap('刷副本：元素峡谷')
    def elemental_valley_trans(self):
        self.elemental_valley()
        self.play_trans(outer_pos.frost_lord_pos, outer_pos.pyro_lord_pos,
                        outer_pos.gale_lord_pos, outer_pos.stone_lord_pos)

    @logwrap('刷副本：贪婪禁地')
    def forbidden_sector_trans(self):
        self.forbidden_sector()
        self.play_trans(outer_pos.the_gold_pos, )

    @logwrap('刷副本：虚影殿堂')
    def the_shadow_keep_trans(self):
        self.the_shadow_keep()
        self.play_trans(outer_pos.mage_pos, outer_pos.support_pos)

    def get_current_energy_value(self):
        energy_text = self.get_text(outer_pos.energy_pos)
        current_energy_value = energy_text.split('/')[0]
        logstep(f'当前能量值：{energy_text}')
        return int(current_energy_value)

    def is_golden_key(self, pid: int = 55561040):
        """
        判断能否挑战当前副本，例如：是否含有挑战次数
        """
        if self.exists(outer_pos.the_gold_pos):
            text = self.get_text(outer_pos.golden_key_count_pos)
            logstep(f'获取当前金币钥匙数量：{text}')
            if int(text) < 1:
                cmd.add_value(pid, 10021, 99)
                logstep("增加金币钥匙数量: 99")
            self.is_golden_key = self.get_text(outer_pos.golden_key_count_pos)

    def _find(self):
        if self.exists(outer_pos.the_shadow_keep_pos):
            if self.exists(outer_pos.fighter_pos) and self.exists(outer_pos.enter_btn_pos):
                self.click(outer_pos.enter_btn_pos)

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

            # 判断是否有金币钥匙，如果没有则增加
            self.is_golden_key()

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

    def verify_energy_consumption_of_lost_sector(self):
        """
        验证<茫然遗迹>的能量消耗值：10
        """
        self.lost_sector()
        self.play_trans(outer_pos.bihna_pos)
        assertion.assert_less_equal(self.start_energy - self.end_energy, 10)

    def verify_energy_consumption_of_the_shadow_keep(self):
        """
        验证<虚影殿堂>的能量消耗值：10
        """
        self.the_shadow_keep()
        self.play_trans(outer_pos.mage_pos)
        assertion.assert_equal(self.start_energy - self.end_energy, 10)

    def verify_energy_consumption_of_potion(self):
        """
        验证<贪婪禁地-药水研究所>的能量消耗值：10
        """
        self.forbidden_sector()

        self.play_trans(outer_pos.potion_pos)

        assertion.assert_equal(self.start_energy - self.end_energy, 10)

    def verify_energy_consumption_of_the_gold(self):
        """
        验证<贪婪禁地-黄金谷>的能量消耗值：1 key
        """
        self.forbidden_sector()
        self.click(outer_pos.the_gold_pos)
        logstep(f"选择关卡：{str(outer_pos.the_gold_pos).split('=')[1]} ...")
        self.enter_btn()

        # 判断是否有金币钥匙，如果没有则增加
        self.is_golden_key()

        start_energy = self.get_current_energy_value()

        # outer.choose_superheroes()

        self.into_fight()
        self.fighting_and_back_trans()

        end_energy = self.get_current_energy_value()
        assertion.assert_equal(start_energy - end_energy, 1)

        if self.exists(outer_pos.into_fight_pos):
            self.close_page()

        self.close_page()
        logstep('副本闯关完成 ...')

    def verify_energy_consumption_of_elemental_valley(self):
        """
        验证<元素峡谷>的能量消耗值：15
        """
        self.elemental_valley()
        self.play_trans(outer_pos.frost_lord_pos)
        assertion.assert_equal(self.start_energy - self.end_energy, 15)

    def verify_energy_consumption_of_sky_city(self):
        """
        验证<苍穹之城>的能量消耗值是否正确
        """
        raise NotImplementedError


if __name__ == '__main__':

    from case.lib.driver.unity_app import get_unity3d_poco_instance
    outer = OuterPage(get_unity3d_poco_instance())
    v = outer.exists(outer_pos.continue_pos)
    print(v)
    outer.click(outer_pos.continue_pos)
    # outer.lost_sector_trans()
    # outer.fighting_and_back_trans()
    # outer.touch_optional_position()
    # outer.verify_energy_consumption_of_the_shadow_keep()
    # outer.verify_energy_consumption_of_potion()
    # outer.verify_energy_consumption_of_elemental_valley()
    # outer.verify_energy_consumption_of_the_gold()






