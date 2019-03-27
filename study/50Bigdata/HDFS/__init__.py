#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Project Name：  study
   File Name：       __init__.py
   Description :
   Author :              Steven Cheng
   date：                  2019/3/26
   time：                  15:26
-------------------------------------------------
   Change Activity:
                   2019/3/26:
-------------------------------------------------
"""

' a study.__init__.py module '

__author__ = 'steven'

import os
import time

from hdfs.client import Client

client = Client("http://127.0.0.1:50070", root="/", timeout=100)

print(client.makedirs("/test/"))
print(client.status("/test/"))
print(client.list("/test/"))
print(client.delete("/test/", True))
upload_filename = client.upload("/test/" + str(int(round(time.time() * 1000))) + ".pdf", "test.pdf")
print(upload_filename)
download_path = os.path.join(os.path.abspath('.'), 'download/hdfs/')
if not os.path.exists(download_path):
    os.makedirs(download_path, True)
else:
    print(download_path, ' is existed.')
print(client.download(upload_filename, download_path + str(int(round(time.time() * 1000))) + ".pdf"))
print(client.delete(upload_filename))
print(client.delete(upload_filename))
