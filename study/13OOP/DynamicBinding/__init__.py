#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Project Name：  study
   File Name：       __init__.py
   Description :
   Author :              Steven Cheng 
   date：                  2019/3/19
   time：                  14:00
-------------------------------------------------
   Change Activity:
                   2019/3/19:
-------------------------------------------------
"""

' a study.__init__.py module '

__author__ = 'steven'


# 动态绑定

class Student:
    def __init__(self):
        self.age = 18

    pass


# 属性
# 区分实例属性和类属性
lisa = Student()

jeff = Student()

lisa.name = 'list wang'

print(lisa.name)
# print(jeff.name)  # AttributeError: 'Student' object has no attribute 'name'

lisa.age = 28
jeff.age = 79
print(lisa.age)
print(jeff.age)


# 预定义属性元组

class Student:
    __slots__ = ('name', 'age', 'sex')

    def __init__(self):
        self.name = 'No Name'
        self.age = 18
        self.sex = '男'

    def __str__(self):
        return 'name:' + self.name + ',age:' + str(self.age) + ',sex:' + self.sex

    pass


lisa = Student()
print(lisa)
# lisa.tittle='No tittle'#AttributeError: 'Student' object has no attribute 'tittle'

# 方法
# 区分实例方法和类方法


# 属性的getter setter
