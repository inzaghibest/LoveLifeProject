__author__ = 'zhxp'
import tornado.web
from controller.base import BaseHandler
from tornado import gen

class ProAnalyHandler(BaseHandler):
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self, *args, **kwargs):
        print("ProAnalyHandler get")
        cursor = self.db.occupation_info.find()
        colls = []
        i = 0
        while (yield cursor.fetch_next):
            coll = cursor.next_object()
            colls.append({})
            for k,v in coll.items():
                colls[i][k]=v
                print(colls)
            i+=1
        self.render("proanaly.html", colls =colls)

class ShowHandler(BaseHandler):
    def get(self, *args, **kwargs):
        print(args)
        occupation = args[0]
        self.render("show.html",occupation = occupation)