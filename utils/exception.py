

class LRunException(Exception):
    
    raise NotImplementedError


class NoSuchNodeException(LRunException):
    raise NotImplementedError


class InvalidOperationException(LRunException):
    raise NotImplementedError


class TargetTimeout(LRunException):
    raise NotImplementedError
