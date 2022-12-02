from case.page.outer import OuterPage
from case.position import outer_pos
from case.lib.utils import commands as cmd, assertion
from utils import logwrap, logstep


class InstanceHandle:

    def __init__(self, poco_instance):
        self.op = OuterPage(poco_instance)

    def verify_energy_consumption_of_lost_sector(self):
        """
        验证<茫然遗迹>的能量消耗值：10
        """
        self.op.lost_sector()
        self.op.play_trans(outer_pos.bihna_pos)
        assertion.assert_less_equal(self.op.start_energy - self.op.end_energy, 10)

    def verify_energy_consumption_of_the_shadow_keep(self):
        """
        验证<虚影殿堂>的能量消耗值：10
        """
        self.op.the_shadow_keep()
        self.op.play_trans(outer_pos.mage_pos)
        assertion.assert_less_equal(self.op.start_energy - self.op.end_energy, 10)

    def verify_energy_consumption_of_potion(self):
        """
        验证<贪婪禁地-药水研究所>的能量消耗值：10
        """
        self.op.forbidden_sector()

        self.op.play_trans(outer_pos.potion_pos)

        assertion.assert_less_equal(self.op.start_energy - self.op.end_energy, 10)

    def verify_energy_consumption_of_the_gold(self):
        """
        验证<贪婪禁地-黄金谷>的能量消耗值：1 key
        """
        self.op.forbidden_sector()
        self.op.click(outer_pos.the_gold_pos)
        logstep(f"选择关卡：{str(outer_pos.the_gold_pos).split('=')[1]} ...")
        self.op.enter_btn()

        # 判断是否有金币钥匙，如果没有则增加
        self.op.is_golden_key()

        start_energy = self.op.get_current_energy_value()

        # outer.choose_superheroes()

        self.op.into_fight()
        self.op.fighting_and_back_trans()

        end_energy = self.op.get_current_energy_value()
        assertion.assert_less_equal(start_energy - end_energy, 1)

        if self.op.exists(outer_pos.into_fight_pos):
            self.op.close_page()

        self.op.close_page()
        logstep('副本闯关完成 ...')

    def verify_energy_consumption_of_elemental_valley(self):
        """
        验证<元素峡谷>的能量消耗值：15
        """
        self.op.elemental_valley()
        self.op.play_trans(outer_pos.frost_lord_pos)
        assertion.assert_less_equal(self.op.start_energy - self.op.end_energy, 15)

    def verify_energy_consumption_of_sky_city(self):
        """
        验证<苍穹之城>的能量消耗值是否正确
        """
        raise NotImplementedError


if __name__ == '__main__':
    assertion.assert_equal(19 - 10, 10)






