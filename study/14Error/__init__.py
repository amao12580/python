#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Project Name：  study
   File Name：       __init__.py
   Description :
   Author :              Steven Cheng 
   date：                  2019/3/22
   time：                  18:48
-------------------------------------------------
   Change Activity:
                   2019/3/22:
-------------------------------------------------
"""

' a study.__init__.py module '

__author__ = 'steven'


class BaseValueError(ValueError):
    pass


def test(*args, **kwargs):
    print(args, len(args), kwargs, len(kwargs))
    if len(args) >= 10:
        raise BaseValueError('args length must less than 10.%s' % str(args))


try:
    test(range(10))
    test(*range(10))
except ValueError as e:
    print('ValueError!', e.args)
    raise
# except BaseValueError as e:
#     print('BaseValueError!', e.args)
#     raise
