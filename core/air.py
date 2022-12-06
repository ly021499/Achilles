# @Time   : 2022/11/4 14:14
# @Author : LOUIE
# @Desc   : airtest核心api的二次封装

from airtest.core import api as air
from utils.logger import log, logwrap
import time


def init_device(platform=None, uuid=None, **kwargs):
    try:
        air.init_device(platform=platform, uuid=uuid, **kwargs)
        log.info(f"init device success, platform: {platform}, uuid:  {uuid}")
    except Exception as e:
        log.error(f"failed to init device, platform: {platform}, uuid:  {uuid}")
        raise e


def connect_device(uri):
    log.info('🍇 🍉 ready to connect device host ...')
    try:
        air.connect_device(uri)
        log.info(f'🍊 🍋 connect device succeeded... host: {uri}')
    except ConnectionError as e:
        log.error(f'connect device failed... host: {uri}')
        raise ConnectionError from e


def device():
    current_active_device = air.device()
    log.info(f'get current active device: {current_active_device}')
    return current_active_device


def set_current(idx):
    try:
        log.info(f"set current active device idx: {idx}")
        air.set_current(idx)
    except Exception as e:
        log.error(f"failed to set current active device idx: {idx}")
        raise e


def auto_setup(basedir=None, devices=None, logdir=None, project_root=None, compress=None):
    air.auto_setup(basedir=basedir, devices=devices, logdir=logdir, project_root=project_root, compress=compress)


def shell(cmd):
    try:
        log.info(f"execute adb shell command: {cmd}")
        return air.shell(cmd)
    except Exception as e:
        log.error(f"failed to execute adb shell command: {cmd}")
        raise e


def start_app(package, activity=None):
    try:
        air.start_app(package, activity)
        log.info(f"start app: {package}, activity: {activity}")
    except Exception as e:
        log.error(f"failed start app {package}, activity: {activity}")
        raise e


def stop_app(package):
    try:
        air.stop_app(package)
        log.info(f"stop the application on device, package: {package}")
    except Exception as e:
        log.error(f"failed to stop the application on device, package: {package}")
        raise e


def clear_app(package):
    try:
        air.clear_app(package)
        log.info(f"clear data of the application on device, package: {package}")
    except Exception as e:
        log.error(f"failed to clear data of the application on device, package: {package}")
        raise e


def install(filepath, **kwargs):
    try:
        log.info(f"install application: {filepath}")
        return air.install(filepath, **kwargs)
    except Exception as e:
        log.error(f"failed to install application: {filepath}")
        raise e


def uninstall(package):
    try:
        log.info(f"uninstall application: {package}")
        return air.uninstall(package)
    except Exception as e:
        log.error(f"failed to uninstall application: {package}")
        raise e


def snapshot(filename=None, msg="", quality=None, max_size=None):
    try:
        log.info(f"take the screenshot of the device and save it to the filepath:{filename}.")
        return air.snapshot(filename, msg, quality, max_size)
    except Exception as e:
        log.error(f"failed to wake up and unlock the device")
        raise e


def wake():
    try:
        log.info(f"wake up and unlock the device")
        return air.wake
    except Exception as e:
        log.error(f"failed to wake up and unlock the device")
        raise e


def home(package):
    raise NotImplementedError


def touch(v, times=1, **kwargs):
    try:
        log.info(f"perform the touch action on the device screen, pos: {v}")
        return air.touch(v, times, **kwargs)
    except Exception as e:
        log.error(f"failed to perform the touch action on the device screen, pos: {v}")
        raise e


def double_click(v1, v2=None, vector=None, **kwargs):
    log.info(f"perform double click")
    return air.double_click(v1, v2, vector, **kwargs)


def swipe(v1, v2=None, vector=None, **kwargs):
    log.info("Perform the swipe action on the device screen.")
    return air.swipe(v1, v2, vector, **kwargs)


def pinch(in_or_out='in', center=None, percent=0.5):
    log.info(f"perform the pinch action on the device screen")
    return air.pinch(in_or_out, center, percent)


def keyevent(keyname, **kwargs):
    log.info(f"perform key event keyname: {keyname} on the device.")
    return air.keyevent(keyname, **kwargs)


def text(value, enter=True, **kwargs):
    try:
        log.info(f"input {value} on the target device")
        return air.text(text, enter, **kwargs)
    except Exception as e:
        log.error(f"failed to input {value} on the target device")
        raise e


def sleep(secs=1.0):
    time.sleep(secs)
    log.info(f'time sleep {secs} seconds')


def wait():
    raise NotImplementedError


def exists(v):
    try:
        log.info(f"the node: {v} exists.")
        return air.exists(v)
    except Exception as e:
        log.error(f"the node: {v} not exists.")
        raise e


if __name__ == '__main__':
    sleep()
