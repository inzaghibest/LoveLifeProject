__author__ = 'zhangxp'

import tornado.web
from controller.base import BaseHandler
from tornado import gen

# 80主页
class EightyHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("80main.html")

# 80Show.html
class EightyAnimationHandler(BaseHandler):
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self, *args, **kwargs):
        print(args)
        if(args[0] == "animation"):
            cursor = self.db.animation_info.find()
        elif(args[0] == "game"):
            cursor = self.db.game_info.find()
        elif(args[0] == "music"):
            cursor = self.db.music_info.find()
        else:
            cursor = self.db.toys_info.find()
        colls = []
        i = 0
        while (yield cursor.fetch_next):
            coll = cursor.next_object()
            colls.append({})
            for k,v in coll.items():
                colls[i][k]=v
                print(colls)
            i+=1
        self.render("80Show.html", colls = colls, category = args[0])

# 80动画管理
class EightyAnimationManageHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("80AnimationManage.html", Message = "编辑80")
    @tornado.web.asynchronous
    @gen.coroutine
    def post(self, *args, **kwargs):
        category = self.get_argument("category")
        name = self.get_argument("name")
        print(name)
        imgurl = self.get_argument("imgurl")
        print(imgurl)
        descrip = self.get_argument("descrip")
        print(descrip)
        audiourl = self.get_argument("audiourl")
        if(category == "animation"):
            doc_coll = yield  self.db.animation_info.find_one({"name":name})
            table_name = "animation_info"
        elif(category == "music"):
            doc_coll = yield  self.db.music_info.find_one({"name":name})
            table_name = "music_info"
        elif(category == "game"):
            doc_coll = yield  self.db.game_info.find_one({"name":name})
            table_name = "game_info"
        else:
            doc_coll = yield  self.db.toys_info.find_one({"name":name})
            table_name = "toys_info"
        if(doc_coll != None):
            self.render("80AnimationManage.html", Message = "该名字已经存在!")
        else:
           yield self.db[table_name].insert({"name":name, "imgUrl":imgurl,
                                                 "descrp":descrip, "audioUrl":audiourl})
           self.render("80AnimationManage.html", Message = "添加成功!")


