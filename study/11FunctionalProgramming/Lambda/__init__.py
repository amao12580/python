f = lambda x, y: (x + 1) / (y + x * 5)
# f=lambda x:x+1
print(f.__name__)
print(f(1, 3))

# 请用匿名函数改造下面的代码：

# -*- coding: utf-8 -*-


is_odd = lambda x: x % 2 == 1

print(type(is_odd))
print(is_odd)
L = list(filter(lambda x: x % 2 == 1, range(1, 20)))

print(L)
