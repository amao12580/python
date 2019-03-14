# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。

def test():
    return lambda x=10, y=4, z=3.141592654: z * pow(x, y)


print(test())
print(test)
# print(test()())
# print(test(2, 10, 8))
print(test()(2, 10, 8))

import functools


def my_max(*args: int):
    print(args)
    return max(args)


my_max_v2 = functools.partial(my_max, 10, 12, 13)
print(my_max_v2(*range(12)))
