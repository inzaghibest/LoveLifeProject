__author__ = 'zhangxp'
import tornado.web
import sys
import controller.session

# 基础类,所有Request相应的类都应该从此继承,保证可以使用session,以及self.current_user可用
class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, *argc, **argkw):
        super(BaseHandler, self).__init__(*argc, **argkw)
        self.session = controller.session.Session(self.application.session_manager, self)
    def get_current_user(self):
        return self.session.get("user_name")



