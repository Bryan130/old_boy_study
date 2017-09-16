#!/usr/bin/env python  
# -*- coding:utf-8 -*-

""" 
@version: v1.0 
@author: Bryan
@license: Apache Licence  
@contact: 244896035@qq.com 
@site: http://http://blog.csdn.net/weixin_36650524 
@software: PyCharm 
@file: 斐波那契数列.py 
@time: 2017/9/13 16:03 
"""


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b, end=" ")
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(6)   # 1 1 2 3 5 8

