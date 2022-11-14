# @Time   : 2022/11/10 15:17
# @Author : LOUIE
# @Desc   : to do something ...
import re

pre_env = 'Env 2[1]/Texture_Check[10]'


def poco(pos):
    print(pos)


def parser_pos(pos):
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

parser(pre_env)



















