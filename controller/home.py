__author__ = 'zhangxp'
import tornado.web
from controller.base import BaseHandler

class HomeHandler(BaseHandler):
    def get(self, *args, **kwargs):
        print("HomeHandler")
        #此处从后台数据库获取
        current_user = self.get_current_user()
        print(current_user)
        # 为访问者提供一个guest帐户
        if current_user == None:
            self.session["username"] = "guest"
            current_user = "guest"
            self.session.save()
        self.render('main.html', username = current_user)


