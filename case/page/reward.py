# @Time   : 2022/11/17 18:29
# @Author : LOUIE
# @Desc   : 掉落奖励
import re
from utils import logwrap, logerror, logstep
from case.position import reward_pos, outer_pos
from case.lib.page import Page
from case.page.outer import OuterPage
from case.lib.utils import assertion
from poco.exceptions import InvalidOperationException, PocoNoSuchNodeException


class RewardPage(Page):

    def __init__(self, poco_instance):
        super(RewardPage, self).__init__(poco_instance)
        self.outer_page = OuterPage(poco_instance)

    @logwrap('获取掉落奖励预览')
    def get_reward_preview(self):
        poss = self.poco(reward_pos.reward_icon_pos)
        reward_preview_list = []
        for pos in poss:
            pos.click()
            reward_preview_list.append(self.get_text(reward_pos.reward_name_pos))
            self.touch_optional_position()
        return reward_preview_list

    @logwrap('战斗已结束，获取战斗奖励')
    def get_battle_reward(self):
        poss = self.poco(nameMatches=reward_pos.battle_reward_pos)
        battle_reward_list = []
        for pos in poss:
            pos.click()

            reward_name = None
            if self.exists(reward_pos.reward_name_pos):
                reward_name = self.get_text(reward_pos.reward_name_pos)
            elif self.exists(reward_pos.lost_reward_name_pos):
                reward_name = self.get_text(reward_pos.lost_reward_name_pos)
            if reward_name not in battle_reward_list:
                battle_reward_list.append(reward_name)
                print(reward_name)
        return battle_reward_list

    @logwrap("执行滑动屏幕操作 ...")
    def swipe_top_to_bottom(self, direction='top'):
        top = [0.35, 0.2]
        bottom = [0.35, 0.8]
        if direction == 'top':
            self.poco.swipe(top, bottom, duration=0.1)
        else:
            self.poco.swipe(bottom, top, duration=0.1)

    def battle(self):
        self.outer_page.into_fight()
        self.outer_page.fighting_and_back_trans()

    def run_from_bottom_to_top(self, max_level_pos):
        """
        从下至上 运行当前副本下的所有关卡
        :param max_level_pos: 当前副本最大关卡数
        :return:
        """
        max_level = int(max_level_pos)
        current_level = 1
        while current_level <= max_level:
            self.sleep(1)
            poco_instance = self.poco(textMatches=str(f'^{current_level}$'))

            # 最大下滑6次，超过6次跳出循环
            index = 0
            while index < 6:
                if poco_instance.exists():
                    break
                self.swipe_top_to_bottom()
                index += 1
                continue

            # 存在点击位置超出屏幕的问题，下滑后再操作
            try:
                poco_instance.click()
            except (InvalidOperationException, PocoNoSuchNodeException):
                self.swipe_top_to_bottom()
                poco_instance.click()

            # 判断 准备通关关卡是否与选中关卡一致
            level_name = self.get_text(reward_pos.level_name_pos)
            level_number = re.search(r'\d+\.?\d*', level_name).group()
            if int(current_level) != int(level_number):
                self.swipe_top_to_bottom()
                poco_instance.click()

            logstep(f'当前选中关卡：{current_level}')
            self.battle()
            current_level += 1

    def run_from_top_to_bottom(self, max_level_pos):
        """
        从上至下 运行当前副本下的所有关卡
        :param max_level_pos: 当前副本最大关卡数
        :return:
        """
        max_level = int(max_level_pos)
        current_level = 10
        while current_level <= max_level:
            self.sleep(0.88)
            poco_instance = self.poco(textMatches=str(f'{current_level}'))
            poco_instance.click()

            start_energy = self.outer_page.get_current_energy_value()

            # 判断 准备通关关卡是否与选中关卡一致
            level_name = self.get_text(reward_pos.level_name_pos)
            level_number = re.search(r'\d+\.?\d*', level_name).group()
            # if int(current_level) != int(level_number):
            #     logerror(f'当前选中关卡：{current_level} 与 关卡名称：{level_name} 不匹配.')
            #     raise NameError(f'当前选中关卡：{current_level}， 关卡名称：{level_name}')

            logstep(f'当前选中关卡：{current_level}， 关卡名称：{level_name}')
            self.battle()

            end_energy = self.outer_page.get_current_energy_value()

            logstep(f'校验能量值消耗数值是否正确 ...')
            assertion.assert_less_equal(start_energy - end_energy, 10)

            reward_list = self.get_battle_reward()

            # 获取表格中的数据
            reward_config = ''
            reward_preview = ['金币', '体力']
            reward_preview.extend(reward_config)

            for reward in reward_list:
                assertion.assert_in(reward, reward_preview)

            current_level += 1

    def bina(self, instance_type, level_pos, *instances):
        self.outer_page.retry(instance_type)
        for instance in instances:
            self.click(instance)
            self.outer_page.enter_btn()
            self.run_from_bottom_to_top(level_pos)


if __name__ == '__main__':
    from case.lib.driver.unity_app import get_unity3d_poco_instance
    reward = RewardPage(get_unity3d_poco_instance())
    reward.bina(outer_pos.elemental_valley_pos, outer_pos.elemental_valley_level_pos, outer_pos.pyro_lord_pos)
    # reward.run_from_top_to_bottom(12)
    reward.get_battle_reward()









