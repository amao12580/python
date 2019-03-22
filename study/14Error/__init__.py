#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging

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

# logging.basicConfig(filename='logs/%(levelname)s.log',level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(message)s',datefmt='%Y-%m-%d %X')

# 2019-03-19 20:04:25.682  INFO [zhengtyun-system,95c06ff569dfdfd3,95c06ff569dfdfd3,true] 12056 --- [nio-8014-exec-6] com.zhengt.system.controller.TestController                            [stdIn] [139] : signature:com.zhengt.system.controller.TestController.login

logging.basicConfig(
    # filename='logs/%(levelname)s.log'
    filename='test.log'
    , level=logging.DEBUG,
    format='%(asctime)s %(levelname)s [%(filename)s] %(process)d [%(threadName)s] %(pathname)s [%('
           'funcName)s]  [%(lineno)d] : %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')

logging.info('this is the info message')
logging.debug('this is the debug message')
logging.warning('this is the warning message')
logging.error('this is the error message')
logging.critical('this is the critical message')


class BaseValueError(ValueError):
    pass


def test(*args, **kwargs):
    logging.info(args)
    if len(args) >= 10:
        raise BaseValueError('args length must less than 10.%s' % str(args))


try:
    test(range(10))
    test(*range(10))
except ValueError as e:
    # print('ValueError!', e.args)
    logging.exception(e)
    raise
# except BaseValueError as e:
#     print('BaseValueError!', e.args)
#     raise
