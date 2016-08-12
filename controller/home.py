__author__ = 'zhangxp'
import tornado.web
from controller.base import BaseHandler
from tornado import gen
import datetime

# 主页
class HomeHandler(BaseHandler):
    def get(self, *args, **kwargs):
        print("HomeHandler")
        current_user = self.get_current_user()
        print(current_user)
        # 为访问者提供一个guest帐户
        if current_user == None:
            print("游客用户提供guest用户")
            self.session["username"] = "guest"
            current_user = "guest"
            self.session.save()
        return self.render('main.html', username = current_user)
    def post(self, *args, **kwargs):
        print(args)

# 新闻
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
        self.render("newsshow.html", colls = colls, username = self.get_current_user())

# 新闻详情
class NewDetailShowHandler(BaseHandler):
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self, *args, **kwargs):
        newstitle = args[0]
        print(newstitle)
        doc_coll = yield self.db.news_detail.find_one({"newstitle":newstitle})
        self.render("newsdetailshow.html",coll = doc_coll)

# 关于我们
class AboutHandler(BaseHandler):
    def get(self, *args, **kwargs):
        username = self.get_current_user
        self.render("about.html", username = username)

# 个人主页
class PersonalHandler(BaseHandler):
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self, *args, **kwargs):
        username = self.get_current_user()
        coll = yield self.db.userinfo.find_one({"username":username})
        if(coll == None):
            print("用户信息不存在,异常情况")
            self.redirect("500.html")
        else:
            self.render("Personal.html",coll = coll)

#旅游网
class TourismHandler(BaseHandler):
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self, *args, **kwargs):
        self.render("Tourism.html", username =self.get_current_user())

#年代show
class AgesHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("ages.html", username = self.get_current_user())

#论坛
class ForumMainHandler(BaseHandler):
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self, *args, **kwargs):
        # 获取贴子类别
        cursor = self.db.post_category.find()
        colls = []
        i = 0
        while (yield cursor.fetch_next):
                coll = cursor.next_object()
                colls.append({})
                for k,v in coll.items():
                    colls[i][k]=v
                print(colls)
                i+=1
        # 获取被赞次数最多的帖子
        post_cursor = self.db.user_publish.find().sort([("ZambisCount",-1)]).limit(6)
        if(post_cursor != None):
            post_colls = []
            i = 0
            while (yield post_cursor.fetch_next):
                    coll = post_cursor.next_object()
                    post_colls.append({})
                    for k,v in coll.items():
                        post_colls[i][k]=v
                    print(post_colls[i])
                    i+=1
        self.render("forumMain.html", username = self.get_current_user(), colls= colls, post_colls = post_colls)


