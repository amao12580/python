# 必选参数、默认参数、可变参数、关键字参数

# 位置参数，必须按照定义的顺序、格式、个数，进行输入

# 默认参数,必选参数在前，默认参数在后.函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。

# 可变参数，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个

# 关键字参数，可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。

def power(x: float, n: int = 2):
    if n <= 0:
        raise ValueError('n must greater than zero.')
    r = 1
    while n > 0:
        n = n - 1
        r = r * x
    return r


# print(power(2, -23))
print(power(2))
print(power(2, 10))
print(power(12, 10))


def student(name: str, city: str, age: int = 12, sex: str = '男'):
    print(name, city, age, sex)


student('张三', '上海市')
student('李四', '天津市', sex='女')
student('王五', '青岛市', 15, '无')
student('赵六', '东莞市', 17, )
student('李七', '中山市', age=18, sex='女')


def tail(L=None):
    if L is None:
        L = []
    L.append('end')
    print(L)


tail()
tail()
tail()
l = ['abc', 'bcd', 'def']
tail(l)
tail(l)
tail(l)


def sum(f: float = 3.141592654, *items):
    if items is None:
        raise ValueError('items must not null.')
    s = 0
    print(f)
    print(items.__class__)
    for item in items:
        if item is None:
            raise ValueError('item must not null.')
        if not isinstance(item, (float, int)):
            raise ValueError('item must be num.', item)
        s = s + item
    print(s)
    s = s * f
    print(s)
    return s


# sum(3, (1, 2, 1234))
sum(*(1, 2, 1234))
sum(4, *(1, 2, 1234))
# sum(*(1, 2, 1234, '1234'))
sum(*range(1, 12))
