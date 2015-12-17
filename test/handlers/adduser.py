import tornado.web
import tornado.gen
import json
import logging

import top.api

class AddUserHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        #get request parameter
        data     = json.loads(self.request.body.decode("utf-8"))
        userid   = data.get("id", "")

        if not userid:
            logging.error("invalid parameter")
            self.set_status(403)
            self.finish()
            return

        a = top.api.OpenimUsersAddRequest()
        tp_userid = userid
        tp_pass   = 'testpwd'
        a.userinfos = {"userid": tp_userid, "password": tp_pass}

        try:
            result = yield a.getResponse()

        except Exception as e:
            logging.error("create tp user failed")

        self.finish()
