#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 购物车.py
# @Author : Bryan.Lan (18645555731@163.com)
# @Link   : https://github.com/Bryan130
# @Date   : 2017/9/2 上午12:37:02

# buy_thing = []
# things_name = ["", "iphone", "car", "book"]
# things_value = ["", "599", "1000", "6"]
# salary = int(input("请输入您的金额："))

# while True:
#     print("""
# ----------------------------------
# 购物清单如下：
# 1. iphone      $599
# 2. car           $1000
# 3. book        $5
# ----------------------------------
#     """)
#     thing_index = input("请输入您需要购买的商品的序号(退出请按quit)：")

#     if thing_index == "quit":
        
#         break
#     else:
        

#     if thing_index == '1':
#         if salary > 599:
#             salary -= 599
#         else:
#             print("您的余额不足，请充值！")
#             continue
#         print("您已购买 iphone, 当前余额为：%s", salary)
#         buy_thing.append("iphone")
#     elif thing_index == '2':
#         if salary > 1000:
#             salary -= 1000
#         else:
#             print("您的余额不足，请充值！")
#             continue
#         print("您已购买 iphone, 当前余额为：%s", salary)
#         buy_thing.append("car")
#     elif thing_index == '3':
#         if salary > 5:
#             salary -= 5
#         else:
#             print("您的余额不足，请充值！")
#             continue
#         print("您已购买 iphone, 当前余额为：%s", salary)
#         buy_thing.append("book")
#     elif thing_index == "quit":
#         print("您已购买了如下商品:")
#         print("您的余额为: %d", salary)
#         break

product_list = [
    ('book', 100),
    ('Mac Pro', 900),
    ('watch', 500),
    ('coffee', 30),
    ('Python', 106),
]

saving = input('input your saving: ')
shopping_car = []

if saving.isdigit():
    saving = int(saving)
    while True:
        for i, v in enumerate(product_list):
            print(i, v)
        user_choice = input('选择购买商品编号[退出：quit]：')

        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                product_item = product_list[user_choice]
                if product_item[1] < saving:
                    saving -= product_item[1]
                    shopping_car.append(product_item)
                    print('您当前的余额为{}'.format(saving))
                else:
                    print("余额不足！")
            else:
                print("编号错误")
        elif user_choice == "quit":
            print("您已购买如下商品".center(30, "-"))
            for i in shopping_car:
                print(i)
            print("您的余额为{}".format(saving))
            break
        else:
            print('invalid chioce')
