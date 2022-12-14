# @Time   : 2022/11/16 16:02
# @Author : LOUIE
# @Desc   : 验证能量、金钥消耗正确

from tests.lib.driver.unity_app import Unity3dPocoUnit
from tests.proxy.outer.energy import EnergyProxy
from tests.page.outer import OuterPage
from utils import log


class TestConsumeEnergy(Unity3dPocoUnit):

    def setUp(self) -> None:
        self.energy = EnergyProxy(self.poco)
        self.outer = OuterPage(self.poco)

    def tearDown(self) -> None:
        self.outer.back_to_outer()

    @log.case
    def test_a_verify_energy_consumption_of_lost_sector(self):
        self.energy.verify_energy_consumption_of_lost_sector()

    @log.case
    def test_b_verify_energy_consumption_of_element_valley(self):
        self.energy.verify_energy_consumption_of_element_valley()

    @log.case
    def test_c_verify_energy_consumption_of_the_shadow_keep(self):
        self.energy.verify_energy_consumption_of_the_shadow_keep()

    @log.case
    def test_d_verify_energy_consumption_of_potion(self):
        self.energy.verify_energy_consumption_of_potion()

    @log.case
    def test_e_verify_energy_consumption_of_the_gold(self):
        self.energy.verify_energy_consumption_of_the_gold()


if __name__ == '__main__':
    import unittest
    unittest.main()

