# -*- coding: utf-8 -*-
# @Time   : 2022/11/16 16:02
# @Author : LOUIE
# @Desc   : 验证能量、金钥消耗正确

from case.lib.driver.unity_app import Unity3dPocoUnit
from case.proxy.energy import EnergyHandle
from utils import logcase


class TestConsumeEnergy(Unity3dPocoUnit):

    def setUp(self) -> None:
        self.energy = EnergyHandle(self.poco)

    @logcase
    def test_a_verify_energy_consumption_of_lost_sector(self):
        self.energy.verify_energy_consumption_of_lost_sector()

    @logcase
    def test_b_verify_energy_consumption_of_the_shadow_keep(self):
        self.energy.verify_energy_consumption_of_the_shadow_keep()

    @logcase
    def test_c_verify_energy_consumption_of_potion(self):
        self.energy.verify_energy_consumption_of_potion()

    @logcase
    def test_d_verify_energy_consumption_of_the_gold(self):
        self.energy.verify_energy_consumption_of_the_gold()

    @logcase
    def test_e_verify_energy_consumption_of_elemental_valley(self):
        self.energy.verify_energy_consumption_of_elemental_valley()


if __name__ == '__main__':
    import unittest
    unittest.main()

