# 列表 list

list0 = [1, 23, 4, 5, 7]

print(list0)

print(len(list0))

print(list0.index(4))
print(list0.index(7))

print(list0.__getitem__(0))
print(list0.__getitem__(1))

print(list0[0])
print(list0[1])

print(len(str(list0[1])))

list0.sort()
print(list0)

list1 = ['123', 123, True, 123.001]

print(list1)

print(list1[1] > 100)

print(list1[2] > 100)

print((list1[2]))

print(bool(list1[2]))

print(not bool(list1[2]))

list1 = [False, 123, True, 123.001]

print(list1)

list1[1] = '123'

list1.append('234')

print(list1)

print(list1[2])

# 元组

tuple0 = (1,)

print(tuple0)

print(tuple0[0])

tuple1 = (1, '2', False)

print(tuple1)

print(tuple1[0])

# 相互转换

list2 = list(tuple0)

print(list2)

tuple2 = tuple(list1)

print(tuple2)
