#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Project Name：  study
   File Name：       __init__.py
   Description :
   Author :              steven
   date：                  2019/3/15
   time：                  9:31
-------------------------------------------------
   Change Activity:
                   2019/3/15:
-------------------------------------------------
"""

' a study.__init__.py module '

__author__ = 'steven'


class Student(object):
    # pass
    def __init__(self, name: str = '', score: float = 0):
        self.name = name
        self.score = score
        pass


test = Student
print(test)
jeff = Student()
print(jeff)
print(jeff.name, jeff.score)

jeff = Student('jeff dan')
print(jeff)
print(jeff.name, jeff.score)

jeff.age = 18
print(jeff)
print(jeff.age)
