# @Time   : 2022/11/14 16:31
# @Author : LOUIE
# @Desc   : to do something ...
from case.lib.driver.unity_app import Unity3dPocoUnit
from case.page.login import LoginPage
from utils import logcase


class TestPapa2(Unity3dPocoUnit):

    def setUp(self) -> None:
        self.login_page = LoginPage(self.poco)

    # @logcase
    # def test_a_login_papa2(self):
    #     self.login_page.transaction()

    @logcase
    def test_b_close_note(self):
        self.login_page.transaction()


if __name__ == '__main__':
    import unittest
    unittest.main()
