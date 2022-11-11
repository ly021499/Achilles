from .logger import log, logwrap, logcase
from .wechat import wechat
from .mail import EMail
from .exception import (InvalidOperationException, AdbError,
                        ConnectError, NoSuchNodeException, InvalidParamError)

import logging

# 设置airtest日志等级，debug会输出很多日志
logger = logging.getLogger("airtest")
logger.setLevel(logging.INFO)
