# from typing import Callable
# def print_name(name: str):
#     print(name)
#     return name


# Callable 作为函数参数使用，其实只是做一个类型检查的作用，检查传入的参数值 get_func 是否为可调用对象
# def get_name(get_func: Callable[[str], str]):
#     return get_func
#
#
# vars = get_name(print_name)
# vars("test")


# # 等价写法，其实就是将函数作为参数传入
# def get_name_test(func):
#     return func
#
#
# vars2 = get_name_test(print_name)
# vars2("小菠萝")
