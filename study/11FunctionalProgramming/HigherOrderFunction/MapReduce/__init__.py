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
