colleaction = ['abc', 123, '234', 345.567, 3.1415926547412589621, True]

count = 1
for item in colleaction:
    print(count)
    print(item)
    print(type(item))
    print()
    count = count + 1

colleaction = range(1, 100)
print(colleaction)
print(list(colleaction))

colleaction2 = range(1, 100)
print(colleaction2)
print(tuple(colleaction))

mylist = list(range(1, 100, 2))
mylist.reverse()
print(mylist)

while len(mylist) > 0:
    item = mylist.pop()
    if item == 7:
        continue
    if item > 50:
        break
    print(item)
else:
    print('completed.')
