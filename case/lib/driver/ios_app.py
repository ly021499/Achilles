# @Time   : 2022/11/4 14:13
# @Author : LOUIE
# @Desc   : iOS 应用 diver

from airtest.core.api import *
from core.app.airtest2 import connect_device, start_app

from poco.drivers.ios import iosPoco
from core.app.poco2 import Poco2
from setting import IOS_DEVICE_HOST, IOS_PACKAGE_NAME
from unittest import TestCase


class IosPoco(iosPoco, Poco2):

    pass


def get_ios_poco_instance():
    connect_device(IOS_DEVICE_HOST)

    return IosPoco()


class IOSPocoUnit(TestCase):

    """
    iOS应用 - 封装的TestCase类，直接用于测试用例的继承
    """

    poco = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.poco = get_ios_poco_instance()
        cls.poco.sleep(10)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.poco.sleep(3)
        stop_app(IOS_PACKAGE_NAME)
















