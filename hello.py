#! /usr/bin/python3
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web

class MainHandle(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello')

application = tornado.web.Application([
    (r"/", MainHandle)
])

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
