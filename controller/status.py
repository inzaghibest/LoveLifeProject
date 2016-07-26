__author__ = 'zhangxp'
import tornado.web
from controller.base import BaseHandler
from tornado import gen
import datetime
from tornado import gen

#向js发送get数据,用于页面动态刷新的场景
class StatusHandler(BaseHandler):
    @tornado.web.asynchronous
    @gen.coroutine
    def post(self, *args):
        print("status get")
        action = self.get_argument("action")
        username = self.get_argument("name")
        print(action)
        print(username)
        if(action == "isused"):
            self.get(username)

    @tornado.web.asynchronous
    @gen.coroutine
    def get(self, *args, **kwargs):
        print(args)
        username = args
        doc_coll = yield self.db.userinfo.find_one({"username":username})
        print(doc_coll)
        msg = ""
        if(doc_coll == None):
            print("None")
            msg = ""
            self.write({"msg":msg})
        else:
            print("have")
            msg = "该用户已经注册了,请换个名字吧"
            self.write({"msg":msg})




