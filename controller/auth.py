__author__ = 'zhangxp'
import tornado.web
from controller.base import BaseHandler
from tornado import gen
import datetime

# 登录页面
class LoginHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("login.html", Message = "欢迎您登录", username=self.get_current_user())

    @tornado.web.asynchronous
    @gen.coroutine
    def post(self, *args, **kwargs):
        username = self.get_body_argument('fname')
        password = self.get_body_argument('fpassword')
        user_coll = yield self.db.userinfo.find_one({"username":username})
        if user_coll==None:
            msg = "没有找到此用户"
            print(msg)
        elif password != user_coll["password"]:
            msg = "你输入的密码有误"
            print(msg)
        else:
            # 用户登陆成功后保存登陆名到session
            msg = "登录成功!"
            # 登录成功后,更新用户的登录时间
            login_time = self.get_current_time()
            yield self.db.userinfo.update({"username":username},{"$set":{"last_login":login_time}})
            self.session["username"] = username
            self.session.save()
        if(msg == "登录成功!"):
            print("登陆成功!")
            return self.redirect("/?username=%s" %self.get_current_user())
        else:
            print(msg)
            self.render("login.html", Message = msg,username = self.get_current_user())

# 注册页面
class RegisterHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("register.html", Message = "欢迎您注册")

    @tornado.web.asynchronous
    @gen.coroutine
    def post(self, *args, **kwargs):
        username = self.get_body_argument('fname')
        password = self.get_body_argument('fpassword')
        gender = self.get_body_argument('gender')
        print(gender)
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
            print(otherStyleTime)
            user_info = {"username":username, "password":password, "power":1,
                         "glod_count":10, "last_login":otherStyleTime, "register_date":otherStyleTime,
                         "gender":gender}
            print(user_info)
            result = yield self.db.userinfo.insert(user_info)
            # 保存用户session
            self.session["username"] = username
            self.session.save()
            # return self.redirect("/?username=%s"%username)
            # next参数指向来到登陆页面之前的页面,为了用户体验,登陆成功之后返回上一个页面的方式
            self.redirect(self.get_argument('next', '/?username%s'%username))

# 退出登录,页面只是负责清除用户的session数据
class ExitLoginHandler(BaseHandler):
    def get(self, *args, **kwargs):
        print("Exit Get")
        self.session["username"] = None
        self.session.save()
        return self.redirect("/?username=%s"%self.get_current_user())










