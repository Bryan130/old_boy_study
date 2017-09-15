#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version: v1.0
@author: Bryan
@license: Apache Licence
@contact: 244896035@qq.com
@site: http://http://blog.csdn.net/weixin_36650524
@software: PyCharm
@file: 列表生成器.py
@time: 2017/9/15 17:22
"""


def func():
    pass


class Main():
    def __init__(self):
        pass


def main():
    a = [lambda x:x*3 for x in range(10)]
    print(a)


if __name__ == "__main__":
    main()
