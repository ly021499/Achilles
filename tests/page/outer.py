# -*- coding: utf-8 -*-
# @Time   : 2022/11/22 17:00
# @Author : LOUIE
# @Desc   : 飞空艇外围
import re
from utils import log
from tests.position.outer_pos import *
from tests.lib.page import Page


class OuterPage(Page):
    """
    前置操作：
    1. 新增秒杀英雄薇薇安
    2. 每个副本战斗英雄出厂配置需要设置好薇薇安
    3. 通关主线任务
    4. 药水研究所需要通关深处洞穴
    """

    @log.wrap('副本入口 - 塔尔魔术工坊')
    def magic_workshop(self):
        return self.click(Magic.magic_workshop_pos)

    @log.wrap('副本入口 - 虚影殿堂')
    def the_shadow_keep(self):
        self.sleep(0.68)
        return self.retry(Shadow.shadow_keep_pos)

    @log.wrap('副本入口 - 贪婪禁地')
    def forbidden_sector(self):
        return self.retry(Forbid.forbidden_sector_pos)

    @log.wrap('副本入口 - 茫然遗迹')
    def lost_sector(self):
        return self.retry(Lost.lost_sector_pos)

    @log.wrap('副本入口 - 苍穹之城')
    def sky_city(self):
        return self.retry(Sky.sky_city_pos)

    @log.wrap('副本入口 - 元素峡谷')
    def element_valley(self):
        return self.retry(Element.element_valley_pos)

    def get_page_title(self):
        """获取当前页面标题"""
        text = self.get_text(Public.page_title_pos)
        log.step(f'当前页面标题: {text}')
        return text

    @log.wrap('返回上一级页面')
    def close_page(self):
        self.get_page_title()
        self.click(Public.close_page_pos)

    @log.wrap('回到 飞空艇外围')
    def back_to_outer(self):
        if self.exists(Public.close_page_pos):
            self.close_page()
        if self.exists(Public.close_page_pos):
            self.close_page()

    @log.wrap('进入副本详情页，选择关卡')
    def enter_btn(self):
        self.click(Public.enter_btn_pos)

    @log.wrap('进入战斗配置页面')
    def into_battle(self):
        self.click(Public.into_battle_pos)

    def get_current_level_name(self):
        """获取当前关卡名称"""
        level_name = self.get_text(Public.level_name_pos)
        log.step(f'当前默认选择关卡: {level_name}')
        return level_name

    def search_current_level_number(self):
        """获取当前关卡名称中的数字"""
        string = self.get_text(Public.level_name_pos)
        expr = r'\d+'
        match_obj = re.search(expr, string)
        if match_obj.group():
            return int(match_obj.group())
        return string

    @log.wrap('开始战前配置')
    def choose_superheroes(self):
        self.click(Public.wwa_hero_pos)
        if self.exists(Public.hero_name_pos):
            self.click(Public.close_hero_page_pos)
            self.drag_to(Public.wwa_hero_pos, Public.play_hero_pos)

    @log.wrap('持续点击任意位置继续')
    def always_click_continue(self):
        self.save_battle_setting()
        while self.exists(Public.continue_pos):
            self.click(Public.continue_pos)

    @log.wrap('点击一下任意位置继续')
    def click_continue(self):
        self.save_battle_setting()
        if self.exists(Public.continue_pos):
            self.click(Public.continue_pos)

    def check_current_page(self):
        if self.get_page_title() == '贪婪禁地':
            log.step('检查当前页面是否在副本详情页，主要针对贪婪禁地-药水研炼所')
            self.enter_btn()

    def get_reward_preview(self):
        """获取战斗奖励预览"""
        reward_preview_list = []
        rewards_preview = self.poco(Reward.reward_icon_pos)
        for reward_preview in rewards_preview:
            reward_type = reward_preview.offspring(Reward.reward_type_pos).get_text()
            reward_preview.click()
            reward_preview_list.append((reward_type, self.get_text(Reward.reward_name_pos)))
        log.step(f'获取战斗奖励预览: {reward_preview_list}')
        return reward_preview_list

    def get_battle_reward(self):
        """获取战斗掉落的奖励"""
        # 黄金谷通关所有关卡后，不获得奖励
        if not self.poco(nameMatches=Reward.battle_reward_pos).exists():
            return False

        battle_reward_list = []
        # 拿到多个元素定位，遍历获取战斗奖励物品
        battle_rewards = self.poco(nameMatches=Reward.battle_reward_pos)
        for battle_reward in battle_rewards:
            reward_type = battle_reward.offspring(Reward.reward_type_pos).get_text()
            battle_reward.click()

            reward_name = None
            if self.exists(Reward.reward_name_pos):
                reward_name = self.get_text(Reward.reward_name_pos)
            elif self.exists(Reward.lost_reward_name_pos):
                reward_name = self.get_text(Reward.lost_reward_name_pos)
                battle_reward.click()
            battle_reward_list.append((reward_type, reward_name))
        log.step(f'战斗结束了，获取战斗奖励: {battle_reward_list}')

        return battle_reward_list

    def fighting(self):
        """战斗"""
        self.click(Public.fighting_pos)
        log.step('战斗一触即发，请耐心等待战斗结束..')
        self.wait_for_appearance(Public.continue_pos, timeout=100)
        log.step('战斗结束了，获得胜利 ...')
        self.sleep(1)

    def get_current_energy_value(self):
        """获取当前能量值"""
        energy_text = self.get_text(Public.energy_pos)
        current_energy_value = energy_text.split('/')[0]
        log.step(f'当前能量值：{energy_text}')
        return int(current_energy_value)

    @log.wrap('校验副本是否存在')
    def check_exists_instance(self, pos):
        if self.exists(pos):
            self.click(pos)
        else:
            log.step(f"副本: {str(pos).split('=')[1]} 不存在，请检查错误")
            raise ModuleNotFoundError(f"副本: {str(pos).split('=')[1]} 不存在，请检查错误")

    def save_battle_setting(self):
        if self.exists(Battle.is_save_title_pos):
            self.click(Battle.save_btn_pos)
            log.step('保存本次战斗设置')

    def retry(self, pos):
        """防止进入错误的副本，增加重试机制，最多五次"""
        log.step(f"准备进入副本：{str(pos).split('=')[1]}")
        count = 1
        while count < 10:
            self.click(pos)
            if not self.exists(pos):
                self.close_page()
                count += 1
                log.step(f"副本进错了，准备重新进入 ...")
                continue
            return


if __name__ == '__main__':
    from tests.lib.driver.unity_app import get_unity3d_poco_instance
    outer = OuterPage(get_unity3d_poco_instance())
    outer.get_battle_reward()






