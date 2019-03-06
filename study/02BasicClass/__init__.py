#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码
'''

# 开始学习一些python编程基础

# 1.基本的流程控制语句
# 每一行都是一个语句，当语句以冒号:结尾时，缩进的语句视为代码块。
price = int(input("please enter apple price.\n"))
print("your price", price)
if price > 0:
    print("accept.")
else:
    print("reject.")

print("////t//n")

print("\\t\\n\\\\")
print("\\\t\\\n\\\\")

print('''
114
147
963
''')

# 2.动态语言

a = 123
b = True
print(a)
print(b)

a = "123"
b = 123
print(a)
print(b)

c = 1234567890
print(c)

# 3.字符编码

print("测试中文输出", "ABCDEFGHIJKLMN", "1243343434")

print(len("我是中文"))

print(len("我是中文".encode("utf-8")))

print("我是中文".encode("utf-8"))

print("我是中文".encode("utf-8").decode("utf-8"))

# 4.格式化

print('Hi, %s, you have $%d.' % ('Michael', 1000000))

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
