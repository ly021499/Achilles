# @Time   : 2022/11/10 10:42
# @Author : LOUIE
# @Desc   : to do something ...
from utils.exception import InvalidParamError
import re


def __format_message(msg, standard_msg):
    if msg is None:
        return standard_msg
    return f'{standard_msg} : {msg}'


def __raise_exception(msg=None):
    raise AssertionError(msg)


def assert_equal(first, second, msg=None):

    if not (first and second):
        raise InvalidParamError(f"Invalid parameter .. {(first, second)}")

    if not first == second:
        __raise_exception(__format_message(msg, f'{first} == {second}'))


def assert_not_equal(first, second, msg=None):

    if not (first and second):
        raise InvalidParamError(f"Invalid parameter .. {(first, second)}")

    if not first != second:
        __raise_exception(__format_message(msg, f'{first} != {second}'))


def assert_in(member, container, msg=None):
    if member not in container:
        standard_msg = f'{member} not found in {container}'
        __raise_exception(__format_message(msg, standard_msg))


def assert_not_in(member, container, msg=None):
    if member in container:
        standard_msg = f'{member} unexpectedly found in {container}'
        __raise_exception(__format_message(msg, standard_msg))


def assert_is_none(obj, msg=None):
    if obj is not None:
        standard_msg = f'{obj} is not None'
        __raise_exception(__format_message(msg, standard_msg))


def assert_is_not_none(obj, msg=None):
    if obj is None:
        standard_msg = 'unexpectedly None'
        __raise_exception(__format_message(msg, standard_msg))


def assert_regex(text, expected_regex, msg=None):

    if isinstance(expected_regex, (str, bytes)):
        assert expected_regex, "expected_regex must not be empty."
        expected_regex = re.compile(expected_regex)

    if not expected_regex.search(text):
        standard_msg = f"Regex didn't match: {expected_regex.pattern} not found in {text}"
        __raise_exception(__format_message(msg, standard_msg))


if __name__ == '__main__':
    assert_equal(1, 2)