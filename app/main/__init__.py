#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : __init__.py.py
# @Author : Hython
# @Date   : 公元 2020/01/14 23:35
from flask import Blueprint

main = Blueprint('main', __name__)
# 把路由和错误处理程序与蓝本关联
from . import views, errors
