# @Time   : 2022/11/10 10:42
# @Author : LOUIE
# @Desc   : 断言方法
from utils.exception import InvalidParamError
import re


def __format_message(msg, standard_msg):
    """
    格式化消息体
    :param msg: 自定义消息
    :param standard_msg: 固定消息
    :return:
    """
    if msg is None:
        return standard_msg
    return f'{standard_msg} : {msg}'


def __raise_exception(msg=None):
    """
    抛出异常
    :param msg:
    :return:
    """
    raise AssertionError(msg)


def assert_equal(first, second, msg=None):
    """

    :param first: 第一个值
    :param second: 第二个值
    :param msg: 消息
    :return:
    """
    if not (first and second):
        raise InvalidParamError(f"Invalid parameter .. {(first, second)}")

    if not first == second:
        __raise_exception(__format_message(msg, f'{first} == {second}'))


def assert_not_equal(first, second, msg=None):
    """

    :param first: 第一个值
    :param second: 第二个值
    :param msg: 消息
    :return:
    """

    if not (first and second):
        raise InvalidParamError(f"Invalid parameter .. {(first, second)}")

    if not first != second:
        __raise_exception(__format_message(msg, f'{first} != {second}'))


def assert_in(member, container, msg=None):
    """
    断言成员存在于集合中
    :param member: 成员
    :param container: 集合
    :param msg: 消息
    :return:
    """
    if member not in container:
        standard_msg = f'{member} not found in {container}'
        __raise_exception(__format_message(msg, standard_msg))


def assert_not_in(member, container, msg=None):
    """
    断言成员不存在于集合中
    :param member: 成员
    :param container: 集合
    :param msg: 消息
    :return:
    """
    if member in container:
        standard_msg = f'{member} unexpectedly found in {container}'
        __raise_exception(__format_message(msg, standard_msg))


def assert_is_none(obj, msg=None):
    """
    断言是否为None
    :param obj: 对象
    :param msg: 消息
    :return:
    """
    if obj is not None:
        standard_msg = f'{obj} is not None'
        __raise_exception(__format_message(msg, standard_msg))


def assert_is_not_none(obj, msg=None):
    """
    断言是否不为None
    :param obj: 对象
    :param msg: 消息
    :return:
    """
    if obj is None:
        standard_msg = 'unexpectedly None'
        __raise_exception(__format_message(msg, standard_msg))


def assert_regex(text, expected_regex, msg=None):
    """
    断言正则匹配文本
    :param text: 匹配文本
    :param expected_regex: 正则
    :param msg: 消息
    :return:
    """

    if isinstance(expected_regex, (str, bytes)):
        assert expected_regex, "expected_regex must not be empty."
        expected_regex = re.compile(expected_regex)

    if not expected_regex.search(text):
        standard_msg = f"Regex didn't match: {expected_regex.pattern} not found in {text}"
        __raise_exception(__format_message(msg, standard_msg))


if __name__ == '__main__':
    assert_equal(1, 2)