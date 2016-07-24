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
        print("LoginHandler")
        username = self.get_body_argument('fname')
        password = self.get_body_argument('fpassword')
        user_coll = yield self.db.userinfo.find_one({"username":username})
        print(user_coll)
        if user_coll==None:
            msg = "没有找到此用户"
        elif password != user_coll["password"]:
            msg = "你输入的密码有误"
        else:
            msg = "登录成功!"
            self.session["username"] = username
            self.session.save()
        if(msg == "登录成功!"):
            self.render("main.html", username = self.get_current_user())
        else:
            self.render("login.html", Message = msg)

class RegisterHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("register.html", Message = "欢迎您注册")
    @tornado.web.asynchronous
    @gen.coroutine
    def post(self, *args, **kwargs):
        print("register post")
        username = self.get_body_argument('fname')
        password = self.get_body_argument('fpassword')
        print(username)
        print(password)
        user_coll = yield self.db.userinfo.find_one({"username":username})
        print(user_coll)
        if user_coll is not None:
            print("already have")
        else:
            user_info = {"username":username, "password":password}
            print(user_info)
            result = yield self.db.userinfo.insert(user_info)
            print(result)
            self.render("main.html",username = username)








