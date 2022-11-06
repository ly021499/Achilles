import unittest
from case.lib.driver.android_app import get_poco_instance
import time

import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.INFO)


class TestCloudMusic(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.poco = get_poco_instance()
        time.sleep(7)

    def test_login_music(self):
        print(1111)

    @classmethod
    def tearDownClass(cls) -> None:pass


if __name__ == '__main__':
    unittest.main()