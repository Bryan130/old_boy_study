#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version: v1.0
@author: Bryan
@license: Apache Licence
@contact: 244896035@qq.com
@site: http://http://blog.csdn.net/weixin_36650524
@software: PyCharm
@file: logging模块.py
@time: 2017/9/19 19:14
"""


import logging

logger = logging.getLogger("bryan")

# 创建一个Handler，用于写入日志文件，test.log是日志写入的文件
fh = logging.FileHandler("test.log")

# 再创建一个Handler，用于输出到控制台
ch = logging.StreamHandler()

# 定义输出log的格式
formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')

fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)

# 可以分别设置输出到文件的级别，和输出到控制台的级别
fh.setLevel(logging.ERROR)
"""输出到文件里的内容
2017-09-19 20:11:45,830 ERROR   : logger error message
2017-09-19 20:11:45,830 CRITICAL: logger critical message
"""
logger.setLevel(logging.DEBUG)
"""输出到屏幕的内容
2017-09-19 20:11:45,830 DEBUG   : logger debug message
2017-09-19 20:11:45,830 INFO    : logger info message
2017-09-19 20:11:45,830 WARNING : logger warning message
2017-09-19 20:11:45,830 ERROR   : logger error message
2017-09-19 20:11:45,830 CRITICAL: logger critical message
"""

logger.debug('logger debug message')
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')

