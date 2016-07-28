__author__ = 'zhangxp'
import tornado.web
import sys
import controller.session
import datetime

# 基础类,所有Request相应的类都应该从此继承,保证可以使用session,以及self.current_user可用
class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, *argc, **argkw):
        super(BaseHandler, self).__init__(*argc, **argkw)
        self.session = controller.session.Session(self.application.session_manager, self)
        self.db = self.application.db

    def get_current_user(self):
        return self.session.get("username")

    def get_current_time(self):
        now = datetime.datetime.now()
        otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
        return otherStyleTime

    # 任何未捕捉的错误都会被它的 write_error() 方法捕捉,所以错误处理覆盖此方法即可
    def write_error(self, status_code, **kwargs):
        print("write_erro")
        if status_code == 404:
            print("404")
            self.render('404.html')
        elif status_code == 500:
            self.render('500.html')
        else:
            super(tornado.web.RequestHandler, self).write_error(status_code, **kwargs)









