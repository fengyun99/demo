#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/11/3 22:52
# @Author   : FengYun
# @File     : UrlManager.py
# @Software : PyCharm
class UrlManager(object):
    @staticmethod
    def buildUrl(url):
        return url

    @staticmethod
    def buildStaticUrl(url):
        # 静态重定向资源位置
        url = '/static' + url + '?version=' + "1.0"
        return UrlManager.buildUrl(url)