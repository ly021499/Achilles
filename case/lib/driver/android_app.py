# @Time   : 2022/11/4 14:13
# @Author : LOUIE
# @Desc   : android 应用 diver

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import device as current_device
from core.app.airtest2 import connect_device, start_app, stop_app
from setting import ANDROID_DEVICE_HOST, ANDROID_PACKAGE_NAME
from core.app.poco2 import Poco2
from unittest import TestCase


class AndroidPoco(AndroidUiautomationPoco, Poco2):
    pass


def get_android_poco_instance():
    if not current_device():  # 判断 device 是否为空，如果为空则连接默认地址
        device_host = ANDROID_DEVICE_HOST
        connect_device(device_host)

    return AndroidPoco(screenshot_each_action=False)  # 实例化poco对象


class AndroidPocoUnit(TestCase):

    """
    Android应用 - 封装的TestCase类，直接用于测试用例的继承
    """

    poco = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.poco = get_android_poco_instance()
        start_app(ANDROID_PACKAGE_NAME)
        cls.poco.sleep(10)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.poco.sleep(3)
        stop_app(ANDROID_PACKAGE_NAME)




