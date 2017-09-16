#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version: v1.0
@author: Bryan
@license: Apache Licence
@contact: 244896035@qq.com
@site: http://http://blog.csdn.net/weixin_36650524
@software: PyCharm
@file: yeild伪并发.py
@time: 2017/9/16 12:54
"""


import time


def consumer(name):
    print("%s 准备吃包子啦!" % name)
    while True:
        baozi = yield
        print("包子[%s]来了,被[%s]吃了!" % (baozi, name))


def producer():
    c = consumer('A')
    c2 = consumer('B')
    next(c)     # c.__next__()
    next(c2)    # c2.__next__()
    print("老子开始准备做包子啦!")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子!")
        c.send(i)
        c2.send(i)


producer()
