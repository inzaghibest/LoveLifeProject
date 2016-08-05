__author__ = 'zhangxp'
import tornado.web
from controller.base import BaseHandler
from tornado import gen

class OlympicMainHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("OlympicMain.html", username = self.get_current_user())

# 奥运新闻主页
class OlympicNewsHandler(BaseHandler):
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self, *args, **kwargs):
        # 获取奥运新闻
        category = args[0]
        print(category)
        if(category == "RealTime"):
            cursor = self.db.aoyun_news_table.find().sort([("publish",-1)]).limit(10)
        else:
            cursor = self.db.aoyun_news_table.find().sort([("publish",-1)]).limit(10)
        if(cursor != None):
            colls = []
            i = 0
            while (yield cursor.fetch_next):
                    coll = cursor.next_object()
                    colls.append({})
                    for k,v in coll.items():
                        colls[i][k]=v
                    print(colls)
                    i+=1
        self.render("OlyNewsMain.html", colls = colls)

