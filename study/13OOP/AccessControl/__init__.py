#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Project Name：  study
   File Name：       __init__.py
   Description :
   Author :              Steven Cheng 
   date：                  2019/3/18
   time：                  19:07
-------------------------------------------------
   Change Activity:
                   2019/3/18:
-------------------------------------------------
"""

' a study.__init__.py module '

__author__ = 'steven'


class Student:

    def __init__(self, name: str = '', score: float = 0):
        self.tittle = 'this is a tittle'  # public
        self.__name = name  # private
        self.__score = score  # private
        self._age = 28  # protected
        self.__sign__ = name + ' Hello world.'  # public

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def get_age(self):
        return self._age

    def get_sign(self):
        return self.__sign__


lisa = Student('lisa li', 88.78)
print(lisa.tittle)
# print(lisa.__name)
print(lisa.get_name())
print(lisa.get_score())
print(lisa.get_age())
print(lisa._age)
print(lisa.__sign__)
print(lisa.get_sign())
