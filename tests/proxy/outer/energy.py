from tests.page.outer import OuterPage
from tests.position.outer_pos import *
from tests.lib.utils import assertion
from utils import logwrap, logstep


class EnergyProxy:

    def __init__(self, poco_instance):
        self.op = OuterPage(poco_instance)

    def brush_instance_zones(self, instance_type):
        self.op.exists_instance(instance_type)

        # # 判断是否是虚影殿堂副本，需要判断哪些副本可以进入，否则跳过
        # if self.op.exists(outer_pos.shadow_keep_pos):
        #     if not self.op.exists(outer_pos.enter_btn_pos):
        #         continue

        start_energy = self.op.get_current_energy_value()

        logstep(f"选择副本类型：{str(instance_type).split('=')[1]} ...")

        self.op.enter_btn()
        self.op.into_battle()
        self.op.fighting()
        self.op.click_continue()

        if self.op.exists(Public.into_battle_pos):
            self.op.close_page()

        end_energy = self.op.get_current_energy_value()

        logstep('副本闯关完成 ...')
        self.op.back_to_outer()
        return start_energy - end_energy

    @logwrap('验证<茫然遗迹-比娜>的能量消耗值：10')
    def verify_energy_consumption_of_lost_sector(self):
        """
        验证<茫然遗迹>的能量消耗值：10
        """
        self.op.lost_sector()
        consume_energy = self.brush_instance_zones(Lost.bihna_pos)
        assertion.assert_less_equal(consume_energy, 10)

    @logwrap('验证<虚影殿堂->的能量消耗值：10')
    def verify_energy_consumption_of_the_shadow_keep(self):
        """
        验证<虚影殿堂>的能量消耗值：10
        """
        self.op.the_shadow_keep()
        consume_energy = self.brush_instance_zones(Shadow.mage_pos)
        assertion.assert_less_equal(consume_energy, 10)

    @logwrap('验证<贪婪禁地-药水研究所>的能量消耗值：10')
    def verify_energy_consumption_of_potion(self):
        """
        验证<贪婪禁地-药水研究所>的能量消耗值：10
        """
        self.op.forbidden_sector()
        consume_energy = self.brush_instance_zones(Forbid.potion_pos)
        assertion.assert_less_equal(consume_energy, 10)

    @logwrap('验证<贪婪禁地-黄金谷>的能量消耗值：1 key')
    def verify_energy_consumption_of_the_gold(self):
        """
        验证<贪婪禁地-黄金谷>的能量消耗值：1 key
        """
        self.op.forbidden_sector()
        self.op.click(Forbid.gold_pos)
        self.op.enter_btn()
        current_level = self.op.search_current_level_number()

        start_energy = self.op.get_current_energy_value()

        self.op.into_battle()
        self.op.fighting()
        self.op.click_continue()

        end_energy = self.op.get_current_energy_value()

        if self.op.exists(Public.into_battle_pos):
            self.op.close_page()

        self.op.close_page()
        logstep('副本闯关完成 ...')

        if self.op.exists(Forbid.gold_pos):
            # 黄金谷如果是首次通关，不扣钥匙
            if int(current_level) < int(Forbid.gold_level_pos):
                gold_key = 0
            else:
                gold_key = 1

        assertion.assert_equal(start_energy - end_energy, gold_key)

    @logwrap('验证<元素峡谷-冰元素>的能量消耗值：15')
    def verify_energy_consumption_of_element_valley(self):
        """
        验证<元素峡谷>的能量消耗值：15
        """
        self.op.element_valley()
        consume_energy = self.brush_instance_zones(Element.ice_element_pos)
        assertion.assert_less_equal(consume_energy, 15)

    @logwrap('验证<苍穹之城>的能量消耗值：15')
    def verify_energy_consumption_of_sky_city(self):
        """
        验证<苍穹之城>的能量消耗值是否正确
        """
        raise NotImplementedError


if __name__ == '__main__':
    from tests.lib.driver.unity_app import get_unity3d_poco_instance
    ep = EnergyProxy(get_unity3d_poco_instance())
    # ep.verify_energy_consumption_of_lost_sector()
    ep.verify_energy_consumption_of_the_shadow_keep()
    # ep.verify_energy_consumption_of_potion()
    ep.verify_energy_consumption_of_the_gold()
    # ep.verify_energy_consumption_of_element_valley()



