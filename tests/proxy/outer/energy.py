from tests.page.outer import OuterPage
from tests.position.outer_pos import *
from tests.lib.utils import assertion
from utils import log


class EnergyProxy:

    def __init__(self, poco_instance):
        self.op = OuterPage(poco_instance)

    def brush_instance_zones(self, instance_type, instance):
        self.op.retry(instance_type)
        self.op.check_exists_instance(instance)

        start_energy = self.op.get_current_energy_value()
        self.op.enter_btn()
        self.op.get_current_level_name()
        self.op.into_battle()
        self.op.fighting()
        self.op.always_click_continue()

        if self.op.exists(Public.into_battle_pos):
            self.op.close_page()
        end_energy = self.op.get_current_energy_value()

        log.step('副本闯关完成 ...')
        self.op.back_to_outer()
        return start_energy - end_energy

    def assert_energy(self, actual, expected):
        """校验能量消耗是否正确"""
        log.step(f'校验能量值消耗数值是否正确 ...')
        assertion.assert_less_equal(actual, expected)

    @log.wrap('验证<茫然遗迹-比娜>的能量消耗值：10')
    def verify_energy_consumption_of_lost_sector(self):
        """
        验证<茫然遗迹>的能量消耗值：10
        """
        consume_energy = self.brush_instance_zones(Lost.lost_sector_pos, Lost.bihna_pos)
        self.assert_energy(consume_energy, Lost.lost_energy_pos)

    @log.wrap('验证<虚影殿堂->的能量消耗值：10')
    def verify_energy_consumption_of_the_shadow_keep(self):
        """
        验证<虚影殿堂>的能量消耗值：10
        """
        consume_energy = self.brush_instance_zones(Shadow.shadow_keep_pos, Shadow.first_instance_pos)
        self.assert_energy(consume_energy, Shadow.shadow_energy_pos)

    @log.wrap('验证<贪婪禁地-药水研究所>的能量消耗值：10')
    def verify_energy_consumption_of_potion(self):
        """
        验证<贪婪禁地-药水研究所>的能量消耗值：10
        """
        consume_energy = self.brush_instance_zones(Forbid.forbidden_sector_pos, Forbid.potion_pos)
        self.assert_energy(consume_energy, Forbid.potion_energy_pos)

    @log.wrap('验证<贪婪禁地-黄金谷>的能量消耗值：1 key')
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
        self.op.always_click_continue()

        end_energy = self.op.get_current_energy_value()

        if self.op.exists(Public.into_battle_pos):
            self.op.close_page()
        self.op.close_page()
        log.step('副本闯关完成 ...')

        # 断言：黄金谷如果是首次通关，不扣钥匙
        if self.op.exists(Forbid.gold_pos):
            if int(current_level) < int(Forbid.gold_level_pos):
                assertion.assert_equal(start_energy - end_energy, 0)
            else:
                assertion.assert_equal(start_energy - end_energy, Forbid.gold_energy_pos)

    @log.wrap('验证<元素峡谷-冰元素>的能量消耗值：15')
    def verify_energy_consumption_of_element_valley(self):
        """
        验证<元素峡谷>的能量消耗值：15
        """
        consume_energy = self.brush_instance_zones(Element.element_valley_pos, Element.ice_element_pos)
        self.assert_energy(consume_energy, Element.element_energy_pos)


if __name__ == '__main__':
    from tests.lib.driver.unity_app import get_unity3d_poco_instance
    ep = EnergyProxy(get_unity3d_poco_instance())
    # ep.verify_energy_consumption_of_lost_sector()
    # ep.verify_energy_consumption_of_the_shadow_keep()
    ep.verify_energy_consumption_of_potion()
    # ep.verify_energy_consumption_of_the_gold()
    # ep.verify_energy_consumption_of_element_valley()



