# @Time   : 2022/11/4 14:14
# @Author : LOUIE
# @Desc   : unity 游戏 driver

from poco.drivers.unity3d.unity3d_poco import UnityPoco
from setting import ANDROID_DEVICE_HOST
from unittest import TestCase

from core.air import connect_device
from core.poco2 import Poco2

import logging

# 设置airtest日志等级，debug会输出很多日志
air_logger = logging.getLogger("airtest")
air_logger.setLevel(logging.ERROR)


class Unity3dPoco(UnityPoco, Poco2):

    pass


def get_unity3d_poco_instance():
    connect_device(ANDROID_DEVICE_HOST)

    return Unity3dPoco()


class Unity3dPocoUnit(TestCase):

    """
    Unity3d游戏 - 封装的TestCase类，直接用于测试用例的继承
    """

    poco = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.poco = get_unity3d_poco_instance()
        # cls.poco.sleep(10)

    # @classmethod
    # def tearDownClass(cls) -> None:
    #     cls.poco.sleep(3)
    #     stop_app(ANDROID_PACKAGE_NAME)
