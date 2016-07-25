__author__ = 'zhxp'
import tornado.web
import tornado.gen
from tornado import gen
from controller.base import BaseHandler

class AdminsHandler(BaseHandler):
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self, *args, **kwargs):
                cursor = self.db.userinfo.find()
                print(cursor)
                print(self.db)
                print(self.db.userinfo)
                colls = []
                dict = {}
                i = 0
                while (yield cursor.fetch_next):
                    coll = cursor.next_object()
                    colls.append({})
                    for k,v in coll.items():
                        colls[i][k]=v
                    print(colls)
                    i+=1
                return self.render("admins.html", colls =colls)
class AnalyHandler(BaseHandler):
    def get(self, *args, **kwargs):
        return self.render("analy.html",Message = "添加职业类别")
    @tornado.web.asynchronous
    @gen.coroutine
    def post(self, *args, **kwargs):
        category = self.get_body_argument("category")
        occupation = self.get_body_argument("occupation")
        print(category)
        print(occupation)
        msg = ""
        doc_coll = yield self.db.occupation_info.find_one({"category":category})
        # 存在不做操作,否则插入
        if(doc_coll != None):
            listocc = []
            for k, v in doc_coll.items():
                if(k == "occupation"):
                    for item in v:
                        if(item != occupation):
                          listocc.append(item)
                          print(listocc)
            listocc.append(occupation)
            print(listocc)
            doc_coll["occupation"] = listocc
            print(doc_coll["occupation"])
            self.db.occupation_info.update({"category":category},doc_coll)
            msg = "更新成功!"
        else:
            print("不存在")
            listocc =[occupation]
            self.db.occupation_info.insert({"category":category, "occupation":listocc})
            msg = "插入成功"
        self.render("analy.html", Message = msg)



class NewsHandler(BaseHandler):
    def get(self, *args, **kwargs):
        return self.render("news.html", Message = "添加新闻")
    @tornado.web.asynchronous
    @gen.coroutine
    def post(self, *args, **kwargs):
        print("news post")
        newscategory = self.get_body_argument("newscategory")
        print(newscategory)
        newstitle = self.get_body_argument("newstitle")
        print(newstitle)
        newstext = self.get_body_argument("newstext")
        print(newstext)
        newsauthor = self.get_body_argument("newsauthor")
        print(newsauthor)
        newsdate = self.get_body_argument("newsdate")
        print(newsdate)
        newsimg = self.get_body_argument("newsimg")
        print(newsimg)
        msg = ""
        doc_coll = yield self.db.news_collection.find_one({"newscategory":newscategory})
        # 新闻的存储模型,存储在两个集合中news_collection和news_detail
        # news_collection:{"newscategory":newscategory, "newstitle":['1','2','3']}
        # news_detail:{"newstitle":newstitle, "newstext":newstext,...}
        # 这样存储是为了便于分类展示新闻标题,点击新闻标题获取新闻详情
        # 存在更新操作,否则插入
        if(doc_coll != None):
            print(doc_coll)
            self.db.news_collection.update({"newscategory":newscategory},{"$addToSet":{"newstitle":newstitle}})
            newsdetail = yield self.db.news_detail.find_one({"newstitle":newstitle})
            print(newsdetail)
            if(newsdetail == None):
                print("insert")
                msg = "插入成功!"
                self.db.news_detail.insert({"newstitle":newstitle, "newstext":newstext, "newsdate":newsdate,"newsauthor":newsauthor})
            else:
                print("update")
                self.db.news_detail.update({"newstitle":newstitle},{"$set":{"newstext":newstext, "newsdate":newsdate,"newsauthor":newsauthor}})
        # if(doc_coll != None):
        #     listocc = []
        #     for k, v in doc_coll.items():
        #         if(k == "newstitle"):
        #             for item in v:
        #                 if(item == newstitle):
        #                     msg = "新闻已经存在了"
        #                     print(msg)
        #                     break;
        #                 else:
        #                   listocc.append(item)
        #                   print(listocc)
        #     if(msg == "新闻已经存在了"):
        #         self.render("news.html", Message = msg)
        #     else:
        #         listocc.append(newstitle)
        #         print(listocc)
        #         doc_coll["newstitle"] = listocc
        #         print(doc_coll["newstitle"])
        #         self.db.news_collection.update({"newscategory":newscategory},doc_coll)
        #         self.db.news_detail.insert({"newstitle":newstitle, "newstext":newstext, "newsdate":newsdate,
        #                                     "newsauthor":newsauthor})
                msg = "更新成功!"
        else:
            print("不存在")
            listocc =[newstitle]
            self.db.news_collection.insert({"newscategory":newscategory, "newstitle":listocc})
            self.db.news_detail.insert({"newstitle":newstitle, "newstext":newstext, "newsdate":newsdate,
                                        "newsauthor":newsauthor})
            msg = "插入成功"
        self.render("news.html", Message = msg)









