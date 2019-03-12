l = [x + 1 for x in range(1, 100) if x % 2 == 0]
print(type(l))
print(l)

l2 = (x + 1 for x in range(1, 100) if x % 2 == 0)
print(type(l2))
print(l2)
print(next(l2))
print(next(l2))
print(next(l2))
print(next(l2))

print('----------------')
for x in l2:
    print(x)


def fib(n: int = 1):
    r = []
    left, right, c = 0, 1, 1
    while c <= n:
        print(right)
        r.append(right)
        left, right, c = right, left + right, c + 1
    return r


'''
a, b = b, a + b
相当于：

t = (b, a + b) # t是一个tuple
a = t[0]
b = t[1]
'''

fib(10)


# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：


def fib_2(n: int = 1):
    left, right, c = 0, 1, 1
    while c <= n:
        yield right
        left, right, c = right, left + right, c + 1


print(type(fib()))  # <class 'list'>

print(type(fib_2()))  # <class 'generator'>

for x in fib(12):
    print(x)

for x in fib_2(12):
    print(x)
