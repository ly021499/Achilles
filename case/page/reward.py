# @Time   : 2022/11/17 18:29
# @Author : LOUIE
# @Desc   : 掉落奖励
import re
from utils import logwrap, logstep
from utils.plugins.parser import get_reward_config, get_target_reward_data
from case.position import reward_pos, outer_pos
from case.lib.page import Page
from case.page.outer import OuterPage
from case.lib.utils import assertion
from poco.exceptions import InvalidOperationException, PocoNoSuchNodeException


class RewardPage(Page):

    def __init__(self, poco_instance):
        super(RewardPage, self).__init__(poco_instance)
        self.outer_page = OuterPage(poco_instance)

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
        return self.outer_page.fighting_and_back_trans()

    @logwrap('升序执行 当前副本下的所有关卡')
    def execute_instance_in_asc(self, max_level_pos):
        """
        升序执行 当前副本下的所有关卡
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

    @logwrap('降序执行 当前副本下的所有关卡')
    def execute_instance_in_desc(self, max_level: int, instance: str):
        """
        降序执行 当前副本下的所有关卡
        :param max_level: 当前副本最大关卡数
        :param instance: 副本名称
        :return:
        """
        start_level = 8
        while start_level <= int(max_level):
            self.sleep(0.88)
            poco_instance = self.poco(textMatches=str(f'{start_level}'))
            poco_instance.click()

            start_energy = self.outer_page.get_current_energy_value()

            # 判断 准备通关关卡是否与选中关卡一致
            level_name = self.get_text(reward_pos.level_name_pos).split('-')[1]

            logstep(f'当前选中关卡：{start_level}， 关卡名称：{level_name}')
            battle_reward_list = self.battle()

            end_energy = self.outer_page.get_current_energy_value()

            logstep(f'校验能量值消耗数值是否正确 ...')
            assertion.assert_less_equal(start_energy - end_energy, 10)

            # 获取表格中的数据
            reward_config = get_reward_config(instance)
            preview_reward_list = get_target_reward_data(reward_config, level_name)
            surprise_drop_item = preview_reward_list[-1]
            preview_reward_list.extend(['金币', '体力', '钻石', '普通核铁'])

            for reward_ in battle_reward_list:
                if reward_[0] == '常规':
                    assertion.assert_in(reward_[1], preview_reward_list)
                elif reward_[0] == '首次':
                    assertion.assert_in(reward_[1], surprise_drop_item)
                else:
                    logstep(f'惊喜掉落物品：{reward_}')
            start_level += 1

    def execute_instance(self, instance_type, level_pos, instance):
        self.outer_page.retry(instance_type)
        sheet_name = instance_type.split('=')[1]
        self.click(instance)
        self.outer_page.enter_btn()
        self.execute_instance_in_desc(level_pos, sheet_name)


if __name__ == '__main__':
    from case.lib.driver.unity_app import get_unity3d_poco_instance
    reward = RewardPage(get_unity3d_poco_instance())
    reward.execute_instance(outer_pos.lost_sector_pos, outer_pos.lost_sector_level_pos, outer_pos.papillaire_pos)
    # reward.run_from_top_to_bottom(12)
    # reward.get_battle_reward()









