# @Time   : 2022/11/10 19:05
# @Author : LOUIE
# @Desc   : 日志工具
import random

from loguru import logger
from typing import Callable
from setting import REPORT_DIR, OUTPUT, LOG_FORMAT
import functools
import time
import os

import logging

# 设置airtest日志等级，debug会输出很多日志
air_logger = logging.getLogger("airtest")
air_logger.setLevel(logging.ERROR)


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

        if OUTPUT:
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

    def random_emoji(self):
        emoji = '🍇🍈🍉🍊🍋🍌🍍🥭🍎🍏🍑🍒🍓🥝🍅🥥🥑🍆🥔🥕🌽🥒🥬🥦🧄🧅🍄🎃🎄🎆🎇🧨✨🎈🎉🎊🎋🎍🎎🎏🍖🍗🥩🥓🍔🍟🍕'
        return random.choice(emoji)

    def step(self, msg):
        logger.info(f'{" ".join(self.random_emoji() * 2)} ：{msg}')

    def info(self, msg):
        logger.info(msg)

    def debug(self, msg):
        logger.debug(msg)

    def warn(self, msg):
        logger.warning(f'{" ".join(self.random_emoji() * 2)} ：{msg}')

    def error(self, msg):
        logger.error(f'😈 😈 ：{msg}')

    def wrap(self, msg: str = None) -> Callable:
        """
        函数日志装饰器
        :param msg: 消息内容
        :return:
        """
        def wrapper(func):
            @functools.wraps(func)
            def inner(*args, **kwargs):
                start_time = time.time()
                res = func(*args, **kwargs)
                end_time = time.time()
                duration = round(end_time - start_time, 2)
                self.step(f"{msg} - func: {func.__name__} - duration: {duration} s")
                return res
            return inner
        return wrapper

    def case(self, func: Callable[[str], str]) -> Callable:
        """
        测试用例日志装饰器
        :param func: 用例函数对象
        :return:
        """
        @functools.wraps(func)
        def inner(*args, **kwargs):
            self.step(f"Start running testcase: {func.__name__}")
            start_time = time.time()
            res = func(*args, **kwargs)
            end_time = time.time()
            duration = round(end_time - start_time, 2)
            self.step(f"End running testcase : {func.__name__} [ Case duration: {duration} s ]")
            self.step(f"{'- ' * 16} 分割线 {' -' * 16}")
            return res
        return inner


log = Logger()


if __name__ == '__main__':
    log.error('aaaa')
    log.step('aaaa')

    @log.case
    def test():
        log.debug(111)

    test()

