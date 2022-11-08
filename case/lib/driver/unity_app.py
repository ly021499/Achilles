# @Time   : 2022/11/4 14:14
# @Author : LOUIE
# @Desc   : unity 游戏 driver

from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco

from core.app.airtest2 import connect_device, start_app
from core.app.poco2 import Poco2
from setting import ANDROID_DEVICE_HOST, ANDROID_PACKAGE_NAME
from unittest import TestCase


class Unity3dPoco(UnityPoco, Poco2):

    pass


def get_unity3d_poco_instance():
    connect_device(ANDROID_DEVICE_HOST)

    poco_instance = Unity3dPoco()
    start_app(ANDROID_PACKAGE_NAME)

    return poco_instance


class Unity3dPocoUnit(TestCase):

    """
    Unity3d游戏 - 封装的TestCase类，直接用于测试用例的继承
    """

    poco = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.poco = get_unity3d_poco_instance()
        cls.poco.sleep(20)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.poco.sleep(3)
        stop_app(ANDROID_PACKAGE_NAME)
