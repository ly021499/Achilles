# @Time   : 2022/11/4 14:13
# @Author : LOUIE
# @Desc   : iOS 应用 diver
from airtest.core.api import *
from core.app.airtest2 import connect_device, start_app

from poco.drivers.ios import iosPoco
from core.app.poco2 import Poco2
from setting import IOS_DEVICE_HOST, PACKAGE_NAME


class IosPoco(iosPoco, Poco2):

    pass


def get_ios_poco_instance():
    connect_device(IOS_DEVICE_HOST)

    poco = IosPoco()
    start_app(PACKAGE_NAME)
    return poco



















