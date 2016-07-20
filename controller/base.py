__author__ = 'zhangxp'
import tornado.web
import sys
import controller.session

# ������,����Request��Ӧ���඼Ӧ�ôӴ˼̳�,��֤����ʹ��session,�Լ�self.current_user����
class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, *argc, **argkw):
        super(BaseHandler, self).__init__(*argc, **argkw)
        self.session = controller.session.Session(self.application.session_manager, self)
    def get_current_user(self):
        return self.session.get("user_name")



