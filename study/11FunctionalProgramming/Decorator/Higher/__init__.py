# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：

import functools
import inspect
import time
from inspect import isfunction


def log(func):
    def wrapper(*args, **kw):
        print('call %s() %s:' % (func.__name__, time.time()))
        return func(*args, **kw)

    return wrapper


# @log
def metric(text):
    def decorator(fn):
        print(inspect.signature(fn))
        print(inspect.signature(fn).parameters)

        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            ticks = time.time()
            print(args, kwargs)
            # new_args = list(args)
            # new_args.insert(0, 'AAA')
            # new_args.append('BBB')
            # new_args = tuple(new_args)
            # kwargs['abc'] = 12345
            # print(new_args, kwargs)

            r = fn(*args, **kwargs)
            # r = fn(*new_args, **kwargs)
            # r = fn(*args)
            message = ''
            if type(text) is str:
                message = text + ' '
            print('%s%s executed in %s ms' %
                  (message, fn.__name__, int((time.time() - ticks) * 1000)))
            return r

        return wrapper

    if type(text) is str:
        return decorator
    elif isfunction(text):
        return decorator(text)
    return decorator


@metric
def fast(x, y):
    print(x, y)
    time.sleep(0.0012)
    return x + y


# 测试


@metric('aaa')
def slow(x, y, z):
    print(x, y, z)
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
