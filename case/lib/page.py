# @Time   : 2022/11/14 15:47
# @Author : LOUIE
# @Desc   : to do something ...
import re
import time
from utils import log, NoSuchNodeException
from poco.exceptions import PocoNoSuchNodeException
from case.lib.driver.android_app import get_android_poco_instance


class Page(object):

    def __init__(self, poco_instance):
        self.poco = poco_instance or get_android_poco_instance()
        self.identifier: str = '>'
        self.index_compile = re.compile(r'(?<=\[)\d+?(?=\])')
        self.chinese_compile = re.compile(r'^(?![a-z|A-Z|0-9])+?')

    def click(self, pos, focus=None, sleep_interval=None):
        try:
            return self.__parser_pos(pos).click(focus, sleep_interval)
        except PocoNoSuchNodeException:
            try:
                time.sleep(1)
                log.debug(f"Try again, locate node：{pos}")
                return self.__parser_pos(pos).click(focus, sleep_interval)
            except PocoNoSuchNodeException:
                raise NoSuchNodeException(f'Cannot find visible node by query UIObjectProxy of "{pos}"')

    def exists(self, pos):
        return self.__parser_pos(pos).exists()

    def long_click(self, pos, duration=2.0):
        return self.__parser_pos(pos).long_click(duration)

    def double_click(self, pos, focus=None, sleep_interval=None):
        return self.__parser_pos(pos).double_click(focus, sleep_interval)

    def rclick(self, pos, focus=None, sleep_interval=None):
        return self.__parser_pos(pos).rclick(focus, sleep_interval)

    def swipe(self, pos, direction, focus=None, duration=0.5):
        return self.__parser_pos(pos).swipe(direction, focus, duration)

    def scroll(self, pos, direction='vertical', percent=0.6, duration=2.0):
        return self.__parser_pos(pos).scroll(direction, percent, duration)

    def pinch(self, pos, direction='in', percent=0.6, duration=2.0, dead_zone=0.1):
        return self.__parser_pos(pos).pinch(direction, percent, duration, dead_zone)

    def set_text(self, pos, text):
        print(self.__parser_pos(pos).get_text())
        return self.__parser_pos(pos).set_text(text)

    def get_text(self, pos):
        return self.__parser_pos(pos).get_text()

    def get_name(self, pos):
        return self.__parser_pos(pos).get_name()

    def sleep(self, secs: float = 1.0):
        log.debug(f"sleep {secs} seconds .")
        time.sleep(secs)

    def __regex_pos_index(self, pos: str):
        """
        正则匹配定位的下标
        :param pos:
        :return:
        """
        s = self.index_compile.search(pos)
        if s:
            index = s.group()
            rep_pos = pos.replace(f"[{index}]", "")
            print(f'replace index: {index}')
            return rep_pos, int(index)
        return pos, 0

    def __parser_pos(self, pos: str):
        """
        解析pos定位
        传入的pos为中文时，使用text文本定位，不以中文开头不会匹配text文本
        传入的pos为元素时，使用普通方式定位，并且当存在多个定位时，使用 & 符号连结，程序自动拆解，并自动解析index
        :param pos: 定位
        :return:
        example：
            原生定位："Btn_Enter"
            索引定位："Bg_Front[1]"
            双级定位: "Bg_Front[1]>Close"
            特殊定位："text=确定"
        """
        if '=' in pos:
            pos_type, pos = pos.split('=')
            if pos_type in ['texture', 'text']:
                print(f"keyword：self.poco({pos_type}={pos})")
                return self.poco(**{pos_type: pos})
            raise TypeError("Position type error . type : [texture、text]")

        if self.identifier not in pos:

            if self.index_compile.search(pos):
                rep_pos, index = self.__regex_pos_index(pos)
                print(f"index pos: self.poco('{rep_pos}')[{index}]")
                return self.poco(rep_pos)[index]

            print(f"raw pos: self.poco('{pos}')")
            return self.poco(pos)

        value_list = pos.split(self.identifier)
        pos_list = [self.__regex_pos_index(value) for value in value_list]

        p0, n0 = pos_list[0]
        p1, n1 = pos_list[1]

        print(f"split pos: self.poco('{p0}')[{n0}].child('{p1}')[{n1}]")

        return self.poco(p0)[n0].child(p1)[n1]





















