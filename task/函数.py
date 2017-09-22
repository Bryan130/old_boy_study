#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# zzz.py
# @Author : Bryan.Lan (18645555731@163.com)
# @Link   : https://github.com/Bryan130
# @Date   : 2017/9/4 下午2:38:07


# def outer():
#     count = 10
#
#     def inter():
#         print(count)
#         # count = 5
#         # print(count)
#     inter()
#     print(count)
#
# outer()

def outer(count):
    def inter():
        print(count)
    return inter

a = outer(2)
a()

