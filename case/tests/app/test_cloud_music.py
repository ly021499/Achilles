import unittest
from case.lib.driver.android_app import get_android_poco_instance
from core.app.airtest2 import *
from setting import PACKAGE_NAME
from case.page.home_page import HomePage

import logging

logger = logging.getLogger("airtest")
logger.setLevel(logging.INFO)


class TestCloudMusic(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.poco = get_android_poco_instance()
        cls.poco.sleep(10)
        cls.home_page = HomePage(cls.poco)

    def test_login_music(self):
        self.home_page.transaction()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.poco.sleep(3)
        stop_app(PACKAGE_NAME)


if __name__ == '__main__':
    unittest.main()
