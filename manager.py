#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/11/6 22:57
# @Author   : FengYun
# @File     : manager.py
# @Software : PyCharm
from flask_script import Server

from application import manager
import www

manager.add_command("runserver", Server(host='0.0.0.0', port=5000,use_debugger=True, use_reloader=True))


def main():
    manager.run()


if __name__ == '__main__':
    try:
        import sys

        sys.exit(main())
    except Exception as e:
        import traceback

        traceback.print_exc()


