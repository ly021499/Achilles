# @Time   : 2022/11/14 15:47
# @Author : LOUIE
# @Desc   : to do something ...


class Page(object):

    def __init__(self, poco_instance):
        self.poco = poco_instance

        def parser(pos):
            value_list = pos.split('/')
            pos_list = []
            for value in value_list:
                recompile = re.compile(r'(?<=\[)\d+?(?=\])')
                s = recompile.search(value)
                if s:
                    index = s.group()
                    rep_pos = value.replace(f"[{index}]", "")
                else:
                    index = 0
                pos_list.append([rep_pos, index])
            return pos_list

    def poco(self):
        pass


class AndroidPage(Page):

    def __init__(self):
        super().__init__()