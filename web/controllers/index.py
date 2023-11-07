#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/11/6 23:15
# @Author   : FengYun
# @File     : index.py
# @Software : PyCharm
from flask import Blueprint, render_template

index_bp = Blueprint('index', __name__)


@index_bp.route('/')
def index():
    return render_template('index/index.html')
