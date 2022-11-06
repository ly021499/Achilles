# @Time   : 2022/11/4 14:13
# @Author : LOUIE
# @Desc   : iOS 应用 diver
from airtest.core.api import *
auto_setup(__file__)

connect_device("iOS:///http://127.0.0.1:8100")

from poco.drivers.ios import iosPoco
poco = iosPoco()
















