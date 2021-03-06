#! /usr/bin/python3
# -*- coding:utf-8 -*-

from __future__ import unicode_literals # 引入新版本特性
from importlib import import_module

def include(module):
    # 导入模块
    res = import_module(module)
    urls = getattr(res, 'urls', res)
    return urls

def url_wrapper(urls):
    # 拼接请求 url
    wrapper_list = []
    for url in urls:
        path, handles = url
        if isinstance(handles, (tuple, list)):
            for handle in handles:
                pattern, handle_class = handle
                wrap = ("{0}{1}".format(path, pattern), handle_class)
                wrapper_list.append(wrap)
        else:
            wrapper_list.append(((path, handles)))
    return wrapper_list

