# @Time   : 2022/11/14 15:47
# @Author : LOUIE
# @Desc   : to do something ...
import re


class Page(object):

    def __init__(self, poco_instance):
        self.poco = poco_instance
        self.identifier: str = '&'
        self.index_compile = re.compile(r'(?<=\[)\d+?(?=\])')
        self.chinese_compile = re.compile(r'^(?![a-z|A-Z|0-9])+?')

    def click(self, pos, focus=None, sleep_interval=None):
        return self.__parser_pos(pos).click(focus, sleep_interval)

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
            return rep_pos, int(index)
        return pos, 0

    def __parser_pos(self, pos: str):
        """
        解析pos定位
        传入的pos为中文时，使用text文本定位，不以中文开头不会匹配text文本
        传入的pos为元素时，使用普通方式定位，并且当存在多个定位时，使用 & 符号连结，程序自动拆解，并自动解析index
        :param pos: 定位
        :return:
        """

        if self.chinese_compile.match(pos):
            return self.poco(text=pos)

        if self.identifier not in pos:

            if self.index_compile.search(pos):
                rep_pos, index = self.__regex_pos_index(pos)
                return self.poco(rep_pos)[index]

            return self.poco(pos)

        value_list = pos.split(self.identifier)

        pos_list = []
        for value in value_list:
            pos_list.append(self.__regex_pos_index(value))

        p0, n0 = pos_list[0]
        p1, n1 = pos_list[1]

        return self.poco(p0)[n0].child(p1)[n1]





















