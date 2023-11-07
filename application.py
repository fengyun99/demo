#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/11/6 22:56
# @Author   : FengYun
# @File     : application.py
# @Software : PyCharm
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager

from common.libs.UrlManager import UrlManager


class Application(Flask):
    def __init__(self, import_name, template_folder=None, root_path=None):
        super(Application, self).__init__(import_name, template_folder=template_folder, root_path=root_path, static_folder=None)
        self.config.from_pyfile('config/base_setting.py')

        db.init_app(self)


db = SQLAlchemy()
app = Application(__name__, template_folder=os.getcwd() + '/web/templates', root_path=os.getcwd())
manager = Manager(app)

'''
函数模板,避免重定向错误
'''
app.add_template_global(UrlManager.buildStaticUrl, 'buildStaticUrl')
app.add_template_global(UrlManager.buildUrl, 'buildUrl')
