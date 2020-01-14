#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : forms.py
# @Author : Hython
# @Date   : 公元 2020/01/14 23:36
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')