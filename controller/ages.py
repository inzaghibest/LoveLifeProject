__author__ = 'zhangxp'

import tornado.web
from controller.base import BaseHandler
from tornado import gen

# 80主页
class EightyHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("80main.html")

# 80动画
class EightyAnimationHandler(BaseHandler):
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self, *args, **kwargs):
        cursor = self.db.animation_info.find()
        colls = []
        i = 0
        while (yield cursor.fetch_next):
            coll = cursor.next_object()
            colls.append({})
            for k,v in coll.items():
                colls[i][k]=v
                print(colls)
            i+=1
        self.render("80animation.html", colls = colls)

# 80动画管理
class EightyAnimationManageHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("80AnimationManage.html", Message = "添加动画")
    @tornado.web.asynchronous
    @gen.coroutine
    def post(self, *args, **kwargs):
        name = self.get_argument("aname")
        print(name)
        imgurl = self.get_argument("animationImg")
        print(imgurl)
        animationDescrp = self.get_argument("animationDescrip")
        print(animationDescrp)
        doc_coll = yield self.db.animation_info.find_one({"animationName":name})
        if(doc_coll != None):
            self.render("80AnimationManage.html", Message = "该动画已经存在")
        else:
            yield self.db.animation_info.insert({"animationName":name, "imgUrl":imgurl,
                                                 "animationDescrp":animationDescrp})
            self.render("80AnimationManage.html", Message = "动画添加成功")

