l = list(range(1, 10))

for item in l:
    print(item + 1)

d = dict({1: 2, 2: 3, 4: 5, 6: 7, 7: 8})

for k, v in d.items():
    print(k, v)

for k in d.keys():
    print(k, d.get(k))

for v in d.values():
    print(v)

s = 'abcdefghijklmn'
for c in s:
    print(c)

# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
from collections import Iterable

print(isinstance('abc', Iterable))  # str是否可迭代
print(isinstance([1, 2, 3], Iterable))  # list是否可迭代
print(isinstance(123, Iterable))  # 整数是否可迭代

for i, v in enumerate(l):  # 生成下标值
    print(i, v)

for i, v in enumerate(s):  # 生成下标值
    print(i, v)
