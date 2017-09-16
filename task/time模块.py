#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version: v1.0
@author: Bryan
@license: Apache Licence
@contact: 244896035@qq.com
@site: http://http://blog.csdn.net/weixin_36650524
@software: PyCharm
@file: time模块.py
@time: 2017/9/16 16:31
"""

import time

# 时间戳时间      <====>       结构化时间
print(time.time())   # 时间戳  1505551067.3217442



# 结构化时间       <====>       格式化时间
print(time.localtime())  # 结构化 time.struct_time(tm_year=2017, tm_mon=9, tm_mday=16, tm_hour=16, tm_min=49, tm_sec=27, tm_wday=5, tm_yday=259, tm_isdst=0)
b = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())   # 结构化时间   -->  格式化时间  2017-09-16 16:56:49
print(b)


# 格式化时间       <====>       时间戳时间

print(time.ctime(time.time()))  # 时间戳时间    -->   格式化时间    Sat Sep 16 17:00:37 2017
