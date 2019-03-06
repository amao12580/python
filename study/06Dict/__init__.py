myDict = {'a': 23, 'b': 34, 'c': 45}
print(myDict)
for key in myDict:
    print(type(key))
    print(key, myDict.get(key))

print('c' in myDict)
print(myDict.__contains__('c'))
print('d' in myDict)
print(myDict.__contains__('d'))

myDict.pop('c')
myDict['e'] = 567
myDict[234] = 5670
print(myDict)
print(len(myDict))
