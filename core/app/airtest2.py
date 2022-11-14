# @Time   : 2022/11/4 14:14
# @Author : LOUIE
# @Desc   : airtest核心api的二次封装

from airtest.core import api
from utils.logger import log, logwrap


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
        raise ConnectionError from e


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
        log.info(f"Stop app {package}")
    except Exception as e:
        log.error(f"Failed to stop app {package}")
        raise e


def clear_app(package):
    try:
        api.clear_app(package)
        log.info(f"Clear app {package}")
    except Exception as e:
        log.error(f"Failed to clear app {package}")
        raise e


def install(filepath, **kwargs):
    try:
        log.info(f"Install app {filepath}")
        return api.install(filepath, **kwargs)
    except Exception as e:
        log.error(f"Failed to install app {filepath}")
        raise e


def uninstall(package):
    try:
        log.info(f"Uninstall app {package}")
        return api.uninstall(package)
    except Exception as e:
        log.error(f"Failed to uninstall app {package}")
        raise e


def snapshot(package):
    raise NotImplementedError


def wake():
    try:
        log.info(f"Wake app")
        return api.wake
    except Exception as e:
        log.error(f"Failed to wake app")
        raise e


def home(package):
    raise NotImplementedError


def touch(v, times=1, **kwargs):
    try:
        log.info(f"touch app {v}")
        return api.touch(v, times=1, **kwargs)
    except Exception as e:
        log.error(f"Failed to uninstall app {v}")
        raise e


def double_click(package):
    raise NotImplementedError


def swipe(package):
    raise NotImplementedError


def pinch():
    raise NotImplementedError


def keyevent():
    raise NotImplementedError


def text():
    try:
        log.info(f"touch app {v}")
        return api.exists(v)
    except Exception as e:
        log.error(f"Failed to uninstall app {v}")
        raise e


def sleep(secs=1.0):
    import time
    time.sleep(secs)
    log.info(f'time sleep {secs} seconds')


def wait():
    raise NotImplementedError


def exists(v):
    try:
        log.info(f"touch app {v}")
        return api.exists(v)
    except Exception as e:
        log.error(f"Failed to uninstall app {v}")
        raise e


@logwrap('1111111')
def find_all():
    try:
        assert 1 == 2
    except:
        print(222)


if __name__ == '__main__':
    sleep()
