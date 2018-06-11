#! /usr/bin/python3
# -*- coding:utf-8 -*-
from  sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('mysql://root:root@demo@localhost:3306/demo?charset=utf8', encoding="utf8", echo=False)
BaseDB = declarative_base()

ERROR_CODE = {
    "0": "ok",
    "1001": "入参非法",
    "1002": "用户已存在"
}