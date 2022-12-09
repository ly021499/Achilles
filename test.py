from poco import Poco
from poco.proxy import UIObjectProxy
import warnings
import re

identifier: str = '>'
index_compile = re.compile(r'(?<=\[)\d+?(?=\])')


class Poco2(Poco):

    def click(self, pos: str):
        pass


class Ark:

    def __call__(self, poco, name=None, **kwargs):
        if not name and len(kwargs) == 0:
            warnings.warn("Wildcard selector may cause performance trouble. Please give at least one condition to "
                          "shrink range of results")

        position = self.__parser_pos(name)

        return UIObjectProxy(poco, position, **kwargs)

    def __parser_pos(self, pos: str):
        if '=' in pos:
            attr, pos = pos.split('=')
            return UIObjectProxy(attr=pos)

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
    a = b = []
    a.append(1)
    b.append(2)
    print(a)
    print(b)
