# -*- coding: utf-8 -*-
'''
Created on 2012-7-3

@author: lihao
'''
import top.api
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.gen

from handlers.adduser import AddUserHandler

from tornado.options import define, options
define("port", default=27000, help="run on the given port", type=int)

#replace with your own appkey
top.setDefaultAppInfo("32212088", "614257de571f01f143c375c8ebc332r4")


class Application(tornado.web.Application):
    def __init__(self):
        handlers=[(r"/taobao/test", AddUserHandler)
                 ]
        tornado.web.Application.__init__(self, handlers, debug=True)


#a.fields="nick"
if __name__ == "__main__":
    tornado.options.parse_command_line()

    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)

    main_loop = tornado.ioloop.IOLoop.instance()
    main_loop.start()
    
