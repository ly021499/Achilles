# @Time   : 2022/11/14 16:31
# @Author : LOUIE
# @Desc   : to do something ...
from case.lib.driver.android_app import AndroidPocoUnit
from case.page.login import LoginPage
from utils import logcase


class TestCloudMusic(AndroidPocoUnit):

    def setUp(self) -> None:
        self.home_page = LoginPage(self.poco)

    @logcase
    def test_1_login_music(self):
        self.home_page.transaction()


if __name__ == '__main__':
    import unittest
    unittest.main()
