# /usr/bin/python3
# -*- coding:utf-8 -*-

import tornado.web
from tornado.escape import json_decode
import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime

from common.commons import (
    http_response,
)

# 导入错误码
from conf.base import (
    ERROR_CODE
)

from models import (
    Users
)

### Configure logging ###
logFilePath = "log/users/users.log"
logger = logging.getLogger("Users")
logger.setLevel(logging.DEBUG)
# 日志整理
handler = TimedRotatingFileHandler(logFilePath, when='D', interval=1, backupCount=30)
formatter = logging.Formatter('%(asctime)s \
 %(filename)s [line: %(lined)d] %(levelname)s %(messages)s',)

handler.suffix = "%Y%m%d" # 日志后缀
handler.setFormatter(formatter)
logger.addHandler(handler)



class RegistHandle(tornado.web.RequestHandler):

    @property
    def db(self):
        return self.application.db

    def post(self):
        try:
            args = json_decode(self.request.body)
            phone = args['phone']
            password = args['password']
            verify_code = args['code']
        except:
            logger.info("RegistHandle: request argument incorrect")
            http_response(self, ERROR_CODE['1001'], 1001)
            return
        
        ex_user =  self.db.query(Users).filter_by(phone = phone).first()
        if ex_user:
            http_response(self, ERROR_CODE['1002'], 1002)
            self.db.close()
            return
        else:
            logger.debug("RegistHandle: insert db, user: %s"%phone)
            create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            new_user = Users(phone, password, create_time)
            self.db.add(new_user)
            self.db.commit()
            self.db.close()


            logger.debug("RegistHandle: regist successful")
            http_response(self, ERROR_CODE['0'], 0)
