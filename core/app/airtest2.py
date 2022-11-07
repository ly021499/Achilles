# @Time   : 2022/11/4 14:14
# @Author : LOUIE
# @Desc   : airtest核心api的二次封装

from airtest.core import api
from utils.logger import log
from utils.exception import ConnectionError


def init_device(platform=None, uuid=None, **kwargs):
    """
    Initialize device if not yet, and set as current device.

    :param platform: Android, IOS or Windows
    :param uuid: uuid for target device, e.g. serialno for Android, handle for Windows, uuid for iOS
    :param kwargs: Optional platform specific keyword args, e.g. `cap_method=JAVACAP` for Android
    :return: device instance
    :Example:
        >>> init_device(platform="Android",uuid="SJE5T17B17", cap_method="JAVACAP")
        >>> init_device(platform="Windows",uuid="123456")
    """
    try:
        api.init_device(platform=platform, uuid=uuid, **kwargs)
        log.info(f"Init device success, platform: {platform}, uuid:  {uuid}")
    except Exception as e:
        log.error(f"Failed to init device, platform: {platform}, uuid:  {uuid}")
        raise e


def connect_device(uri):
    log.info('Ready to connect device host ...')
    try:
        api.connect_device(uri)
        log.info(f'Connection device succeeded... host: {uri}')
    except ConnectionError as e:
        log.info(f'Connecting device failed... host: {uri}')
        raise ConnectionError


def device():
    current_active_device = api.device()
    log.info(f'Get current active device: {current_active_device}')
    return current_active_device


def set_current(idx):
    try:
        log.info(f"Set current active device idx: {idx}")
        api.set_current(idx)
    except Exception as e:
        log.error(f"Failed to set current active device idx: {idx}")
        raise e


def auto_setup(basedir=None, devices=None, logdir=None, project_root=None, compress=None):
    api.auto_setup(basedir=basedir, devices=devices, logdir=logdir, project_root=project_root, compress=compress)


def shell(cmd):
    try:
        log.info(f"Execute adb shell command: {cmd}")
        return api.shell(cmd)
    except Exception as e:
        log.error(f"Failed to execute adb shell command: {cmd}")
        raise e


def start_app(package, activity=None):
    try:
        api.start_app(package, activity)
        log.info(f"Start app: {package}, activity: {activity}")
    except Exception as e:
        log.error(f"Failed start app {package}, activity: {activity}")
        raise e


def stop_app(package):
    try:
        api.stop_app(package)
        log.info(f"stop app {package}")
    except Exception as e:
        log.error(f"Failed to stop app {package}")
        raise e
















