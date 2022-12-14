# @Time   : 2022/11/17 18:29
# @Author : LOUIE
# @Desc   : 掉落奖励
from utils import log
from utils.parser import get_reward_config, get_target_reward_data
from tests.position.outer_pos import *
from tests.lib.page import Page
from tests.page.outer import OuterPage
from tests.lib.utils import assertion


class RewardPage(Page):

    def __init__(self, poco_instance):
        super(RewardPage, self).__init__(poco_instance)
        self.outer_page = OuterPage(poco_instance)

    def assert_rewards(self, instance, level_name, battle_reward_list):
        """校验奖励物品是否与配置一致"""
        # 获取表格中的数据
        reward_config = get_reward_config(instance)
        preview_reward_list = get_target_reward_data(reward_config, level_name)
        preview_reward_list.extend(['金币', '钻石', '普通核铁'])

        for reward_ in battle_reward_list:
            if reward_[0] == '常规':
                assertion.assert_in(reward_[1], preview_reward_list)
            elif reward_[0] == '首次':
                assertion.assert_in(reward_[1], preview_reward_list)
            else:
                log.step(f'惊喜掉落物品：{reward_}')

    def assert_energy(self, battle_reward_list, actual, expected):
        """校验能量消耗是否正确，存在奖品中有体力返回的情况，所以需要增加判断"""
        log.step(f'校验能量值消耗数值是否正确 ...')
        if '体力' in str(battle_reward_list):
            assertion.assert_less_equal(actual, 0)
        else:
            assertion.assert_less_equal(actual, expected)

    def get_battle_reward_list(self):
        """获取战斗后的奖励"""
        self.outer_page.click_continue()
        battle_reward_list = self.outer_page.get_battle_reward()
        self.outer_page.always_click_continue()
        return battle_reward_list

    @log.wrap('降序执行 当前副本下的所有关卡')
    def execute_instance_in_desc(self, max_level: int, instance: str, consume_energy: int):
        """
        降序执行 当前副本下的所有关卡
        :param max_level: 当前副本最大关卡数
        :param instance: 副本名称
        :param consume_energy: 副本消耗
        :return:
        """
        current_level = self.outer_page.search_current_level_number()
        while current_level <= int(max_level):
            self.sleep(1)
            self.click(f"textMatches={str(current_level)}")

            # 获取能量初始值和结束值、战斗奖励
            start_energy = self.outer_page.get_current_energy_value()
            level_name = self.outer_page.get_current_level_name()
            self.outer_page.enter_btn()
            self.outer_page.fighting()
            battle_reward_list = self.get_battle_reward_list()
            end_energy = self.outer_page.get_current_energy_value()
            self.outer_page.check_current_page()
            current_level += 1

            # 断言体力消耗和战斗奖励
            self.assert_energy(battle_reward_list, start_energy - end_energy, consume_energy)
            if battle_reward_list is not False:
                self.assert_rewards(instance, level_name, battle_reward_list)

        self.outer_page.back_to_outer()

    def common_brush_instance(self, instance_type, max_level, instance, consume_energy):
        """通用 Rush 副本的方法"""
        self.outer_page.retry(instance_type)
        sheet_name = instance_type.split('=')[1]
        self.click(instance)
        self.outer_page.enter_btn()
        self.execute_instance_in_desc(max_level, sheet_name, consume_energy)

    def check_level(self, current_level: str):
        """纠正关卡定位"""
        poco_instance = self.poco(textMatches=str(current_level))
        if current_level == 10:
            poco_instance = self.poco(textMatches=str(current_level))[1]
        if current_level == 50:
            poco_instance = self.poco(textMatches=str(current_level))[1]
        return poco_instance

    def brush_sky_city(self, current_level, max_level):
        """Rush 苍穹之城副本"""
        self.outer_page.sky_city()
        while current_level <= int(max_level):
            # 等待一秒点击更稳定点
            self.sleep(1)
            poco_instance = self.check_level(str(current_level))
            start_energy = self.outer_page.get_current_energy_value()
            poco_instance.click()
            level_name = self.outer_page.get_current_level_name()

            # 获取能量初始值和结束值、战斗奖励
            self.click(Sky.battle_btn_pos)
            self.outer_page.fighting()
            battle_reward_list = self.get_battle_reward_list()
            end_energy = self.outer_page.get_current_energy_value()

            # 断言战斗奖励和能量值消耗
            self.assert_energy(start_energy - end_energy, Sky.sky_energy_pos)
            self.assert_rewards('苍穹之城', level_name, battle_reward_list)

            current_level += 1

        self.outer_page.back_to_outer()

    def brush_the_shadow(self):
        self.common_brush_instance(
            Shadow.shadow_keep_pos, Shadow.shadow_level_pos,
            Shadow.first_instance_pos, Shadow.shadow_energy_pos
        )


if __name__ == '__main__':
    from tests.lib.driver.unity_app import get_unity3d_poco_instance
    reward = RewardPage(get_unity3d_poco_instance())
    # reward.brush_instance(
    #     Element.element_valley_pos, Element.element_level_pos,
    #     Element.fire_element_pos, Element.element_energy_pos
    # )
    # reward.brush_sky_city(Sky.sky_level_pos, Sky.sky_energy_pos)
    # reward.brush_the_shadow()
    # reward.brush_sky_city(28, 30)
    reward.get_battle_reward_list()






