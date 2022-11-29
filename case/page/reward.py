# @Time   : 2022/11/17 18:29
# @Author : LOUIE
# @Desc   : 掉落奖励
import re

from utils import logwrap, log
from case.position import reward_pos
from case.lib.page import Page
from case.page.outer import OuterPage
from airtest.core import api as air


class RewardPage(Page):

    def __init__(self, poco_instance):
        super(RewardPage, self).__init__(poco_instance)
        self.outer_page = OuterPage(poco_instance)

    @logwrap('先获取掉落奖励预览')
    def get_reward_preview(self):
        poss = self.poco(reward_pos.reward_icon_pos)
        reward_preview_list = []
        for pos in poss:
            pos.click()
            reward_preview_list.append(self.get_text(reward_pos.reward_name_pos))
            self.touch_optional_position()
        return reward_preview_list

    @logwrap('战斗结束后再获取战斗奖励结果')
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

        return battle_reward_list

    def xunhuan(self):
        current_level = int(reward_pos.lost_level_pos)
        while current_level > 0:
            poco_instance = self.poco(textMatches=str(current_level))
            if poco_instance.exists():
                poco_instance.click()
                level_name = self.get_text(reward_pos.level_name_pos)
                level_number = re.search(r'\d+\.?\d*', level_name).group()
                if int(current_level) != int(level_number):
                    self.poco.swipe([0.35, 0.27], [0.35, 0.6], duration=0.2)
                    poco_instance.click()
                print(current_level, level_number)
            else:
                self.poco.swipe([0.35, 0.25], [0.35, 0.80], duration=0.2)
                poco_instance.click()
            current_level = current_level - 1

    def battle(self):
        self.outer_page.the_shadow_keep()
        self.outer_page.enter_btn()
        self.outer_page.into_fight()
        self.outer_page.fighting_and_back_trans()

    def is_check(self):
        self.poco.swipe([0.35, 0.55], [0.35, 0.7], duration=0.2)


if __name__ == '__main__':
    from case.lib.driver.unity_window import get_unity_window_poco_instance
    reward = RewardPage(get_unity_window_poco_instance())
    reward.battle()










