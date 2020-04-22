#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : decorators.py
# @Author : Hython
# @Date   : 公元 2020/04/22 22:58
from functools import wraps
from flask import abort
from flask_login import current_user
from .models import Permission


def permission_required(permission):
    def decorator(f):
        @wraps
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def admin_required(f):
    return permission_required(Permission.ADMIN)(f)
