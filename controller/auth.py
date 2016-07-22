__author__ = 'zhangxp'
import tornado.web
from controller.base import BaseHandler
from tornado import gen

class LoginHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("login.html", Message = "欢迎您登录")
    @tornado.web.asynchronous
    @gen.coroutine
    def post(self, *args, **kwargs):
        print("login post")
        username = self.get_body_argument('fname')
        password = self.get_body_argument('fpassword')
        user = yield self.db.member.find_one({"username":username})
        if user==None:
            msg = "没有找到此用户"
        return self.redirect("/login")




