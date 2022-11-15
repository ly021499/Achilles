from case.lib.driver.android_app import AndroidPocoUnit
from case.page.music import MusicPage
from utils import logcase


class TestCloudMusic(AndroidPocoUnit):

    def setUp(self) -> None:
        self.home_page = MusicPage(self.poco)

    @logcase
    def test_1_login_music(self):
        self.home_page.transaction()

    @logcase
    def test_2_add_my_favorite(self):
        self.home_page.transaction2()


if __name__ == '__main__':
    import unittest
    unittest.main()
