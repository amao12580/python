# 官方 python 3 的函数 doc  https://docs.python.org/3/library/functions.html
print(pow(3, 2))
print(pow(3, 3))
print(pow(3, 4))
area = 3.141592654 * pow(3, 2)
print(area)

a = abs  # 变量a指向abs函数
print(a(-1))  # 所以也可以通过a调用abs函数


def my_abs_v1(var):
    if not isinstance(var, (int, float)):
        raise TypeError('bad type', var, var.__class__)
    if var >= 0:
        return var
    else:
        return -var


print(my_abs_v1(-125))
print(my_abs_v1(1205))


# print(my_abs_v1('1258'))


def nothing(var):
    print(var)
    pass
    print(var)
    return
    pass
    print(var)


nothing('234')


def multiple(var):  # 函数可以同时返回多个值，实质上还是一个值，用元组封装了
    print(var)
    return var, -var, range(1, 10, 2)


print(multiple(100))
