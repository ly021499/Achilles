# @Time   : 2022/11/14 15:47
# @Author : LOUIE
# @Desc   : 基于poco对象、airtest二次封装的操作方法

from utils import log, logstep, NoSuchNodeException
from poco.exceptions import PocoNoSuchNodeException, PocoTargetRemovedException
from tests.lib.driver.android_app import get_android_poco_instance
import re
import time


identifier: str = '>'
index_compile = re.compile(r'(?<=\[)\d+?(?=\])')


class Page(object):

    def __init__(self, poco_instance):
        self.poco = poco_instance or get_android_poco_instance()

    def get_poco(self, pos: str):
        return self.__parser_pos(pos)

    def touch_optional_position(self):
        logstep("点击任意位置继续 ...")
        return self.poco.click([0.2, 0.82])

    def click(self, pos: str, focus=None, sleep_interval: float = None):
        try:
            return self.__parser_pos(pos).click(focus, sleep_interval)
        except PocoNoSuchNodeException:
            try:
                log.debug(f"Try locating the node： {pos} again")
                return self.__parser_pos(pos).click(focus, sleep_interval)
            except PocoNoSuchNodeException:
                raise NoSuchNodeException(f'Cannot find visible node by query UIObjectProxy of "{pos}"')

    def exists(self, pos: str):
        try:
            return self.__parser_pos(pos).exists()
        except (PocoTargetRemovedException, PocoNoSuchNodeException):
            return False

    def long_click(self, pos: str, duration: float = 2.0):
        return self.__parser_pos(pos).long_click(duration)

    def double_click(self, pos: str, focus=None, sleep_interval: float = None):
        return self.__parser_pos(pos).double_click(focus, sleep_interval)

    def rclick(self, pos: str, focus=None, sleep_interval: float = None):
        return self.__parser_pos(pos).rclick(focus, sleep_interval)

    def swipe(self, pos: str, direction: str, focus=None, duration: float = 0.5):
        return self.__parser_pos(pos).swipe(direction, focus, duration)

    def scroll(self, pos: str, direction: str = 'vertical', percent: float = 0.6, duration: float = 2.0):
        return self.__parser_pos(pos).scroll(direction, percent, duration)

    def pinch(self, pos: str, direction: str = 'in', percent: float = 0.6, duration: float = 2.0, dead_zone: float = 0.1):
        return self.__parser_pos(pos).pinch(direction, percent, duration, dead_zone)

    def set_text(self, pos: str, text: str):
        return self.__parser_pos(pos).set_text(text)

    def get_text(self, pos: str):
        return self.__parser_pos(pos).get_text()

    def get_name(self, pos: str):
        return self.__parser_pos(pos).get_name()

    def drag_to(self, pos: str, target: str, duration=0.5):
        return self.__parser_pos(pos).drag_to(self.__parser_pos(target), duration)

    def wait_for_appearance(self, pos, timeout=30):
        return self.__parser_pos(pos).wait_for_appearance(timeout)

    def wait_for_disappearance(self, pos, timeout=30):
        return self.__parser_pos(pos).wait_for_appearance(timeout)

    def sleep(self, secs: float = 1.0):
        logstep(f"sleep {secs} seconds .")
        time.sleep(secs)

    def __regex_pos_index(self, pos: str):
        """
        正则匹配定位的下标
        :param pos:
        :return:
        """
        s = index_compile.search(pos)
        if s:
            index = s.group()
            rep_pos = pos.replace(f"[{index}]", "")
            return rep_pos, int(index)
        return pos, 0

    def __parser_pos(self, pos: str):
        """
        解析pos定位，基于poco定位方式，支持更简便的一行式书写定位方法，支持五种定位方法；
        传入的pos为中文时，使用text文本定位，不以中文开头不会匹配text文本；
        属性定位与正则定位属于同一种书写方式，均采用关键字方式书写，例如：text=确定、textMatches=确定；
        传入的pos为元素时，使用普通方式定位，并且当存在多级定位时，使用 > 符号连结，程序自动拆解，并自动解析index；
        相对定位与顺序定位可结合使用，采用先切割后取值的方式解析定位，例如：Bg_Front[1]>Close；
        :param pos: 定位
        :return:
        example：
            基本定位："Btn_Enter"
            顺序定位："Bg_Front[1]"
            相对定位: "Bg_Front[1]>Close"
            属性定位："text=确定"
            正则定位："textMatches=确定"
        """
        if '=' in pos:
            attr, pos = pos.split('=')
            return self.poco(**{attr: pos})

        if identifier not in pos:
            if index_compile.search(pos):
                rep_pos, index = self.__regex_pos_index(pos)
                return self.poco(rep_pos)[index]

            return self.poco(pos)

        value_list = pos.split(identifier)
        pos_list = [self.__regex_pos_index(value) for value in value_list]

        p0, n0 = pos_list[0]
        p1, n1 = pos_list[1]

        return self.poco(p0)[n0].child(p1)[n1]























