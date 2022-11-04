import platform
import os

# Path
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
CASE_DIR = os.path.join(BASE_DIR, "case")
REPORT_DIR = os.path.join(BASE_DIR, "report")
LOG_DIR = os.path.join(BASE_DIR, "report\\logs")

# WeboHook
WEBHOOK = ''    # 调试webhook
# WEBHOOK = ''  # 正式webhook

# Other
SYSTEM = platform.system()
ENV = 'prod'

# Log
IS_WRITE = False
