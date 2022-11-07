from pocounit.suite import PocoTestSuite
from airtest.core.api import device as current_device, connect_device
from airtest.core.api import start_app, stop_app

from case.lib.engine.android_app import AndroidAppCase
from case.lib.utils.installation import install_android_app

import time


# 套件
class CalculatorSuite(PocoTestSuite):
    def setUp(self):
        # 连接设备地址
        if not current_device():
            connect_device('Android:///')
        # apk包名
        self.package_name = 'com.google.android.calculator'
        # 启动应用
        start_app(self.package_name)

    def tearDown(self):
        # 关闭应用
        stop_app(self.package_name)


# 用例
class CalculatorCase(AndroidAppCase):
    def setUp(self):
        # clear previous result
        clr = self.poco('com.google.android.calculator:id/clr')
        if clr.exists():
            clr.click()


class CalculatorPlus(CalculatorCase):
    def runTest(self):
        self.poco('com.google.android.calculator:id/digit_1').click()
        self.poco('com.google.android.calculator:id/op_add').click()
        self.poco('com.google.android.calculator:id/digit_1').click()
        self.poco('com.google.android.calculator:id/eq').click()
        time.sleep(1)
        result = self.poco('com.google.android.calculator:id/formula').get_text()
        self.assertEqual(result, '2', '1+1=2 ^^')


class CalculatorMinus(CalculatorCase):
    def runTest(self):
        self.poco('com.google.android.calculator:id/digit_1').click()
        self.poco('com.google.android.calculator:id/op_sub').click()
        self.poco('com.google.android.calculator:id/digit_1').click()
        self.poco('com.google.android.calculator:id/eq').click()
        time.sleep(1)
        result = self.poco('com.google.android.calculator:id/formula').get_text()
        self.assertEqual(result, '0', '1-1=0 ^^')


if __name__ == '__main__':
    suite = CalculatorSuite([
        CalculatorPlus(),
        CalculatorMinus(),
    ])
    import pocounit
    pocounit.run(suite)
