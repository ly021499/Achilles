import platform
import os

# Device
ANDROID_DEVICE_HOST = 'Android:///127.0.0.1:7555'
ANDROID_PACKAGE_NAME = 'com.netease.cloudmusic'
IOS_DEVICE_HOST = 'iOS:///127.0.0.1:7555'
IOS_PACKAGE_NAME = 'com.netease.cloudmusic'

# Path
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
CASE_DIR = os.path.join(BASE_DIR, "case")
RESULT_DIR = os.path.join(BASE_DIR, "result")
LOG_DIR = os.path.join(BASE_DIR, "result\\logs")

# Wechat
URL = ''
WEBHOOK = ''    # 调试webhook
# WEBHOOK = ''  # 正式webhook

# Other
SYSTEM = platform.system()
ENV = 'prod'

# Log
IS_WRITE = False
LOG_FORMAT = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | " \
             "<green>{level: <8}</green> | " \
             "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - " \
             "<green>{message}</green>"

# Report
TESTER = 'LOUIE'
TITLE = 'Achilles Report'
DESCRIPTION = 'describe: Before the Trojan War broke out, Tethys heard a prophecy about Achilles: ' \
              'he would be famous in history, but he was doomed to die on the battlefield when he was young.'
RERUN = 1

