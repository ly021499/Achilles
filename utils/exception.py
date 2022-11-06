
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


class ConnectionError(LRunException):
    """
        This is ConnectError
    """
    pass


class AdbError(LRunException):
    """
        This is AdbError
    """
    pass

