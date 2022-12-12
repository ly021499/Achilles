# @Time   : 2022/11/16 16:02
# @Author : LOUIE
# @Desc   : 验证【贪婪禁地】每个副本所有关卡的 1.通关情况 2.能量消耗 3.战斗奖励与运营配置符合

from tests.lib.driver.unity_app import Unity3dPocoUnit
from tests.proxy.outer.instance import InstanceProxy
from utils import log


class TestForbiddenSector(Unity3dPocoUnit):

    def setUp(self) -> None:
        self.instance = InstanceProxy(self.poco)

    @log.case
    def test_a_verify_brush_instance_of_bihna(self):
        self.instance.verify_brush_instance_of_bihna()

    @log.case
    def test_b_verify_brush_instance_of_chester(self):
        self.instance.verify_brush_instance_of_chester()


if __name__ == '__main__':
    import unittest
    unittest.main()
