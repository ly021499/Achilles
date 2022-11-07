# @Time   : 2022/11/4 14:13
# @Author : LOUIE
# @Desc   : android 应用 diver

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import device as current_device
from core.app.airtest2 import connect_device, start_app
from setting import ANDROID_DEVICE_HOST, PACKAGE_NAME
from core.app.poco2 import Poco2


class AndroidPoco(AndroidUiautomationPoco, Poco2):
    pass


def get_android_poco_instance():
    if not current_device():  # 判断 device 是否为空，如果为空则连接默认地址
        device_host = ANDROID_DEVICE_HOST
        connect_device(device_host)

    poco = AndroidPoco(screenshot_each_action=False)  # 实例化poco对象

    start_app(PACKAGE_NAME)

    return poco