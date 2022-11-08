from .logger import log, logwrap, logcase
from .wechat import wechat
from .email import EMail
from .exception import InvalidOperationException, AdbError, ConnectError, NoSuchNodeException
import logging

logger = logging.getLogger("airtest")
logger.setLevel(logging.INFO)   # 设置airtest日志等级，dbeug会输出很多日志
