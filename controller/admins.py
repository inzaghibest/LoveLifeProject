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
        return self.render("news.html")



