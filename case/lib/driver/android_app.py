# @Time   : 2022/11/4 14:13
# @Author : LOUIE
# @Desc   : android 应用 diver

from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from setting import ANDROID_DEVICE_HOST
from unittest import TestCase
from core.air import connect_device
from core.poco2 import Poco2


class AndroidPoco(AndroidUiautomationPoco, Poco2):
    pass


def get_android_poco_instance():
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
        # start_app(ANDROID_PACKAGE_NAME)
        # cls.poco.sleep(10)
    #
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     cls.poco.sleep(3)
    #     stop_app(ANDROID_PACKAGE_NAME)




