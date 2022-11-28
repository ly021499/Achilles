# @Time   : 2022/11/14 16:31
# @Author : LOUIE
# @Desc   : to do something ...
from case.lib.driver.unity_app import Unity3dPocoUnit
from case.page.outer import OuterPage
from utils import logcase


class TestOuter(Unity3dPocoUnit):

    @logcase
    def test_a_elemental_valley(self):
        self.outer_page.elemental_valley_trans()

    def setUp(self) -> None:
        self.outer_page = OuterPage(self.poco)

    @logcase
    def test_b_lost_sector(self):
        self.outer_page.lost_sector_trans()

    @logcase
    def test_c_forbidden_sector(self):
        self.outer_page.forbidden_sector_trans()

    @logcase
    def test_d_the_shadow_keep(self):
        self.outer_page.the_shadow_keep_trans()


if __name__ == '__main__':
    import unittest
    unittest.main()
