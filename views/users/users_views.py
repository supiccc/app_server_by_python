# /usr/bin/python3
# -*- coding:utf-8 -*-

import tornado.web
from tornado.escape import json_decode
import logging
from logging.handlers import TimedRotatingFileHandler

from common.commons import (
    http_response,
)

# 导入错误码
from conf.base import (
    ERROR_CODE
)

### Configure logging ###
logFilePath = "log/users/users.log"
logger = logging.getLogger("Users")
logger.setLevel(logging.DEBUG)
handler = TimedRotatingFileHandler(logFilePath, when='D', interval=1, backupCount=30)
formatter = logging.Formatter('%(asctime)s \
 %(filename)s [line: %(lined)d] %(levelname)s %(messages)s',)

handler.suffix = "%Y%m%d" # 文件后缀名
handler.setFormatter(formatter)
logger.addHandler(handler)



class RegistHandle(tornado.web.RequestHandler):
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
        logger.debug("RegistHandle: regist successfully")    
        http_response(self, ERROR_CODE['0'], 0)
