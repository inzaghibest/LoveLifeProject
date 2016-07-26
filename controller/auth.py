__author__ = 'zhangxp'
import tornado.web
from controller.base import BaseHandler
from tornado import gen
import datetime

# 登录页面
class LoginHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("login.html", Message = "欢迎您登录")

    @tornado.web.asynchronous
    @gen.coroutine
    def post(self, *args, **kwargs):
        username = self.get_body_argument('fname')
        password = self.get_body_argument('fpassword')
        user_coll = yield self.db.userinfo.find_one({"userinfo":username})
        print(user_coll)
        if user_coll==None:
            msg = "没有找到此用户"
        elif password != user_coll["password"]:
            msg = "你输入的密码有误"
        else:
            msg = "登录成功!"
            self.session["userinfo"] = username
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
        username = self.get_body_argument('fname')
        password = self.get_body_argument('fpassword')
        user_coll = yield self.db.userinfo.find_one({"username":username})
        msg = ""
        # 判断用户是否已经注册,如果已经注册,提示
        if user_coll is not None:
            msg = "该用户已被注册,请换一个用户名"
            print("register already have")
            self.render("register.html", Message=msg)
        else:
            now = datetime.datetime.now()
            otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
            user_info = {"username":username, "password":password, "power":1,
                         "glod_count":10, "last_login":otherStyleTime}
            print(user_info)
            result = yield self.db.userinfo.insert(user_info)
            self.render("main.html",username = username)








