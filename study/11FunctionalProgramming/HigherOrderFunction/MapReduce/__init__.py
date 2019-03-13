from functools import reduce

# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

# print(chr(65))
# print(chr(97))

lower = {}
upper = {}


def init_one_metadata(n: int):
    if n <= 0:
        raise ValueError('n must greater than zero.')
    upper[n] = chr(n)
    n = n + 32
    lower[n] = chr(n)


def init_metadata():
    list(map(init_one_metadata, range(65, 91)))
    # print(lower)
    # print(upper)


init_metadata()


def normalize(name: str):
    if name is None or name == '':
        return name
    return name[0].upper() + name[1:]


# 测试:
L1 = ['a', 'B', 'adam', 'LISA', 'barT']

# print(normalize(L1[0]))
L2 = list(map(normalize, L1))
print(L2)


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：

def prod(l):
    if l is None:
        raise ValueError('l can not be null.')
    if len(l) == 0:
        return 0
    return reduce(multiply, l)


def multiply(x: float, y: float):
    return x * y


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
