import platform
import os
import time


__ENV = 'TEST'


# Config, Only the CONFIG parameters need to be modified
__TEST_CONFIG = {
    'wx_url': '',       # 企业微信请求地址
    'webhook': '',      # 企业微信webhook
    'output': False,    # 控制是否创建目录输出日志和报告
    'android_device_host': 'Android:///127.0.0.1:5555',     # android设备地址
    'ios_device_host': 'iOS:///127.0.0.1:5555',             # iOS设备地址
    'cmd_conf': {       # GM命令配置
        'url': 'http://192.168.1.16/gmModuleapi/Gmcommand/command',
        'cookie': "oss3_session=38gloqpl90urnilj7upcnd36dqr5o32q",  # cookie时效只有一天，需要定期更换
        'platform_id': 80,
        'server_id': 80002990
    }
}

__PRE_CONFIG = {
    'wx_url': '',
    'webhook': '',
    'output': False,
    'android_device_host': 'Android:///127.0.0.1:5555',
    'ios_device_host': 'iOS:///127.0.0.1:7555',
    'cmd_conf': {
        'url': 'https://oss3.hrgame.com.cn/gmModuleapi/Gmcommand/command',
        'cookie': "oss3_session=k55ih9sarta31bun945un5n8f9et06ms",
        'platform_id': 14,
        'server_id': 14102992
    }
}

__PROD_CONFIG = {
    'wx_url': '',
    'webhook': '',
    'output': True,
    'android_device_host': 'Android:///127.0.0.1:7555',
    'ios_device_host': 'iOS:///127.0.0.1:7555',
    'cmd_conf': {
        'url': 'https://oss3.hrgame.com.cn/gmModuleapi/Gmcommand/command',
        'cookie': 'oss3_session=bi1a9blettt7dq1r00gev37j6rgu2e42',
        'platform_id': 14,
        'server_id': 14102992
    }
}


def __get_env_conf():
    env_list = ['PROD', 'TEST', 'PRE']
    if __ENV.upper() not in env_list:
        raise ModuleNotFoundError("不存在的环境")
    if __ENV.upper() == 'TEST':
        return __TEST_CONFIG
    elif __ENV.upper() == 'PRE':
        return __PRE_CONFIG
    else:
        return __PROD_CONFIG


CONF = __get_env_conf()


def __get_result_path():
    dir_name = str(time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time())))
    result_path = os.path.join(os.path.join(BASE_DIR, "report"), dir_name)
    if CONF.get('output'):
        if not os.path.exists(result_path):
            os.mkdir(result_path)
    return result_path


# Path
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
CASE_DIR = os.path.join(BASE_DIR, "tests\\case")
LOG_DIR = os.path.join(BASE_DIR, "report\\logs")
RES_DIR = os.path.join(BASE_DIR, "res")
REPORT_DIR = __get_result_path()


# Device
ANDROID_DEVICE_HOST = CONF.get('android_device_host')
ANDROID_PACKAGE_NAME = 'com.netease.cloudmusic'
IOS_DEVICE_HOST = CONF.get('ios_device_host')
IOS_PACKAGE_NAME = 'com.netease.cloudmusic'


# Log
OUTPUT = CONF.get('output')
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
GM_PLATFORM_ID = CONF['cmd_conf'].get('platform_id')
GM_SERVER_ID = CONF['cmd_conf'].get('server_id')


