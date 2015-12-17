# openim
The tornado version for aliyun openim sdk

code examples:

a = top.api.OpenimUsersAddRequest()
tp_userid = 'harry'
tp_pass   = 'testpwd'
a.userinfos = {"userid": tp_userid, "password": tp_pass}

try:
    result = yield a.getResponse()
except Exception as e:
    logging.error("create tp user failed")


more details refer to test
