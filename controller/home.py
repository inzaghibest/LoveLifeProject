__author__ = 'zhangxp'
import tornado.web
from controller.base import BaseHandler
from tornado import gen
import datetime


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
    def post(self, *args, **kwargs):
        print(args)

class NewsShowHandler(BaseHandler):
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self, *args, **kwargs):
        cursor = self.db.news_collection.find()
        colls = []
        i = 0
        while (yield cursor.fetch_next):
                coll = cursor.next_object()
                colls.append({})
                for k,v in coll.items():
                    colls[i][k]=v
                print(colls)
                i+=1
        self.render("newsshow.html", colls = colls)

class NewDetailShowHandler(BaseHandler):
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self, *args, **kwargs):
        newstitle = args[0]
        print(newstitle)
        doc_coll = yield self.db.news_detail.find_one({"newstitle":newstitle})
        self.render("newsdetailshow.html",coll = doc_coll)



