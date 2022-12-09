# @Time   : 2022/11/2 21:05
# @Author : LOUIE
# @Desc   : 自定义异常类

class LRunException(Exception):

    pass


class NoSuchNodeException(LRunException):
    """
    This is NoSuchNodeException
    """
    pass


class InvalidOperationException(LRunException):
    """
    This is InvalidOperationException
    """
    pass


class TargetTimeout(LRunException):
    """
    This is TargetTimeout
    """
    pass


class ConnectError(LRunException):
    """
    This is ConnectError
    """
    pass


class AdbError(LRunException):
    """
    This is AdbError
    """
    pass


class InvalidParamError(LRunException):
    """
    This is InvalidParamError
    """
    pass

