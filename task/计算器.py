#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version: v1.0
@author: Bryan
@license: Apache Licence
@contact: 244896035@qq.com
@site: http://http://blog.csdn.net/weixin_36650524
@software: PyCharm
@file: 计算器.py
@time: 2017/9/22 9:30
"""

import re


def check(s):
    flag = True
    if re.search("[a-zA-Z]", s):
        flag = False
        return flag
    return flag


def formatter(s):
    s = re.sub(" ", "", s)
    return s


def peel(s):
    s1 = re.search("\([^()]+\)", s)
    if s1:
        s1 = s1.group()
        return s1
    return s


def user_input():
    sources = input("请输入：")
    return sources


def mul_div(s):
    if re.search("\*", s):
        x, y = re.search("\*", s).group()
        z = float(x) * float(y)
    else:
        print(s)
        s = s.replace("(", "")
        print(s)
        s = s.replace(")", "")
        print(s)
        x, y = re.split("/", s)
        z = float(x) / float(y)
        print("z", z)
    return z


def main(sources):
    # sources = user_input()
    if check(sources):
        print(sources)
        sources = formatter(sources)
        while True:
            print("sources", sources)
            sources1 = peel(sources)
            print("sources1", sources1)
            if re.search("[*/]", sources1):
                sources2 = mul_div(sources1)
                print("sources2", sources2)
                sources = re.sub(sources1, str(sources2), sources)
                print(sources)
            elif re.search("[\-+]", sources):
                pass
    else:
        print("不允许输入非法字符")


if __name__ == "__main__":
    sources = "1- 2*( (6 0-30+(-40/5)*(9-2*5/3 +7/3*99/4*2 998+10 *568/ 14) )-(-4*3)/ (16- 3* 2))"
    main(sources)
