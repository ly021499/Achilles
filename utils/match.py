# @Time   : 2022/11/4 15:46
# @Author : LOUIE
# @Desc   : 邮件发送

import re


def __search(regex, string):
    _compile = re.compile(f'{regex}')
    match_obj = _compile.search(string)
    if match_obj:
        return match_obj.group()
    return None


def match_index(string: str):
    """
    正则匹配定位的下标
    :param string:
    :return:
    """
    return __search(r'=\[)\d+?(?=(?<\])', string)


def match_number(string: str):
    return __search(r'\d+', string)



