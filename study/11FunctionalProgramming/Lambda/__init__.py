# 请用匿名函数改造下面的代码：

# -*- coding: utf-8 -*-


def is_odd(x): return x % 2 == 1


print(type(is_odd))
print(is_odd)
L = list(filter(is_odd, range(1, 20)))

print(L)
