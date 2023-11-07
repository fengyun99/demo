#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/11/6 22:57
# @Author   : FengYun
# @File     : www.py
# @Software : PyCharm
from application import app
from web.controllers.index import index_bp
from web.controllers.user.User import route_user
from web.controllers.static import route_static
from web.controllers.account.Account import route_account

app.register_blueprint(index_bp, url_prefix='/')
app.register_blueprint(route_user, url_prefix='/user')
app.register_blueprint(route_static, url_prefix='/static')
app.register_blueprint(route_account, url_prefix='/account')