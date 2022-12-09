from poco import Poco
from poco.proxy import UIObjectProxy
import warnings
import re
from poco.drivers.android.uiautomation import AndroidUiautomationPoco


identifier: str = '>'
index_compile = re.compile(r'(?<=\[)\d+?(?=\])')


class Poco2(Poco):

    def click(self, pos: str):
        pass


poco = AndroidUiautomationPoco()


class Ark:

    def __init__(self, poco_instance):
        self.poco = poco_instance

    def __call__(self, pos=None, **kwargs):
        if not pos and len(kwargs) == 0:
            warnings.warn("Wildcard selector may cause performance trouble. Please give at least one condition to "
                          "shrink range of results")

        return self.__parser_pos(pos)

    def __parser_pos(self, pos: str):
        if '=' in pos:
            attr, pos = pos.split('=')
            return self.poco(attr=pos)

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


if __name__ == '__main__':
    ark = Ark()