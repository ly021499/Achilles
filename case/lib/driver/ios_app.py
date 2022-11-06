# @Time   : 2022/11/4 14:13
# @Author : LOUIE
# @Desc   : iOS 应用 diver
from airtest.core.api import *
from setting import IOS_DEVICE_HOST
auto_setup(__file__)

connect_device(IOS_DEVICE_HOST)

from poco.drivers.ios import iosPoco
poco = iosPoco()
















