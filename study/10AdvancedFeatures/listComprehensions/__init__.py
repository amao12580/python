l = list(range(1, 100, 2))
print(l)
l2 = [v * v for v in l if v % 3 == 0]
print(l)
print(l2)
