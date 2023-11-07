#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/11/7 21:01
# @Author   : FengYun
# @File     : Account.py.py
# @Software : PyCharm
from flask import Blueprint,render_template

route_user = Blueprint('user', __name__)


@route_user.route('/login')
def login():
    return render_template('user/login.html')
