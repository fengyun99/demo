#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/11/7 21:51
# @Author   : FengYun
# @File     : static.py
# @Software : PyCharm
from flask import Blueprint, send_from_directory
from application import app

route_static = Blueprint('static', __name__)


@route_static.route('/<path:filename>')
def get_static(filename):
    app.logger.info(filename)
    return send_from_directory(app.root_path + '/web/static/', filename)
