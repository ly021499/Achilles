# @Time   : 2022/11/2 19:05
# @Author : LOUIE
# @Desc   : 日志工具

from loguru import logger
from setting import LOG_DIR, IS_WRITE
import time
import os


class Logger:

    """
    通过单例模式，只实例化一个日志对象
    直接调用log实例对象进行日志调用
    """
    
    def __new__(cls, *args, **kwargs):
        
        if not hasattr(cls, '_instance'):
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        """
        添加日志记录器，写入文件
        日志分类型存储，一份完整日志，一份错误日志
        通过读取配置文件中的 IS_WRITE 判断是否需要写入文件，便于调试
        """
        date = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))

        if IS_WRITE:
            all_log_path = os.path.join(LOG_DIR, "all") + "/" + date + ".log"
            logger.add(all_log_path,     # 日志存放位置
                       retention=7,      # 清理周期
                       level="INFO",     # 日志级别
                       enqueue=True,      # 具有使日志记录调用非阻塞的优点
                       encoding="utf-8"
                       )
            error_log_path = os.path.join(LOG_DIR, "error") + "/" + date + ".log"
            logger.add(error_log_path,
                       retention=7,
                       level="ERROR",
                       enqueue=True,
                       encoding="utf-8"
                       )

    def get_logger(self) -> logger:
        return logger


log = Logger().get_logger()


if __name__ == '__main__':
    log.info(1111)
    log.warning(1111)
    log.critical(1111)
    log.error(1111)
    log.debug(1111)