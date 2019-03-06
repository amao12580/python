# 有同学问，能不能像.exe文件那样直接运行.py文件呢？在Windows上是不行的，但是，在Mac和Linux上是可以的，方法是在.py文件的第一行加上一个特殊的注释：

# !/usr/bin/env python3
name = input("Please enter your name.\n");
print("Hello", name);
varA = 100 + 200;
varB = 582 * 410;
print("Hello world!");
print(varA);
print(varB);
print(varA + varB);
print(2 << 10);
print(2 >> 10);
print(2 ** 10);
