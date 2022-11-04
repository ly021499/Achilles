# @Time   : 2022/11/4 17:31
# @Author : LOUIE
# @Desc   : to do something ...
from core.app.poco2 import Poco2
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from case.lib.engine.android_app import get_poco_instance



from airtest.core.api import start_app, stop_app

import time

poco = get_poco_instance()

package_name = 'com.google.android.calculator'
start_app(package_name)

# poco('com.google.android.calculator:id/clr')
#
#
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
