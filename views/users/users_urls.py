#! /usr/bin/python3
# -*- coding:utf-8 -*-

from __future__ import unicode_literals
from .users_views import (
    RegistHandle
)

urls = [
    (r'regist', RegistHandle)
]