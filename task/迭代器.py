#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version: v1.0
@author: Bryan
@license: Apache Licence
@contact: 244896035@qq.com
@site: http://http://blog.csdn.net/weixin_36650524
@software: PyCharm
@file: 迭代器.py
@time: 2017/9/16 13:05
"""


# 生产器都是迭代器，迭代器不一定是生产器
# list, tuple, dict, string  --->  Iterable(可迭代对象)
# 什么是迭代器：
# 满足两个条件：1. 有iter方法。   2. 有next方法
l = [1, 2, 3, 4]
m = iter(l)
print(m)          # <list_iterator object at 0x0350B450>

n = next(m)
print(n)          # 1
n = next(m)
print(n)          # 2
n = next(m)
print(n)          # 3

# for 循环内部做的三件事：
# 1. 调用可迭代对象的iter方法返回一个迭代器对象
# 2. 不断调用迭代器对象的next方法
# 3. 处理 StopIteration


# isinstance(o, t)    判断一个对象 o 是否是一个 t 对象
# 判断[1, 2, 3] 是不是 list，是就返回 True，
# eq:   isinstance([1, 2, 3], list)   ---->   True
# eq:   isinstance([1, 2, 3], dict)   ---->   False

max(len(x.strip()) for x in open('/hello/abc', 'r'))
