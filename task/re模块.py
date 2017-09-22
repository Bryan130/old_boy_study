#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version: v1.0
@author: Bryan
@license: Apache Licence
@contact: 244896035@qq.com
@site: http://http://blog.csdn.net/weixin_36650524
@software: PyCharm
@file: re模块.py
@time: 2017/9/21 10:31
"""

# 元字符
# . 通配符       通配一个字符（除 换行符）
# ^  尖角号      从开始匹配   尖角号 ^ 在方括号 [] 里，表示 取反
# $  刀了符      从最后开始匹配
# *  星号        前面的字符重复 0,正无穷次, 贪婪匹配， 后面加个 ？ ，变为 非贪婪匹配
# ？  问号       前面的字符重复 0,1次
# +  加号        前面的字符重复 1,正无穷次
# {n} 花括号     前面的字符重复 n次
# {n,m} 花括号   前面的字符重复 n或m次
# []  方括号
# ()  小括号     分组
# \  反斜杠      转义（跟特殊字符去除特殊功能，跟某些普通字符实现特殊功能）
# \d    匹配任何十进制数，它相当于类 [0-9]
# \D    匹配任何非数字字符，它相当于类 [^0-9]
# \s    匹配任何空白字符，它相当于类 [\t\n\r\f\v]
# \S    匹配任何非空白字符，它相当于类 [^\t\n\r\f\v]
# \w    匹配任何字母数字字符，它相当于类 [a-zA-Z0-9_]
# \W    匹配任何非字母数字字符，它相当于类 [^a-zA-Z0-9_]
# \b    匹配一个特殊字符边界，一般指单词和空格间的位置


import re

# # findall  全匹配，贪婪匹配，返回一个列表
# ret = re.findall("a.", "hfakdhk")
# print(ret)      # ['ak']
# ret = re.findall("a.", "hfakdaehk")
# print(ret)      # ['ak', 'ae']
#
# ret = re.search("a.", "asdaoiejf")
# print(ret)          # <_sre.SRE_Match object; span=(0, 2), match='as'>
# print(ret.group())  # as   search 非贪婪匹配，只匹配第一个
#
# # split   分割字符串, 返回列表
# ret = re.split("a", "khfksdhajdsdhf")
# print(ret)          # ['khfksdh', 'jdsdhf']
#
# # sub  替换
# ret = re.sub("a..x", "s...b", "kfhgalexfirhjfi")
# print(ret)          # kfhgs...bfirhjfi



# s = "1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))"
#
# ret = re.search("\([^\(\)]+\)", s)
# print(ret.group())


# 校验是否又不合法的字符
# ret = re.search("[a-zA-Z]", s)
# print(ret)
# 格式化字符串
# s = re.sub(" ", "", s)
# print(s)

# s = re.search("\([^()]+\)", s).group()
# print(s)
# s = "60-3 0-(4.0/5)"
# def peel(s):
#     s1 = re.search("\([^()]+\)", s)
#     if s1:
#         s1 = s1.group()
#         return s1
#     return s
#
# ws = peel(s)
# print(ws)

# sources = "1- 2*( (6 0-30+(-40/5)*(9-2*5/3 +7/3*99/4*2 998+10 *568/ 14) )-(-4*3)/ (16- 3* 2))"
#
#
# a = '\(-40/5\)'
# b = '-8.0'
# ret = re.sub(a, b, sources)
# print(ret)

