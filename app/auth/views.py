#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : views.py
# @Author : Hython
# @Date   : 公元 2020/01/17 0:23
from flask import render_template
from . import auth


@auth.route('/login')
def login():
    return render_template('auth/login.html')
