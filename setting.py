import platform
import os
import time


__ENV = 'TEST'


def __get_result_path():
    dir_name = str(time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time())))
    result_path = os.path.join(os.path.join(BASE_DIR, "report"), dir_name)
    if __ENV.upper() == 'PROD':
        if not os.path.exists(result_path):
            os.mkdir(result_path)
    return result_path


# Path
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
CASE_DIR = os.path.join(BASE_DIR, "case\\tests")
LOG_DIR = os.path.join(BASE_DIR, "report\\logs")
REPORT_DIR = __get_result_path()


# Config, Only the CONFIG parameters need to be modified
__TEST_CONFIG = {
    'wx_url': '',
    'webhook': '',
    'is_write': False,
    'android_device_host': 'Android:///127.0.0.1:7555',
    'ios_device_host': 'iOS:///127.0.0.1:7555',
    'cmd_conf': {
        'url': 'http://192.168.1.16/gmModuleapi/Gmcommand/command',
        'cookie': "ci_session=vhv65b5rt0hm41andok3pg6l9196lgv5; oss3_session=8b6cqeb3scgdk79tli309jdmqk318u2q",
    }
}

__PROD_CONFIG = {
    'wx_url': '',
    'webhook': '',
    'is_write': True,
    'android_device_host': 'Android:///127.0.0.1:7555',
    'ios_device_host': 'iOS:///127.0.0.1:7555',
    'cmd_conf': {
        'url': '',
        'cookie': ''
    }
}


def __get_env_conf():
    env_list = ['PROD', 'TEST']
    if __ENV.upper() not in env_list:
        raise FileNotFoundError
    if __ENV.upper() == 'TEST':
        return __TEST_CONFIG
    else:
        return __PROD_CONFIG


CONF = __get_env_conf()


# Device
ANDROID_DEVICE_HOST = CONF.get('android_device_host')
ANDROID_PACKAGE_NAME = 'com.netease.cloudmusic'
IOS_DEVICE_HOST = CONF.get('ios_device_host')
IOS_PACKAGE_NAME = 'com.netease.cloudmusic'


# Log
IS_WRITE = CONF.get('is_write')
LOG_FORMAT = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | " \
             "<green>{level: <8}</green> | " \
             "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - " \
             "<green>{message}</green>"
SYSTEM = platform.system()


# Report
TESTER = 'LOUIE'
TITLE = 'Achilles Report'
DESCRIPTION = 'Before the Trojan War broke out, Tethys heard a prophecy about Achilles'
RERUN = 1
WX_URL = CONF.get('wx_url')
WEBHOOK = CONF.get('webhook')

# GM
GM_URL = CONF['cmd_conf'].get('url')
GM_COOKIE = CONF['cmd_conf'].get('cookie')



