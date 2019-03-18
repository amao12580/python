#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Project Name：  study
   File Name：       __init__.py
   Description :
   Author :              Steven Cheng 
   date：                  2019/3/18
   time：                  19:28
-------------------------------------------------
   Change Activity:
                   2019/3/18:
-------------------------------------------------
"""

' a study.__init__.py module '

__author__ = 'steven'


class Animal:
    _name = 'no name'

    def __init__(self):
        self._name = 'animal'

    def sing(self):
        print(self._name, ' is sing.')


class Cat(Animal):
    def __init__(self):
        self._name = 'cat'
        super(Animal, self).__init__()


class Duck:
    _name = 'no name'

    def sing(self):
        self._name = 'duck'
        print(self._name, ' is sing.')


animal = Animal()
animal.sing()
animal2 = Cat()
animal2.sing()

print(isinstance(animal, Animal))
print(isinstance(animal2, Animal))
print(isinstance(animal2, Cat))
print(isinstance(animal, Cat))

duck = Duck()

duck.sing()
