__author__ = 'zhxp'
import tornado.web
from controller.base import BaseHandler
from tornado import gen


# 职业页面
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
        self.render("proanaly.html", colls =colls, username = self.get_current_user())

# 职业展示页面
class ShowHandler(BaseHandler):
    def get(self, *args, **kwargs):
        # 获取职业名称
        occupation = args[0]
        print(occupation)
        # 生成此职位在各个地区的需求程度,柱状图
        #occupation = self.get_argument("occupation");
        #print(occupation)
      # picinterfaces.zp_show_oneZw_gzddCounts_Bar(occupation, 'static/images/OccupationPic/%sForArea.png'%occupation)
        # 生成此职业不同经验的需求程度
       # picinterfaces.zp_show_oneZw_gzjyCounts_Bar(occupation,'static/images/OccupationPic/%sForExperience.png'%occupation)
        # 生成此职业不同学历的需求程度
        #picinterfaces.zp_show_oneZw_xlCounts_Bar(occupation,'static/images/OccupationPic/%sForEducation.png'%occupation)
        self.render("show.html",occupation = occupation,current_time = self.get_current_time())