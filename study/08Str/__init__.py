# str 不可变类型 指针引用
a = 'abc'
b = "abc"
print(a == b)

print(a.__eq__(b))

c = a.zfill(10)
print(a)
print(c)
d = b.replace('bc', 'bcdef')
print(b)
print(d)

# e = d.replace('f', 123.25)  # 替换类型需要是str
# print(d)
# print(e)
