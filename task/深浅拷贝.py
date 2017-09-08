#!/usr/bin/env python  
# -*- coding:utf-8 -*-

""" 
@version: v1.0 
@author: Bryan
@license: Apache Licence  
@contact: 244896035@qq.com 
@site: http://http://blog.csdn.net/weixin_36650524 
@software: PyCharm 
@file: 深浅拷贝.py 
@time: 2017/9/8 17:49 
"""

dic = {
    "a": "asd",
    "b": {
        "asd": 1,
        "aa": "asd"
    }
}

dic1 = dic.copy()

dic1["a"] = "aaa"
dic1["b"]["aa"] = "dsa"
print(dic)
print(dic1)


a = [1, 2]
print(id(a))
b = a
print(id(b))
