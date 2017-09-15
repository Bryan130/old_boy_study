#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version: v1.0
@author: Bryan
@license: Apache Licence
@contact: 244896035@qq.com
@site: http://http://blog.csdn.net/weixin_36650524
@software: PyCharm
@file: login.py
@time: 2017/9/15 11:17
"""
pages = ["home", "finance", "book"]
login_status = "False"

# usr = "bryan"
# pwd = "123"
WX_pwd = "1234"

def login_type(auth_type):
    def login_state(func):
        def login():
            global login_status
            if login_status == "False":
                if auth_type == "JD":
                    username = input("Please input your username:")
                    password = input("Please input your password:")
                    with open("JD.txt", "r") as jd:
                        for dataline in jd:
                            print(dataline)
                            (usr, pwd) = dataline.split(",", 1)
                            if username == usr and password == pwd.rstrip():
                                print("login success!")
                                login_status = "True"
                                func()
                                break
                            else:
                                print("username or password is wrong")
                elif auth_type == "WX":
                    password = input("Please input your WX password:")
                    if password == WX_pwd:
                        print("login success!")
                        login_status = "True"
                        func()
            else:
                pass
                func()
        return login
    return login_state


@login_type("JD")
def home():
    print("This is Home Page!")


@login_type("WX")
def finance():
    print("This is Finance Page!")


def book():
    print("This is Book Page!")


class Main():
    def __init__(self):
        pass


def page_view():
    print("---------------------------------")
    for i, v in enumerate(pages):
        print(i, v)
    print("退出：q")


def main():
    while True:
        page_view()
        page_num = input("Please input:")
        if page_num.isdigit():
            if page_num == "0":
                home()
            elif page_num == "1":
                finance()
            elif page_num == "2":
                book()
            else:
                print("Invalid input!")
        elif page_num == "q":
            break
        else:
            print("Invalid input!")


if __name__ == "__main__":
    main()
