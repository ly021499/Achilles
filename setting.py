import platform
import os
import time

# Device
ANDROID_DEVICE_HOST = 'Android:///127.0.0.1:7555'
ANDROID_PACKAGE_NAME = 'com.netease.cloudmusic'
IOS_DEVICE_HOST = 'iOS:///127.0.0.1:7555'
IOS_PACKAGE_NAME = 'com.netease.cloudmusic'

# Path
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
CASE_DIR = os.path.join(BASE_DIR, "case\\tests")
LOG_DIR = os.path.join(BASE_DIR, "report\\logs")


def __get_result_path():
    dir_name = str(time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time())))
    result_path = os.path.join(os.path.join(BASE_DIR, "report"), dir_name)
    if not os.path.exists(result_path):
        os.mkdir(result_path)
    return result_path


REPORT_DIR = __get_result_path()


# Wechat
URL = ''
WEBHOOK = ''    # 调试webhook
# WEBHOOK = ''  # 正式webhook

# Other
SYSTEM = platform.system()
ENV = 'prod'

# Log
IS_WRITE = True
LOG_FORMAT = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | " \
             "<green>{level: <8}</green> | " \
             "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - " \
             "<green>{message}</green>"

# Report
TESTER = 'LOUIE'
TITLE = 'Achilles Report'
DESCRIPTION = 'Before the Trojan War broke out, Tethys heard a prophecy about Achilles'
RERUN = 1

if __name__ == '__main__':
    print(REPORT_DIR)