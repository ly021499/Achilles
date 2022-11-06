# @Time   : 2022/11/4 14:13
# @Author : LOUIE
# @Desc   : android 应用 diver
from pocounit.case import PocoTestCase
from pocounit.addons.poco.action_tracking import ActionTracker
from pocounit.addons.poco.capturing import SiteCaptor
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from airtest.core.api import device as current_device
from airtest.core.helper import device_platform

from utils import log
from utils import exception
from core.app.airtest2 import connect_device, start_app
from setting import ANDROID_DEVICE_HOST, PACKAGE_NAME
from core.app.poco2 import AndroidPoco


class AndroidAppCase(PocoTestCase):

    # Todo: 封装安卓APP的单元测试框架，简单理解为unittest的再封装，安卓原生APP可以直接集成

    @classmethod
    def setUpClass(cls):
        super(AndroidAppCase, cls).setUpClass()
        log.info(f'Connect device host ...')
        if not current_device():        # 判断 device 是否为空，如果为空则连接默认地址
            device_host = 'Android://127.0.0.1:7555'
            connect_device(device_host)
            log.info(f'Connect success! host: {device_host}')

        dev = current_device()
        meta_info_emitter = cls.get_result_emitter('metaInfo')
        if device_platform() == 'Android':
            meta_info_emitter.snapshot_device_info(dev.serialno, dev.adb.get_device_info())

        cls.poco = AndroidUiautomationPoco(screenshot_each_action=False)    # 实例化poco对象

        action_tracker = ActionTracker(cls.poco)
        cls.register_addon(action_tracker)
        cls.site_capturer = SiteCaptor(cls.poco)
        cls.register_addon(cls.site_capturer)


def get_poco_instance():
    if not current_device():  # 判断 device 是否为空，如果为空则连接默认地址
        device_host = ANDROID_DEVICE_HOST
        connect_device(device_host)

    poco = AndroidPoco(screenshot_each_action=False)  # 实例化poco对象

    start_app(PACKAGE_NAME)

    return poco