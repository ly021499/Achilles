# @Time   : 2022/11/10 19:05
# @Author : LOUIE
# @Desc   : 日志工具

from loguru import logger
from typing import Callable
from setting import REPORT_DIR, IS_WRITE, LOG_FORMAT
import functools
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
            all_log_path = os.path.join(REPORT_DIR, "all.log")
            logger.add(all_log_path,     # 日志存放位置
                       retention=7,      # 清理周期
                       level="DEBUG",     # 日志级别
                       enqueue=True,      # 具有使日志记录调用非阻塞的优点
                       encoding="utf-8",
                       format=LOG_FORMAT
                       )
            error_log_path = os.path.join(REPORT_DIR, "error.log")
            logger.add(error_log_path,
                       retention=7,
                       level="ERROR",
                       enqueue=True,
                       encoding="utf-8",
                       format=LOG_FORMAT
                       )

    def get_logger(self) -> logger:
        return logger


log = Logger().get_logger()     # 日志记录器


def logwrap(msg: str = None) -> Callable:
    """
    日志装饰器，简单记录函数的日志

    Args:
        msg (function): 函数
    """
    def wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            start_time = time.time()
            res = func(*args, **kwargs)
            end_time = time.time()
            duration = round(end_time - start_time, 2)
            log.debug(f"📣 📣 📣  {msg}  ... [ Func: {func.__name__} - Duration: {duration} ]")
            return res
        return inner
    return wrapper


def logcase(func: Callable[[str], str]) -> Callable:
    @functools.wraps(func)
    def inner(*args, **kwargs):
        log.info(f"(`･ω･´)ゞ  Start of running testcase: {func.__name__}")
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        duration = round(end_time - start_time, 2)
        log.info(f"(ง •̀_•́)ง  End of running testcase : {func.__name__} ... [ Case duration: {duration} ]")
        log.info(f"{'- ' * 16} 分割线 {' -' * 16}")
        return res
    return inner


if __name__ == '__main__':
    # 测试代码
    log.info(1111)
    log.warning(1111)
    log.critical(1111)
    log.error(1111)
    log.debug(1111)

    @logcase
    @logwrap('hello louie')
    def login(username, password):
        print(username, password)
        return object

    login('louie', '123')
