import platform
import os

# Device
DEVICE_HOST = 'Android:///127.0.0.1:7555'
PACKAGE_NAME = 'com.netease.cloudmusic'

# Path
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
CASE_DIR = os.path.join(BASE_DIR, "case")
RESULT_DIR = os.path.join(BASE_DIR, "result")
LOG_DIR = os.path.join(BASE_DIR, "result\\logs")

# WeboHook
WEBHOOK = ''    # 调试webhook
# WEBHOOK = ''  # 正式webhook

# Other
SYSTEM = platform.system()
ENV = 'prod'

# Log
IS_WRITE = False
