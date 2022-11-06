# @Time   : 2022/11/4 14:14
# @Author : LOUIE
# @Desc   : unity 游戏 driver
from airtest.core.api import *
auto_setup(__file__)

connect_device("android:///http://127.0.0.1:8100")

# 完全启动游戏
start_app("com.NetEase")
sleep(3.0) # sleep一定时间以确保游戏完全启动

from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()