set1 = {12, 14, 12, 25, 69}
print(set1)

set1.add(12)
set1.add(123)
print(set1)
set1.remove(12)

for item in set1:
    print(item)

set2 = {12, 25, 456}

set3 = set1 & set2  # 交集
print(set3)
set4 = set1 | set2  # 并集
print(set4)
