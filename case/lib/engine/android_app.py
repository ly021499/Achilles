from pocounit.case import PocoTestCase
from pocounit.addons.poco.action_tracking import ActionTracker
from pocounit.addons.poco.capturing import SiteCaptor
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from airtest.core.api import connect_device, device as current_device
from airtest.core.helper import device_platform

from utils import log


class AndroidAppCase(PocoTestCase):

    # Todo: 封装安卓APP的单元测试框架，简单理解为unittest的再封装，安卓原生APP可以直接集成

    @classmethod
    def setUpClass(cls):
        super(AndroidAppCase, cls).setUpClass()
        log.info(f'Connect device host ...')
        if not current_device():
            device_host = 'Android://127.0.0.1:7555'
            connect_device(device_host)
            log.info(f'Connect success! host: {device_host}')

        dev = current_device()
        meta_info_emitter = cls.get_result_emitter('metaInfo')
        if device_platform() == 'Android':
            meta_info_emitter.snapshot_device_info(dev.serialno, dev.adb.get_device_info())

        cls.poco = AndroidUiautomationPoco(screenshot_each_action=False)

        action_tracker = ActionTracker(cls.poco)
        cls.register_addon(action_tracker)
        cls.site_capturer = SiteCaptor(cls.poco)
        cls.register_addon(cls.site_capturer)
