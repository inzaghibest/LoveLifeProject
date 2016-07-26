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
        print(action)
        if(action == "isused"):
            self.get()

    def get(self, *args, **kwargs):
        print("get")
        self.write({"msg":"该用户已经注册了"})

