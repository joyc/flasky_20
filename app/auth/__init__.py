#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : __init__.py.py
# @Author : Hython
# @Date   : 公元 2020/01/17 0:22
from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views
