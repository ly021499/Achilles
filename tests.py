# @Time   : 2022/11/4 17:31
# @Author : LOUIE
# @Desc   : to do something ...
from core.app.poco2 import Poco2
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from case.lib.driver.android_app import get_poco_instance
from core.app.airtest2 import stop_app, start_app
from utils.logger import log

import time

poco = get_poco_instance()

package_name = 'com.netease.cloudmusic'
start_app(package_name)

# poco('com.netease.cloudmusic')


# def runTest():
#     poco('com.google.android.calculator:id/digit_1').click()
#     poco('com.google.android.calculator:id/op_add').click()
#     poco('com.google.android.calculator:id/digit_1').click()
#     poco('com.google.android.calculator:id/eq').click()
#     time.sleep(1)
#     result = poco('com.google.android.calculator:id/formula').get_text()
#     assert result == 2
#
#
# runTest()
# time.sleep(5)
# stop_app(package_name)
