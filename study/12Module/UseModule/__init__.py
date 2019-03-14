#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Project Name：  study
   File Name：       __init__.py
   Description :
   Author :              steven
   date：                  2019/3/14
   time：                  14:50
-------------------------------------------------
   Change Activity:
                   2019/3/14:
-------------------------------------------------
"""

' a study.__init__.py module '

__author__ = 'steven'

import sys


def test(*args, **kwargs):
    print(sys.api_version)
    print(sys.argv)
    print(sys.callstats())
    print(sys.getfilesystemencoding())
    print(sys.exc_info())


if __name__ == '__main__':
    test()
