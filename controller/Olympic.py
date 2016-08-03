__author__ = 'zhangxp'
import tornado.web
from controller.base import BaseHandler
from tornado import gen

class OlympicMainHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("OlympicMain.html")
