#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Project Name：  study
   File Name：       __init__.py
   Description :
   Author :              steven
   date：                  2019/3/14
   time：                  21:12
-------------------------------------------------
   Change Activity:
                   2019/3/14:
-------------------------------------------------
"""

' a study.__init__.py module '

__author__ = 'steven'


class Student(object):
    def __init__(self, name: str, score: float):
        self.name = name
        self.score = score

    def print(self):
        print('name:' + self.name + ',score=' + str(self.score))


jeff = Student('Jeff Dan', 85.69)
bob = Student('Bob Jean', 105.659)

jeff.print()
bob.print()
