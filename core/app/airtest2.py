# @Time   : 2022/11/4 14:14
# @Author : LOUIE
# @Desc   : airtest核心api的二次封装

from airtest.core import api
from utils.logger import log
from utils.exception import ConnectionError


def init_device(platform=None, uuid=None, **kwargs):
    try:
        api.init_device(platform=platform, uuid=uuid, **kwargs)
        log.info(f"init device success, platform: {platform}")
    except Exception as e:
        log.error(f"failed init device, platform: {platform}")
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
    return api.device()


def set_current(idx):
    api.set_current(idx)


def auto_setup(basedir=None, devices=None, logdir=None, project_root=None, compress=None):
    api.auto_setup(basedir=basedir, devices=devices, logdir=logdir, project_root=project_root, compress=compress)


def shell(cmd):
    return api.shell(cmd)


def start_app(package, activity=None):
    try:
        api.start_app(package, activity)
        log.info(f"start app: {package}, activity: {activity}")
    except Exception as e:
        log.error(f"failed start app {package}, activity: {activity}")
        raise e


def stop_app(package):
    try:
        api.stop_app(package)
        log.info(f"stop app {package}")
    except Exception as e:
        log.error(f"failed stop app {package}")
        raise e
















