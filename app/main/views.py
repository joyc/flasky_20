#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : views.py
# @Author : Hython
# @Date   : 公元 2020/01/14 23:36
from datetime import datetime
from flask import render_template, session, redirect, url_for, current_app
from .. import db
from ..models import User
from ..email import send_email
from . import main
from .forms import NameForm
from flask_login import login_required


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@main.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'


@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)
