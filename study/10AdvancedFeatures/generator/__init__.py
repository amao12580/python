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
