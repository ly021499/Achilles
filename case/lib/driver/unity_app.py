# @Time   : 2022/11/4 14:14
# @Author : LOUIE
# @Desc   : unity 游戏 driver

from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco

from core.app.airtest2 import connect_device, start_app
from core.app.poco2 import Poco2
from setting import ANDROID_DEVICE_HOST, PACKAGE_NAME


class Unity3dPoco(UnityPoco, Poco2):

    pass


def get_unity3d_poco_instance():
    connect_device(ANDROID_DEVICE_HOST)
    poco_instance = UnityPoco()
    start_app(PACKAGE_NAME)

    return poco_instance
