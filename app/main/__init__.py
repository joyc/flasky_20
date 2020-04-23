#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : __init__.py.py
# @Author : Hython
# @Date   : 公元 2020/01/14 23:35
from flask import Blueprint

main = Blueprint('main', __name__)
# 把路由和错误处理程序与蓝本关联
from . import views, errors


# Permission类加入模板上下文
from ..models import Permission
@main.app_context_processor
def inject_permission():
    return dict(Permission=Permission)
