from case.lib.driver.android_app import AndroidPocoUnit
from case.page.music import HomePage
from utils import logcase


class TestCloudMusic(AndroidPocoUnit):

    def setUp(self) -> None:
        self.home_page = HomePage(self.poco)

    @logcase
    def test_1login_music(self):
        self.home_page.transaction()

    @logcase
    def test_2add_my_favorite(self):
        self.home_page.transaction2()


if __name__ == '__main__':
    import unittest
    unittest.main()
