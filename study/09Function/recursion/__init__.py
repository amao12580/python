import sys


def recursion(n: int = 1):
    if n == 1:
        return n
    return n * recursion(n - 1)


print(sys.getrecursionlimit())  # 获取系统的递归深度设置
print(recursion(5))
print(recursion(10))
print(recursion(100))
print(recursion(998))


# print(recursion(1000))


def recursion_v2(n: int = 1):
    return recursion_inter(n, 1)


# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
def recursion_inter(num, product):
    if num == 1:
        return product
    return recursion_inter(num - 1, num * product)  # 尾递归，解决深度递归爆栈


print(recursion_v2(5))
print(recursion_v2(10))
print(recursion_v2(100))


# print(recursion_v2(998))
# print(recursion_v2(1000))

# !/usr/bin/env python2.4
# This program shows off a python decorator(
# which implements tail call optimization. It
# does this by throwing an exception if it is
# it's own grandparent, and catching such
# exceptions to recall the stack.


class TailRecurseException:
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs


def tail_call_optimized(g):
    """
    This function decorates a function with tail call
    optimization. It does this by throwing an exception
    if it is it's own grandparent, and catching such
    exceptions to fake the tail call optimization.

    This function fails if the decorated
    function recurses in a non-tail context.
    """

    def func(*args, **kwargs):
        f = sys._getframe()
        # 为什么是grandparent, 函数默认的第一层递归是父调用,
        # 对于尾递归, 不希望产生新的函数调用(即:祖父调用),
        # 所以这里抛出异常, 拿到参数, 退出被修饰函数的递归调用栈!(后面有动图分析)
        if f.f_back and f.f_back.f_back \
                and f.f_back.f_back.f_code == f.f_code:
            # 抛出异常
            raise TailRecurseException(args, kwargs)
        else:
            while True:
                try:
                    return g(*args, **kwargs)
                except TailRecurseException as e:
                    # 捕获异常, 拿到参数, 退出被修饰函数的递归调用栈
                    args = e.args
                    kwargs = e.kwargs

    func.__doc__ = g.__doc__
    return func


@tail_call_optimized
def factorial(n, acc=1):
    "calculate a factorial"
    if n == 0:
        return acc
    return factorial(n - 1, n * acc)


print(factorial(10000))
