# @Time   : 2022/11/16 16:02
# @Author : LOUIE
# @Desc   : 验证【苍穹之城】每个副本所有关卡的 1.通关情况 2.能量消耗 3.战斗奖励与运营配置符合

from tests.lib.driver.unity_app import Unity3dPocoUnit
from tests.proxy.outer.reward import RewardPage
from utils import log


class TestSkyCity(Unity3dPocoUnit):

    def setUp(self) -> None:
        self.reward = RewardPage(self.poco)

    # @log.case
    # def test_a_brush_sky_city_25(self):
    #     self.reward.brush_sky_city(1, 25)
    #
    # @log.case
    # def test_b_brush_sky_city_50(self):
    #     self.reward.brush_sky_city(26, 50)
    #
    # @log.case
    # def test_c_brush_sky_city_75(self):
    #     self.reward.brush_sky_city(51, 75)

    @log.case
    def test_d_brush_sky_city_100(self):
        self.reward.brush_sky_city(60, 100)


if __name__ == '__main__':
    import unittest
    unittest.main()
